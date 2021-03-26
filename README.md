Casting Agency
-----

## Introduction

This is the final project for the [NANODEGREE PROGRAM Full Stack Web Developer](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd0044) from Udacity. 

## Casting Agency Specifications

The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. You are an Executive Producer within the company and are creating a system to simplify and streamline your process.

* Models:

  * Movies with attributes title and release date
  * Actors with attributes name, age and gender

* Roles:
 * Casting Assistant
    * Can view actors and movies `(get:actors)(get:movies)`

  * Casting Director
    * All permissions a Casting Assistant has and…
    * Add or delete an actor from the database `(post:actors)(delete:actors)`
    * Modify actors or movies `(patch:actors)(patch:movies)`

  * Executive Producer
    * All permissions a Casting Director has and…
    * Add or delete a movie from the database `(post:movies)(delete:movies)`

## Login credentials (for the different roles mentioned above)
Hosted App on Heroku

Please access the app from this link: https://sansergi-casting-agency.herokuapp.com/login

### Login credentials (for the different roles mentioned above)
Tokens are done from authentication via Auth0, please use the following credentials:

User: `casting_assistant@agency.com`
Password: `Casting123456!`

User: `casting_director@agency.com`
Password: `Casting123456!`

User: `executive_producer@agency.com` 
Password: `Casting123456!`


## Tech Stack 

### Dependencies for running locally

Our tech stack will include the following:
 * **SQLAlchemy ORM** to be our ORM library of choice
 * **PostgreSQL** as our database of choice
 * **Python3** and **Flask** as our server language and server framework
 * **Flask-Migrate** for creating and running schema migrations
 * **Bootstrap 3** for our frontend

You can download and install the dependencies mentioned above using `pip` as:
```
pip install requirements.txt

```
Then set up environment variables as follow:

```
source setup.sh
```

Finally create the local Postgresql database:

```
$ python3 manage.py db init
$ python3 manage.py db migrate

```
### Run the server

To run the server, execute:
```
python3 app.py

```
All set ups are already done from the setup.sh file. 

### Run tests

```
$ python3 casting_test.py
```

## Error handling
The following error codes are handle within the app:

* 400: Bad request
* 401: Unauthorized
* 404: Resource not found
* 422: Unprocessable
* AuthError: Corresponding Auth0 error status code and description

## Endpoints
Please rememenber to logging in with approved credentials in order to generate a JWT (JSON Web Token) that will grant the user access based on their role's permissions.

Casting Agency app includes the following API endpoints. Below is an overview of their expected behavior:

### GET /movies
Returns a list of all the movies in the database
Example: `curl -X GET -H "Authorization: Bearer ***replace this with your token***" http://0.0.0.0:8080/movies`

### GET /actors
Returns a list of all the actors in the database
Example: `curl -X GET -H "Authorization: Bearer ***replace this with your token***" http://0.0.0.0:8080/actors`

### GET /movies/{movie_id}
Returns details about the specific movie listed in the database
Example: `curl -X GET -H "Authorization: Bearer ***replace this with your token***" http://0.0.0.0:8080/movies/1`

### GET /actors/{actor_id}
Returns details about the specific actor listed in the database
Example: `curl -X GET -H "Authorization: Bearer ***replace this with your token***" http://0.0.0.0:8080/actors/1`

### GET /movies/create
Returns the form to create a new movie
Roles authorized: executive producer
Example: `curl -X GET -H "Authorization: Bearer ***replace this with your token***" http://0.0.0.0:8080/movies/create`

### POST /movies/create
Adds a new movie project to the database, including the movie's title, image link and release date 
Roles authorized: executive producer
Example: `curl -X POST -H "Authorization: Bearer ***replace this with your token***" -H "Content-Type: application/json" -d '{ "title": "TEST MOVIE", "release_date":"10/10/2000", "image_link":"http://test.com"}' http://0.0.0.0:8080/movies/create`

### GET /actors/create
Returns the form to list an actor
Roles authorized: casting director and executive producer
Example: `curl -X GET -H "Authorization: Bearer ***replace this with your token***" http://0.0.0.0:8080/actors/create`

### POST /actors/create
Adds a new actor to the database, including name, gender, age, picture link and movie id where he/she acts
Roles authorized: executive producer
Example: `curl -X POST -H "Authorization: Bearer ***replace this with your token***" -H "Content-Type: application/json" -d '{ "name": "TEST ACTOR", "age":"20", "picture_link":"http://test.com", "gender":"male", "movie_id":"1"}' http://0.0.0.0:8080/movies/create`

### GET /movies/edit/{movie_id}
Returns the form to update a movie
Roles authorized: executive producer
Example: `curl -X POST -H "Authorization: Bearer ***replace this with your token***" http://0.0.0.0:8080/movies/edit/1`

### POST /movies/edit/{movie_id}/
Updates an existing movie
Roles authorized: executive producer
Example: `curl -X POST -H "Authorization: Bearer ***replace this with your token***" -H "Content-Type: application/json" -d ''{ "title": "TEST MOVIE", "release_date":"10/10/2000", "image_link":"http://test.com"}' http://0.0.0.0:8080/movies/edit/1`

### GET /movies/delete/{movie_id}
Deletes a movie from the database
Roles authorized: executive producer
Example: `curl X GET -H "Authorization: Bearer ***replace this with your token***" https://0.0.0.0:8080/movies/delete/1`

### GET /actors/edit/{actor_id}
Returns the form to update an actor
Roles authorized: casting director and executive producer
Example: `curl -X POST -H "Authorization: Bearer ***replace this with your token***" http://0.0.0.0:8080/actors/edit/1`

### POST /actors/edit/{actor_id}/
Updates an existing actor
Roles authorized: casting director and executive producer
Example: `curl -X POST -H "Authorization: Bearer ***replace this with your token***" -H "Content-Type: application/json" -d '{ "name": "TEST ACTOR", "age":"20", "picture_link":"http://test.com", "gender":"male", "movie_id":"1"}' http://0.0.0.0:8080/movies/edit/1`

### GET /actors/delete/{actor_id}
Deletes an actor from the database
Roles authorized: casting director and executive producer
Example: `curl X GET -H "Authorization: Bearer ***replace this with your token***" https://0.0.0.0:8080/actors/delete/1`

## Motivation for project

This is a great closure for me, personally it was a great learning journey, where the support from Udacity community and mentors was great. The overall team was very informative and the lessons made me grow professionaly, with knowledge I am planning to implement in the near future. 

Really looking forward to continue learning and become better at this passion I have: programing!!! :nerd_face:





