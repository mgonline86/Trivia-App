import os
from sqlalchemy import func
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category, User

QUESTIONS_PER_PAGE = 10


def paginate_questions(request, selection):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE

    questions = [question.format() for question in selection]
    current_questions = questions[start:end]

    return current_questions


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)

    '''
  @TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
  '''
    CORS(app, resources={r"http://127.0.0.1:5000/*": {"origins": "*"}})
    '''
  @TODO: Use the after_request decorator to set Access-Control-Allow
  '''
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET,PATCH,POST,DELETE,OPTIONS')
        return response
    '''
  @TODO: 
  Create an endpoint to handle GET requests 
  for all available categories.
  '''
    @app.route('/categories')
    def retrieve_categories():
        categories = Category.query.order_by(Category.id).all()
        categories_list = {}
        for cat in categories:
            categories_list[str(cat.id)] = cat.type

        if len(categories_list) == 0:
            abort(404)

        return jsonify({
            'success': True,
            'categories': categories_list
        })
    '''
  @TODO: 
  Create an endpoint to handle GET requests for questions, 
  including pagination (every 10 questions). 
  This endpoint should return a list of questions, 
  number of total questions, current category, categories. 

  TEST: At this point, when you start the application
  you should see questions and categories generated,
  ten questions per page and pagination at the bottom of the screen for three pages.
  Clicking on the page numbers should update the questions. 
  '''
    @app.route('/questions')
    def retrieve_questions():
        selection = Question.query.order_by(Question.id).all()
        current_questions = paginate_questions(request, selection)
        categories = Category.query.order_by(Category.id).all()
        categories_list = {}
        for cat in categories:
            categories_list[str(cat.id)] = cat.type
        current_category = []
        for cat in current_questions:
            if cat['category'] not in current_category:
                current_category.append(cat['category'])

        if len(current_questions) == 0:
            abort(404)

        return jsonify({
            'success': True,
            'questions': current_questions,
            'total_questions': len(Question.query.all()),
            'categories': categories_list,
            'current_category': current_category
        })

    '''
  @TODO: 
  Create an endpoint to DELETE question using a question ID. 

  TEST: When you click the trash icon next to a question, the question will be removed.
  This removal will persist in the database and when you refresh the page. 
  '''
    @app.route('/questions/<int:question_id>', methods=['DELETE'])
    def delete_question(question_id):
        body = request.get_json()
        try:
            question = Question.query.filter(
                Question.id == question_id).one_or_none()
            if question is None:
                abort(404)

            question.delete()
            received_questions = body.get('questions')
            received_questions_ids = []
            for question in received_questions:
                if question['id'] != question_id:
                    received_questions_ids.append(question['id'])
            selection = Question.query.filter(Question.id.in_(
                received_questions_ids)).order_by(Question.id).all()
            current_questions = paginate_questions(request, selection)

            return jsonify({
                'success': True,
                'deleted': question_id,
                'questions': current_questions,
                'total_questions': len(Question.query.all())
            })
        except:
            abort(422)
    '''
  @TODO: 
  Create an endpoint to POST a new question, 
  which will require the question and answer text, 
  category, and difficulty score.

  TEST: When you submit a question on the "Add" tab, 
  the form will clear and the question will appear at the end of the last page
  of the questions list in the "List" tab.  
  '''

    '''
  @TODO: 
  Create a POST endpoint to get questions based on a search term. 
  It should return any questions for whom the search term 
  is a substring of the question. 

  TEST: Search by any phrase. The questions list will update to include 
  only question that include that string within their question. 
  Try using the word "title" to start. 
  '''

    @app.route('/questions', methods=['POST'])
    def create_question():
        body = request.get_json()
        new_question = body.get('question')
        new_answer = body.get('answer')
        new_difficulty = body.get('difficulty')
        new_rating = body.get('rating')
        new_category = body.get('category')
        query = body.get('searchTerm')

        try:
            if query:
                selection = Question.query.order_by(Question.id).filter(
                    Question.question.ilike('%'+query+'%')).all()
                current_questions = paginate_questions(request, selection)
                categories = Category.query.order_by(Category.id).all()
                categories_list = [category.type for category in categories]

                return jsonify({
                    'success': True,
                    'questions': current_questions,
                    'total_questions': len(selection)})

            else:
                question = Question(question=new_question, answer=new_answer,
                                    difficulty=new_difficulty, rating=new_rating, category=new_category)
                question.insert()

                selection = Question.query.order_by(Question.id).all()
                current_questions = paginate_questions(request, selection)

                return jsonify({
                    'success': True,
                    'created': question.id,
                    'questions': current_questions,
                    'total_questions': len(Question.query.all())
                })
        except:
            abort(422)

    '''
  @TODO: 
  Create a GET endpoint to get questions based on category. 

  TEST: In the "List" tab / main screen, clicking on one of the 
  categories in the left column will cause only questions of that 
  category to be shown. 
  '''
    @app.route('/categories/<int:category_id>/questions')
    def retrieve_question_by_category(category_id):
        selection = Question.query.filter(
            Question.category == category_id).order_by(Question.id).all()
        current_questions = paginate_questions(request, selection)

        if len(current_questions) == 0:
            abort(404)

        return jsonify({
            'success': True,
            'questions': current_questions,
            'total_questions': len(selection)
        })

    '''
  @TODO: 
  Create a POST endpoint to get questions to play the quiz. 
  This endpoint should take category and previous question parameters 
  and return a random questions within the given category, 
  if provided, and that is not one of the previous questions. 

  TEST: In the "Play" tab, after a user selects "All" or a category,
  one question at a time is displayed, the user is allowed to answer
  and shown whether they were correct or not. 
  '''
    @app.route('/quizzes', methods=['POST'])
    def start_quizz():

        body = request.get_json()
        quiz_category = body.get('quiz_category')
        previousQuestions = body.get('previous_questions')
        try:
            if quiz_category.get('id') == 0:
                selection = Question.query.order_by(func.random()).filter(
                    ~Question.id.in_(previousQuestions)).first()
                total_questions = len(Question.query.all())
            else:
                id = int(quiz_category.get('id'))
                selection = Question.query.order_by(func.random()).filter(
                    Question.category == id, ~Question.id.in_(previousQuestions)).first()
                total_questions = len(Question.query.filter(
                    Question.category == id).all())

            if total_questions == len(previousQuestions) and len(previousQuestions) != 0:
                return jsonify({
                    'success': True,
                    'currentQuestion': {}
                })
            else:
                question = selection.format()
                return jsonify({
                    'success': True,
                    'currentQuestion': question
                })
        except:
            abort(422)

  # User login handler
    @app.route('/login', methods=['POST'])
    def user_login():
        body = request.get_json()
        username = body.get('username')
        password = body.get('password')
        d_user = User.query.filter(
            User.username == username).first()
        try:
            if password == d_user.password:
                d_user.status = True
                d_user.update()
                return jsonify({
                    'success': True,
                    'correct_password': True
                })
            else:
                return jsonify({
                    'success': True,
                    'correct_password': False
                })
        except:
            abort(422)

  # User register handler

    @app.route('/register', methods=['POST'])
    def user_register():
        try:
            body = request.get_json()
            new_username = body.get('username')
            new_password = body.get('password')
            user = User(username=new_username, password=new_password,
                        score=0, status=False)
            user.insert()
            return jsonify({
                'success': True,
                'created': user.id
            })

        except:
            abort(422)

  # User status handler

    @app.route('/status', methods=['POST'])
    def reset_users():
        try:
            guest = User.query.filter(User.username == 'Guest').first()
            guest.score = 0
            guest.update()
            users = User.query.filter(User.status == True).all()
            for user in users:
                user.status = False
                user.update()
            return jsonify({
                'success': True,
                'status_reset': True
            })
        except:
            abort(422)

  # Retrieving user data handler

    @app.route('/users')
    def retrieve_user():
        try:
            user = User.query.filter_by(status=True).first()
            current_user = user.format()
            if len(current_user) == 0:
                abort(404)

            return jsonify({
                'success': True,
                'currentUser': current_user
            })
        except:
            abort(422)

  # Tracking user score handler

    @app.route('/scores', methods=['POST'])
    def set_score():
        try:
            body = request.get_json()
            numCorrect = body.get('numCorrect')
            previousNumCorrect = body.get('previousNumCorrect')
            scoreAdded = numCorrect-previousNumCorrect
            user = User.query.filter_by(status=True).first()
            user.score = user.score+scoreAdded
            user.update()
            return jsonify({
                'success': True,
                'currentScore': user.score,
                'previousNumCorrect': numCorrect
            })
        except:
            abort(422)

  # Adding new category handler

    @app.route('/categories', methods=['POST'])
    def add_categories():
        try:
            body = request.get_json()
            new_category = body.get('newCategory')
            category = Category(type=new_category)
            category.insert()
            categories = Category.query.order_by(Category.id).all()
            categories_list = {}
            for cat in categories:
                categories_list[str(cat.id)] = cat.type
            return jsonify({
                'success': True,
                'created': category.id,
                'categories': categories_list
            })

        except:
            abort(422)

  # Changing a question's rating handler

    @app.route('/questions/<int:question_id>', methods=['PATCH'])
    def rate_question(question_id):
        try:
            question = Question.query.filter(
                Question.id == question_id).first()
            body = request.get_json()
            new_rating = body.get('rating')
            question.rating = new_rating
            question.update()
            received_questions = body.get('questions')
            received_questions_ids = []
            for q in received_questions:
                received_questions_ids.append(q['id'])
            selection = Question.query.filter(Question.id.in_(
                received_questions_ids)).order_by(Question.id).all()
            current_questions = paginate_questions(request, selection)

            return jsonify({
                'success': True,
                'updated': question.id,
                'questions': current_questions
            })
        except:
            abort(422)

    '''
  @TODO: 
  Create error handlers for all expected errors 
  including 404 and 422. 
  '''

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
        }), 404

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "bad request"
        }), 400

    @app.errorhandler(405)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 405,
            "message": "method not allowed"
        }), 405

    @app.errorhandler(500)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 500,
            "message": "internal server error"
        }), 500
    return app
