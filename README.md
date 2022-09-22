# INU-API

-----

### Introduction

INU-API is a Dog management system site which illustrates a company that is in the business of matching users to dogs in for Dog duty.
INU-API gives one ease of seeing users and dogs managed by the company.


### Tech Stack

Our tech stack will include:

* **SQLAlchemy ORM** to be our ORM library of choice
* **PostgreSQL** as our database of choice
* **Python3** and **Flask** as our server language and server framework
* **Flask-Migrate** for creating and running schema migrations

### Main Files: Project Structure


Overall:
* Models are located in `models.py`.
* Controllers are located in `controllers.py`.


### Development Setup
## Backend


First, [install Flask](http://flask.pocoo.org/docs/1.0/installation/#install-flask) if you haven't already.

  ```
  $ cd ~
  $ sudo pip3 install Flask
  ```

To start and run the local development server,

1. Initialize and activate a virtualenv:
  ```
  $ cd YOUR_PROJECT_DIRECTORY_PATH/
  $ virtualenv --no-site-packages env
  $ source env/bin/activate
  ```

2. Install the dependencies:
  ```
  $ pip install -r requirements.txt
  ```

3. Run the development server:
  ```
  $ export FLASK_APP=api
  $ flask run
  ```

4. Run tests
  ```
  $ pytest
  ```

5. Navigate to Home page [http://localhost:5000](http://localhost:5000)

6. Active endpoints

    | Functionality            | Endpoint                             |  
    | ------------------------ | -----------------------------        | 
    | Fetches a list of users  | GET /users                           | :heavy_check_mark: | 
    | Fetches a list of dogs   | GET /dogs                            | :heavy_check_mark: |   
    | Creates a user           | POST /users                          | :heavy_check_mark: |   
    | Creates a dog            | POST /dogs                           | :heavy_check_mark: |  
    | Filters user list by query params city, firstname, lastname |GET /users/filter' |:heavy_check_mark: |  




7. Live project

    - The backend has been deployed to heroku platform [Hosted API](https://inu-backend.herokuapp.com/api/v1/users)

8. API Documentation
    - [![Run in Postman](https://run.pstmn.io/button.svg)](https://documenter.getpostman.com/view/4755480/2s7ZE8nMpb)
    Run the above collection to test out with appropriate response data for each endpoint
