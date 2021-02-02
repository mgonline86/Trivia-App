import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category, User


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgres://{}:{}@{}/{}".format(
            'M&A', 'JiMmY1986$', 'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

        self.new_question = {
            'question': 'What are you testing?',
            'answer': 'I am testing you',
            'difficulty': 5,
            'rating': 5,
            'category': 3
        }

        self.new_quiz = {
            'quiz_category': {'type': 'Science', 'id': '1'},
            'previous_questions': []
        }

        self.deleted_id = Question.query.filter(
            Question.answer == 'The Liver').first().id

        self.del_state_questions = {
            'questions': [{
                'id': 5, 'question': """Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?""",
                'answer': 'Maya Angelou',
                'difficulty': 2,
                'rating': 4,
                'category': 4
            }, {
                'id': self.deleted_id,
                'question': 'What is the heaviest organ in the human body?',
                'answer': 'The Liver',
                'difficulty': 4,
                'rating': 4,
                'category': 1
            }]
        }

        self.del_return_questions = [
            {
                'id': 5, 'question': """Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?""",
                'answer': 'Maya Angelou',
                'difficulty': 2,
                'rating': 4,
                'category': 4
            }
        ]

        self.new_user = {
            'username': 'user5',
            'password': 'pass5'
        }

        self.user_score = {
            'numCorrect': 4,
            'previousNumCorrect': 3
        }

    def tearDown(self):
        deleted_question = Question.query.filter(
            Question.answer == 'The Liver').first()
        if deleted_question is None:
            body = {
                'question': 'What is the heaviest organ in the human body?',
                'answer': 'The Liver',
                'difficulty': 4,
                'rating': 4,
                'category': 1
            }
            new_question = body.get('question')
            new_answer = body.get('answer')
            new_difficulty = body.get('difficulty')
            new_category = body.get('category')
            new_rating = body.get('rating')
            question = Question(question=new_question, answer=new_answer,
                                difficulty=new_difficulty, category=new_category, rating=new_rating)
            question.insert()
            print('q_un-del')

        created_question = Question.query.filter(
            Question.answer == 'I am testing you').first()
        if created_question:
            created_question.delete()
            print('q_un-create')

        created_user = User.query.filter(
            User.username == 'user5').first()
        if created_user:
            created_user.delete()
            print('u_un-create')

        created_category = Category.query.filter(
            Category.type == 'Physics').first()
        if created_category:
            created_category.delete()
            print('c_un-create')
    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """

    # Testing endpoint to GET requests for all available categories.
    def test_get_categories(self):
        res = self.client().get('/categories')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['categories']))

    def test_405_if_put_categories_not_allowed(self):
        res = self.client().put('/categories')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'method not allowed')

    # Testing endpoint to GET requests for questions, including pagination (every 10 questions).

    def test_get_paginated_questions(self):
        res = self.client().get('/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['questions'])
        self.assertTrue(len(data['questions']))
        self.assertTrue(data['total_questions'])
        self.assertTrue(data['categories'])
        self.assertTrue(len(data['categories']))
        self.assertTrue(data['current_category'])
        self.assertTrue(len(data['current_category']))

    def test_404_sent_requesting_beyond_valid_page(self):
        res = self.client().get('/questions?page=1000',
                                json={'current_category': [1]})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    # Testing endpoint to DELETE question using a question ID.

    def test_delete_question(self):
        res = self.client().delete('/questions/'+str(self.deleted_id),
                                   json=self.del_state_questions)
        data = json.loads(res.data)

        question = Question.query.filter(
            Question.id == self.deleted_id).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], self.deleted_id)
        self.assertTrue(data['total_questions'])
        self.assertTrue(len(data['questions']))
        self.assertTrue(data['questions'])
        self.assertEqual(data['questions'], self.del_return_questions)
        if res.status_code == 200:
            print('q_del')

    def test_422_if_question_does_not_exist(self):
        res = self.client().delete('/questions/1000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

    # Testing endpoint to POST a new question.

    def test_create_new_question(self):
        res = self.client().post('/questions', json=self.new_question)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['created'])
        self.assertTrue(data['questions'])
        self.assertTrue(len(data['questions']))
        self.assertTrue(data['total_questions'])
        if res.status_code == 200:
            print('q_create')

    def test_405_if_question_creation_not_allowed(self):
        res = self.client().post('/questions/45', json=self.new_question)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'method not allowed')

    # Testing endpoint to GET requests for questions based on category, including pagination (every 10 questions).

    def test_get_paginated_questions_by_category(self):
        res = self.client().get('/categories/1/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['questions'])
        self.assertTrue(len(data['questions']))
        self.assertTrue(data['total_questions'])

    def test_404_sent_requesting_beyond_valid_page_by_category(self):
        res = self.client().get('/categories/1/questions?page=1000',
                                json={'current_category': [1]})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    # Testing endpoint to POST a quiz.

    def test_quiz_start(self):
        res = self.client().post('/quizzes', json=self.new_quiz)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['currentQuestion'])

    def test_404_if_quiz_start_fails(self):
        res = self.client().post('/quizzes/45', json=self.new_quiz)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    # Testing endpoint to POST a search.

    def test_get_questions_search_with_results(self):
        res = self.client().post('/questions', json={'searchTerm': 'name'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['questions'])
        self.assertEqual(len(data['questions']), 2)
        self.assertTrue(data['total_questions'])

    def test_get_questions_search_without_results(self):
        res = self.client().post('/questions', json={'searchTerm': 'lolo'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(len(data['questions']), 0)
        self.assertEqual(data['total_questions'], 0)

    # Testing endpoint to POST a user login.

    def test_login_user_with_correct_pass(self):
        res = self.client().post(
            '/login', json={'username': 'user1', 'password': 'pass1'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['user_exist'], True)

    def test_login_user_with_wrong_pass(self):
        res = self.client().post(
            '/login', json={'username': 'user1', 'password': 'xxxxx'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['user_exist'], False)

    def test_login_user_do_not_exist(self):
        res = self.client().post(
            '/login', json={'username': 'xxxxx', 'password': 'xxxxx'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

    # Testing endpoint to POST new user.

    def test_create_new_user(self):
        res = self.client().post('/register', json=self.new_user)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['created'])
        if res.status_code == 200:
            print('u_create')

    def test_405_if_user_creation_fails(self):
        res = self.client().post('/register')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

        # Testing endpoint to POST users status reset.

    def test_user_status_reset(self):
        res = self.client().post('/status')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['status_reset'], True)

    def test_404_if_status_reset_fails(self):
        res = self.client().post('/status/45')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    # Testing endpoint to GET requests for active user.
    def test_get_active_user(self):
        active_user = User.query.filter(User.status == True).first()
        if active_user is None:
            active_user = User.query.first()
            active_user.status = True
            active_user.update()
        res = self.client().get('/users')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['currentUser']))
        users = User.query.filter(User.status == True).all()
        for user in users:
            user.status = False
            user.update()

    def test_422_if_get_active_user_fails(self):
        res = self.client().get('/users')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

    # Testing endpoint to POST user's score.

    def test_update_user_score(self):
        users = User.query.filter(User.status == True).all()
        for user in users:
            user.status = False
            user.update()

        active_user = User.query.filter(User.username == 'Guest').first()
        active_user.status = True
        active_user.score = 0
        active_user.update()

        res = self.client().post('/scores', json=self.user_score)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['currentScore'])
        self.assertEqual(data['currentScore'], 1)
        self.assertTrue(data['previousNumCorrect'])
        self.assertEqual(data['previousNumCorrect'], 4)

    def test_404_if_update_user_score_fails(self):
        res = self.client().post('/scores/45', json=self.user_score)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    # Testing endpoint to POST new category.

    def test_create_new_category(self):
        res = self.client().post(
            '/categories', json={'newCategory': 'Physics'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['categories'])
        self.assertTrue(len(data['categories']))
        if res.status_code == 200:
            print('c_create')

    def test_422_if_category_creation_fails(self):
        res = self.client().post('/categories')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

    # Testing endpoint to PATCH question rating.

    def test_update_question_rating(self):
        res = self.client().patch(
            '/questions/17', json={'rating': 5, 'questions': self.del_return_questions})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['updated'])
        self.assertEqual(data['updated'], 17)
        self.assertTrue(data['questions'])
        self.assertEqual(data['questions'], self.del_return_questions)
        self.assertTrue(len(data['questions']))

    def test_422_if_update_question_rating_fails(self):
        res = self.client().patch('/questions/17')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
