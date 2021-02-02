# Full Stack Trivia API Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Environment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virtual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by navigating to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server.

## Database Setup

With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:

```bash
psql trivia < trivia.psql
```

## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application.

## Tasks

One note before you delve into your tasks: for each endpoint you are expected to define the endpoint and response data. The frontend will be a plentiful resource because it is set up to expect certain endpoints and response data formats already. You should feel free to specify endpoints in your own way; if you do so, make sure to update the frontend or you will get some unexpected behavior.

1. Use Flask-CORS to enable cross-domain requests and set response headers.
2. Create an endpoint to handle GET requests for questions, including pagination (every 10 questions). This endpoint should return a list of questions, number of total questions, current category, categories.
3. Create an endpoint to handle GET requests for all available categories.
4. Create an endpoint to DELETE question using a question ID.
5. Create an endpoint to POST a new question, which will require the question and answer text, category, and difficulty score.
6. Create a POST endpoint to get questions based on category.
7. Create a POST endpoint to get questions based on a search term. It should return any questions for whom the search term is a substring of the question.
8. Create a POST endpoint to get questions to play the quiz. This endpoint should take category and previous question parameters and return a random questions within the given category, if provided, and that is not one of the previous questions.
9. Create error handlers for all expected errors including 400, 404, 422 and 500.

REVIEW_COMMENT

This README is missing documentation of your endpoints. Below is an example for your endpoint to get all categories. Please use it as a reference for creating your documentation and resubmit your code.

Endpoints
GET '/categories'
GET ...
POST ...
DELETE ...

---

---

# API REFERENCE

## `Getting Started`

---

- Base URL: At present this app can only run locally and is not hosted as a base URL. The backend app is hosted at the default, `http://127.0.0.1:5000/`, which is set as a proxy in the frontend configuration.
- Authentication: This version of the application does not require authentication of API keys.

## `Error Handling`

---

The following errors are returned as JSON object in the following format:

```
{
  "error": 404,
  "message": "resource not found",
  "success": false
}
```

The API will return five error types when request fail:

- ### 400: Bad Request
- ### 422: Unprocessable
- ### 404: Resource Not Found
- ### 405: Method Not Allowed
- ### 500: Internal Server Error

## ` Endpoints`

---

### ALL CATEGORIES

**`GET` /categories**

Returns a dictionary of all available categories in which the keys are the ids and the value is the corresponding string of the category.

**Endpoint URL**

```
http://127.0.0.1:5000/categories
```

**Example**

_Request:_

```
curl http://127.0.0.1:5000/categories
```

_Responses:_

```
{'1' : "Science",
'2' : "Art",
'3' : "Geography",
'4' : "History",
'5' : "Entertainment",
'6' : "Sports"}
```

### ALL QUESTIONS

**`GET` /questions**

Returns a variety of information about all available questions in the form of an object of five keys.

**Endpoint URL**

```
http://127.0.0.1:5000/questions
```

**Query parameters**

| Name                      |  Type   | Description                                                                                                                                                                           |
| ------------------------- | :-----: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`page`**_` (OPTIONAL)`_ | Integer | The requested questions page where questions are paginated by ten questions per page, if the page parameter wasn't included it will always response with the first page of questions. |

**Response fields**

| Name                   |  Type   | Description                                                                                                                       |
| ---------------------- | :-----: | --------------------------------------------------------------------------------------------------------------------------------- |
| **`success`**          | Boolean | The request process success condition.                                                                                            |
| **`questions`**        |  List   | A list of question objects limited by ten objects for the requested questions page.                                               |
| **`total_questions`**  | Integer | The total number of all available questions.                                                                                      |
| **`categories`**       | Object  | A dictionary of all available categories in which the keys are the ids and the value is the corresponding string of the category. |
| **`current_category`** |  list   | A list of integer numbers each one represent a unique category id.                                                                |

**Example**

_Request:_

```
curl http://127.0.0.1:5000/questions?page=2
```

_Responses:_

```
{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports",
  },
  "current_category": [
    3,
    2,
    1,
    4
  ],
  "questions": [
    {
      "answer": "Agra",
      "category": 3,
      "difficulty": 2,
      "id": 15,
      "question": "The Taj Mahal is located in which Indian city?",
      "rating": 2
    },
    {
      "answer": "Escher",
      "category": 2,
      "difficulty": 1,
      "id": 16,
      "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?",
      "rating": 3
    },
    {
      "answer": "Mona Lisa",
      "category": 2,
      "difficulty": 3,
      "id": 17,
      "question": "La Giaconda is better known as what?",
      "rating": 3
    },
    {
      "answer": "One",
      "category": 2,
      "difficulty": 4,
      "id": 18,
      "question": "How many paintings did Van Gogh sell in his lifetime?",
      "rating": 5
    },
    {
      "answer": "Jackson Pollock",
      "category": 2,
      "difficulty": 2,
      "id": 19,
      "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?",
      "rating": 5
    },
    {
      "answer": "The Liver",
      "category": 1,
      "difficulty": 4,
      "id": 20,
      "question": "What is the heaviest organ in the human body?",
      "rating": 2
    },
    {
      "answer": "Alexander Fleming",
      "category": 1,
      "difficulty": 3,
      "id": 21,
      "question": "Who discovered penicillin?",
      "rating": 4
    },
    {
      "answer": "Blood",
      "category": 1,
      "difficulty": 4,
      "id": 22,
      "question": "Hematology is a branch of medicine involving the study of what?",
      "rating": 3
    },
    {
      "answer": "Scarab",
      "category": 4,
      "difficulty": 4,
      "id": 23,
      "question": "Which dung beetle was worshipped by the ancient Egyptians?",
      "rating": 4
    }
  ],
  "success": true,
  "total_questions": 19
}
```

### QUESTIONS BY CATEGORY

**`GET` /categories/<category_id>/questions**

Returns a variety of information about all questions of one category in the form of an object of three keys.

**Endpoint URL**

```
http://127.0.0.1:5000/categories/<category_id>/questions
```

**Path parameters**

| Name                             |  Type  | Description                               |
| -------------------------------- | :----: | ----------------------------------------- |
| **`category_id`**_` (REQUIRED)`_ | String | The unique id for the requested category. |

**Response fields**

| Name                  |  Type   | Description                                                                   |
| --------------------- | :-----: | ----------------------------------------------------------------------------- |
| **`success`**         | Boolean | The request process success condition.                                        |
| **`questions`**       |  List   | A list of question objects limited by ten objects for the requested category. |
| **`total_questions`** | Integer | The total number of all questions available.                                  |

**Example**

_Request:_

```
curl http://127.0.0.1:5000/categories/6/questions
```

_Responses:_

```
{
  "questions": [
    {
      "answer": "Brazil",
      "category": 6,
      "difficulty": 3,
      "id": 10,
      "question": "Which is the only team to play in every soccer World Cup tournament?",
      "rating": 3
    },
    {
      "answer": "Uruguay",
      "category": 6,
      "difficulty": 4,
      "id": 11,
      "question": "Which country won the first ever soccer World Cup in 1930?",
      "rating": 3
    }
  ],
  "success": true,
  "total_questions": 2
}
```

### ACTIVE USER DATA

**`GET` /users**

Returns a variety of information about current active user in the form of an object of two keys.

**Endpoint URL**

```
http://127.0.0.1:5000/users
```

**Response fields**

| Name              |  Type   | Description                                                            |
| ----------------- | :-----: | ---------------------------------------------------------------------- |
| **`success`**     | Boolean | The request process success condition.                                 |
| **`currentUser`** | Object  | A user object of five keys for the user having his status set to True. |

**Example**

_Request:_

```
curl http://127.0.0.1:5000/users
```

_Responses:_

```
{
  "currentUser": {
    "id": 2,
    "password": "pass1",
    "score": 24,
    "status": true,
    "username": "user1"
  },
  "success": true
}
```

### ADD A NEW QUESTION

**`POST` /questions**

Adds a new question to the database by receiving a JSON body with the request and returns an object of four keys.

**Endpoint URL**

```
http://127.0.0.1:5000/questions
```

**JSON body parameters**

| Name                            |  Type   | Description                                               |
| ------------------------------- | :-----: | --------------------------------------------------------- |
| **`question`**_` (REQUIRED)`_   | String  | The text body containing the new question.                |
| **`answer`**_` (REQUIRED)`_     | String  | The text body containing the submitted question's answer. |
| **`difficulty`**_` (REQUIRED)`_ | Integer | The level of difficulty for the submitted question.       |
| **`rating`**_` (REQUIRED)`_     | Integer | The initial rating for the submitted question.            |
| **`category`**_` (REQUIRED)`_   | Integer | The unique category id for the submitted question.        |

**Response fields**

| Name                  |  Type   | Description                                        |
| --------------------- | :-----: | -------------------------------------------------- |
| **`success`**         | Boolean | The request process success condition.             |
| **`created`**         | Integer | The unique id number of the created question.      |
| **`questions`**       |  List   | A list of question objects limited by ten objects. |
| **`total_questions`** | Integer | The total number of all available questions.       |

**Example**

_Request:_

```
curl -X POST -H "Content-Type:application/json" -d '{"question":"What's your name?","answer":"I am Jimmy","category":3,"difficulty":3}' http://127.0.0.1:5000/questions
```

_Responses:_

```
{
  "created": 60,
  "questions": [
    {
      "answer": "Apollo 13",
      "category": 5,
      "difficulty": 4,
      "id": 2,
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?",
      "rating": 2
    },
    {
      "answer": "Tom Cruise",
      "category": 5,
      "difficulty": 4,
      "id": 4,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?",
      "rating": 3
    },
    {
      "answer": "Maya Angelou",
      "category": 4,
      "difficulty": 2,
      "id": 5,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?",
      "rating": 3
    },
    {
      "answer": "Edward Scissorhands",
      "category": 5,
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?",
      "rating": 3
    },
    {
      "answer": "Muhammad Ali",
      "category": 4,
      "difficulty": 1,
      "id": 9,
      "question": "What boxer's original name is Cassius Clay?",
      "rating": 2
    },
    {
      "answer": "Brazil",
      "category": 6,
      "difficulty": 3,
      "id": 10,
      "question": "Which is the only team to play in every soccer World Cup tournament?",
      "rating": 3
    },
    {
      "answer": "Uruguay",
      "category": 6,
      "difficulty": 4,
      "id": 11,
      "question": "Which country won the first ever soccer World Cup in 1930?",
      "rating": 3
    },
    {
      "answer": "George Washington Carver",
      "category": 4,
      "difficulty": 2,
      "id": 12,
      "question": "Who invented Peanut Butter?",
      "rating": 2
    },
    {
      "answer": "Lake Victoria",
      "category": 3,
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?",
      "rating": 2
    },
    {
      "answer": "The Palace of Versailles",
      "category": 3,
      "difficulty": 3,
      "id": 14,
      "question": "In which royal palace would you find the Hall of Mirrors?",
      "rating": 2
    }
  ],
  "success": true,
  "total_questions": 21
}
```

### SEARCH FOR QUESTIONS

**`POST` /questions**

Search for questions containing the search term in their question's head text, it receives a JSON body with the request and returns a variety of information about all available questions containing the search term in the form of an object of three keys.

**Endpoint URL**

```
http://127.0.0.1:5000/questions
```

**JSON body parameters**

| Name                            |  Type  | Description                                             |
| ------------------------------- | :----: | ------------------------------------------------------- |
| **`searchTerm`**_` (REQUIRED)`_ | String | The search term to match with the question's head text. |

**Response fields**

| Name                  |  Type   | Description                                                                   |
| --------------------- | :-----: | ----------------------------------------------------------------------------- |
| **`success`**         | Boolean | The request process success condition.                                        |
| **`questions`**       |  List   | A list of question objects containing the search term limited by ten objects. |
| **`total_questions`** | Integer | The total number of all available questions containing the search term.       |

**Example**

_Request:_

```
curl -X POST -H "Content-Type:application/json" -d '{"searchTerm":"name"}' http://127.0.0.1:5000/questions
```

_Responses:_

```
{
  "questions": [
    {
      "answer": "Muhammad Ali",
      "category": 4,
      "difficulty": 1,
      "id": 9,
      "question": "What boxer's original name is Cassius Clay?",
      "rating": 2
    },
    {
      "answer": "Brazil",
      "category": 6,
      "difficulty": 3,
      "id": 10,
      "question": "Which is the only team to play in every soccer World Cup tournament?",
      "rating": 3
    }
  ],
  "success": true,
  "total_questions": 2
}
```

### START A QUIZ

**`POST` /quizzes**

Get a random question, it receives a JSON body with the request and returns a random question.

**Endpoint URL**

```
http://127.0.0.1:5000/quizzes
```

**JSON body parameters**

| Name                                    |  Type  | Description                                                                                                                                                         |
| --------------------------------------- | :----: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`quiz_category`**_` (REQUIRED)`_      | Object | A dictionary of one key string id and its value integer number of the desired category id, to get a question from any category the value of id sent should be zero. |
| **`previous_questions`**_` (REQUIRED)`_ |  List  | List of all questions (id)s that should not be included in the response.                                                                                            |

**Response fields**

| Name                  |  Type   | Description                                                                                                                                                                                                        |
| --------------------- | :-----: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **`success`**         | Boolean | The request process success condition.                                                                                                                                                                             |
| **`currentQuestion`** | Object  | A random question from the requested category with id outside the previous_questions parameter, incase there is no question's id outside the previous_questions parameter currentQuestion will be an empty object. |

**Example**

_Request:_

```
curl -X POST -H "Content-Type:application/json" -d '{"previous_questions":[20,21],"quiz_category":{"id": "1"}}' http://127.0.0.1:5000/quizzes
```

_Responses:_

```
{"currentQuestion":{"answer":"Blood","category":1,"difficulty":4,"id":22,"question":"Hematology is a branch of medicine involving the study of what?","rating":3},"success":true}
```

### USER LOGIN

**`POST` /login**

Check user submitted data(user name, password) with the ones in the database by receiving a JSON body with the request and returns an object of two keys.

**Endpoint URL**

```
http://127.0.0.1:5000/login
```

**JSON body parameters**

| Name                          |  Type  | Description                                           |
| ----------------------------- | :----: | ----------------------------------------------------- |
| **`username`**_` (REQUIRED)`_ | String | The registered user name.                             |
| **`password`**_` (REQUIRED)`_ | String | The password associated with the submitted user name. |

**Response fields**

| Name                   |  Type   | Description                                                                                                       |
| ---------------------- | :-----: | ----------------------------------------------------------------------------------------------------------------- |
| **`success`**          | Boolean | The request process success condition.                                                                            |
| **`correct_password`** | Boolean | The submitted password matching process success condition , on True the user status converted from False to True. |

**Example**

_Request:_

```
curl -X POST -H "Content-Type:application/json" -d '{"username":"user1","password":"pass1"}' http://127.0.0.1:5000/login
```

_Responses:_

```
{
  "correct_password": true,
  "success": true
}
```

### ADD A NEW USER

**`POST` /register**

Adds a new user to the database by receiving a JSON body with the request and returns an object of two keys.

**Endpoint URL**

```
http://127.0.0.1:5000/register
```

**JSON body parameters**

| Name                          |  Type  | Description                                           |
| ----------------------------- | :----: | ----------------------------------------------------- |
| **`username`**_` (REQUIRED)`_ | String | The new user name.                                    |
| **`password`**_` (REQUIRED)`_ | String | The password associated with the submitted user name. |

**Response fields**

| Name          |  Type   | Description                               |
| ------------- | :-----: | ----------------------------------------- |
| **`success`** | Boolean | The request process success condition.    |
| **`created`** | Integer | The unique id number of the created user. |

**Example**

_Request:_

```
curl -X POST -H "Content-Type:application/json" -d '{"username":"user8","password":"pass8"}' http://127.0.0.1:5000/register
```

_Responses:_

```
{
  "created": 7,
  "success": true
}
```

### RESET USERS STATUS

**`POST` /status**

Resets all users status to False and Guest score to zero, returns an object of two keys.

**Endpoint URL**

```
http://127.0.0.1:5000/status
```

**Response fields**

| Name               |  Type   | Description                                 |
| ------------------ | :-----: | ------------------------------------------- |
| **`success`**      | Boolean | The request process success condition.      |
| **`status_reset`** | Boolean | The reset status process success condition. |

**Example**

_Request:_

```
curl -X POST http://127.0.0.1:5000/status
```

_Responses:_

```
{
  "status_reset": true,
  "success": true
}
```

### TRACKING ACTIVE USER SCORE

**`POST` /scores**

Calculate the user score, it receives a JSON body with the request and returns information about active user score in the form of an object of three keys.

**Endpoint URL**

```
http://127.0.0.1:5000/scores
```

**JSON body parameters**

| Name                                    |  Type   | Description                                                                                          |
| --------------------------------------- | :-----: | ---------------------------------------------------------------------------------------------------- |
| **`numCorrect`**_` (REQUIRED)`_         | integer | The number of correct answers during the current quiz after each question submission.                |
| **`previousNumCorrect`**_` (REQUIRED)`_ | integer | The number of previous correct answers during the current quiz for the previous question submission. |

**Response fields**

| Name                     |  Type   | Description                                                 |
| ------------------------ | :-----: | ----------------------------------------------------------- |
| **`success`**            | Boolean | The request process success condition.                      |
| **`currentScore`**       | Integer | The active user's score after last submission.              |
| **`previousNumCorrect`** | Integer | The numCorrect parameter submitted for the current request. |

**Example**

_Request:_

```
curl -X POST -H "Content-Type:application/json" -d '{"numCorrect":3,"previousNumCorrect":2}' http://127.0.0.1:5000/scores
```

_Responses:_

```
{
  "currentScore": 25,
  "previousNumCorrect": 3,
  "success": true
}
```

### ADD A NEW CATEGORY

**`POST` /categories**

Adds a new category to the database by receiving a JSON body with the request and returns an object of three keys.

**Endpoint URL**

```
http://127.0.0.1:5000/categories
```

**JSON body parameters**

| Name                             |  Type  | Description                                |
| -------------------------------- | :----: | ------------------------------------------ |
| **`newCategory`**_` (REQUIRED)`_ | string | The text body containing the new category. |

**Response fields**

| Name             |  Type   | Description                                                                                                                         |
| ---------------- | :-----: | ----------------------------------------------------------------------------------------------------------------------------------- |
| **`success`**    | Boolean | The request process success condition.                                                                                              |
| **`created`**    | Integer | The unique id number of the created category.                                                                                       |
| **`categories`** | Object  | A a dictionary of all available categories in which the keys are the ids and the value is the corresponding string of the category. |
| .                |

**Example**

_Request:_

```
curl -X POST -H "Content-Type:application/json" -d '{"newCategory":"Chemistry"}' http://127.0.0.1:5000/categories
```

_Responses:_

```
{
  "categories": {
    "1": "Science",
    "10": "Chemistry",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "created": 10,
  "success": true
}
```

### DELETE A QUESTION

**`DELETE` /questions/<question_id>**

Delete a certain question by its unique id from the data by receiving a JSON body with the request and returns an object of four keys.

**Endpoint URL**

```
http://127.0.0.1:5000/questions/<question_id>
```

**Path parameters**

| Name                             |  Type  | Description                                   |
| -------------------------------- | :----: | --------------------------------------------- |
| **`question_id`**_` (REQUIRED)`_ | String | The unique id for the question to be deleted. |

**JSON body parameters**

| Name                           | Type | Description                                                                 |
| ------------------------------ | :--: | --------------------------------------------------------------------------- |
| **`questions`**_` (REQUIRED)`_ | List | A list of question objects that are currently viewed in the user interface. |

**Response fields**

| Name                  |  Type   | Description                                                                                              |
| --------------------- | :-----: | -------------------------------------------------------------------------------------------------------- |
| **`success`**         | Boolean | The request process success condition.                                                                   |
| **`deleted`**         | Integer | The unique id number of the deleted question.                                                            |
| **`questions`**       |  List   | A list of question objects limited by ten objects that were viewed in the user interface after deletion. |
| **`total_questions`** | Integer | The total number of all available questions after deletion.                                              |

**Example**

_Request:_

```
curl -X DELETE -H "Content-Type:application/json" -d '{"questions":[ {"answer": "Muhammad Ali", "category": 4, "difficulty": 1, "id": 9,"question":"What boxer's original name is Cassius Clay?","rating": 2},{"answer": "Brazil", "category": 6, "difficulty": 3, "id": 10,"question":"Which is the only team to play in every soccer World Cup tournament?","rating": 3},{"answer": "Jimmy", "category": 1, "difficulty": 1, "id": 67,"question":"What's Your Name?","rating":1}]}' http://127.0.0.1:5000/questions/67
```

_Responses:_

```
{
    "deleted": 67,
    "questions": [
        {"answer": "Muhammad Ali", "category": 4, "difficulty": 1, "id": 9, "question": "What boxer's original name is Cassius Clay?", "rating": 2},
        {"answer": "Brazil", "category": 6, "difficulty": 3, "id": 10, "question": "Which is the only team to play in every soccer World Cup tournament?", "rating": 3}
    ],
    "success": true,
    "total_questions": 19
}
```

### CHANGE A QUESTION RATING

**`PATCH` /questions/<question_id>**

Change the rating of a certain question by its unique id from the data by receiving a JSON body with the request and returns an object of three keys.

**Endpoint URL**

```
http://127.0.0.1:5000/questions/<question_id>
```

**Path parameters**

| Name                             |  Type  | Description                                                  |
| -------------------------------- | :----: | ------------------------------------------------------------ |
| **`question_id`**_` (REQUIRED)`_ | String | The unique id for the question needing to change its rating. |

**JSON body parameters**

| Name                           |  Type   | Description                                                                 |
| ------------------------------ | :-----: | --------------------------------------------------------------------------- |
| **`rating`**_` (REQUIRED)`_    | Integer | An integer number representing the new rating for the desired question.     |
| **`questions`**_` (REQUIRED)`_ |  List   | A list of question objects that are currently viewed in the user interface. |

**Response fields**

| Name            |  Type   | Description                                                                                              |
| --------------- | :-----: | -------------------------------------------------------------------------------------------------------- |
| **`success`**   | Boolean | The request process success condition.                                                                   |
| **`updated`**   | Integer | The unique id number of the updated question.                                                            |
| **`questions`** |  List   | A list of question objects limited by ten objects that were viewed in the user interface after updating. |

**Example**

_Request:_

```
curl -X PATCH -H "Content-Type:application/json" -d '{"rating": 5,"questions":[ {"answer": "Muhammad Ali", "category": 4, "difficulty": 1, "id": 9,"question":"What boxer's original name is Cassius Clay?", "rating": 2},{"answer": "Brazil", "category": 6, "difficulty": 3, "id": 10,"question":"Which is the only team to play in every soccer World Cup tournament?","rating": 3}]}' http://127.0.0.1:5000/questions/9
```

_Responses:_

```
{
  "questions": [
    {
      "answer": "Muhammad Ali",
      "category": 4,
      "difficulty": 1,
      "id": 9,
      "question": "What boxer's original name is Cassius Clay?",
      "rating": 5
    },
    {
      "answer": "Brazil",
      "category": 6,
      "difficulty": 3,
      "id": 10,
      "question": "Which is the only team to play in every soccer World Cup tournament?",
      "rating": 3
    }
  ],
  "success": true,
  "updated": 9
}
```

## Testing

To run the tests, run

```

dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py

```
