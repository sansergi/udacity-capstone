Casting Agency
-----

## Introduction

This is the final project for the [NANODEGREE PROGRAM Full Stack Web Developer] (https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd0044) from Udacity. 

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

### GET /login
Redirects the user to the Auth0 login page, where the user can log in or sign up
Roles authorized: all users
Example: `curl https://0.0.0.0:8080/login`

### GET /post-login
Handles the response from the access token endpoint and stores the user's information in a Flask session
Roles authorized: casting assistant, executive producer
Example: `curl https://0.0.0.0:8080/post-login`

### GET /logout
Clears the user's session and logs them out
Roles authorized: all users
Example: `curl https://0.0.0.0:8080/logout`

### GET /movies
Returns a list of all the movie projects in the database
Roles authorized: casting assistant, executive producer
Example: `curl https://0.0.0.0:8080/movies`

### GET /actors
Returns a list of all the actors in the database
Roles authorized: casting assistant, executive producer
Example: `curl https://0.0.0.0:8080/actors`

### GET /movies/{movie_id}
Returns details about each individual movie project listed in the database
Roles authorized: casting assistant, executive producer
Example: curl `https://0.0.0.0:8080/movies/1`

### GET /actors/{actor_id}
Returns details about each individual actor listed in the database
Roles authorized: casting assistant, executive producer
Example: `curl https://0.0.0.0:8080/actors/1`

### GET /movies/create
Returns the form to list a movie project
Roles authorized: executive producer
Example: `curl https://0.0.0.0:8080/movies/create`

### GET /actors/create
Returns the form to list an actor profile
Roles authorized: executive producer
Example: `curl https://0.0.0.0:8080/actors/create`

### POST /movies/create
Adds a new movie project to the database, including the movie's name, genre, release year, and rating
Roles authorized: executive producer
Example: `curl https://0.0.0.0:8080/movies/create -X POST -H "Content-Type: application/json" -d '{ "name": "A Star is Born 2", "director": "Bradley Cooper", "genre": "Musical", "release_year": 2023, "rating": "R"}'`

### POST /actors/create
Adds a new actor profile to the database, including the actor's name, age, gender, and profile image
Roles authorized: executive producer
Example: `curl https://0.0.0.0:8080/actors -X POST -H "Content-Type: application/json" -d '{ "name": "Ana de Armas", "age": 32, "gender": "Female", "image_link": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Ana_de_Armas_by_Gage_Skidmore.jpg/220px-Ana_de_Armas_by_Gage_Skidmore.jpg"}'`

### GET /movies/{movie_id}/patch
Returns the form to update a movie project
Roles authorized: executive producer
Example: `curl https://0.0.0.0:8080/movies/1/patch`

### GET /actors/{actor_id}/patch
Returns the form to update an actor profile
Roles authorized: executive producer
Example: `curl https://0.0.0.0:8080/actors/1/patch`

### GET /movies/{movie_id}/patch
Updates an existing movie project, with revised details related to the movie's name, genre, release year, or rating
Roles authorized: executive producer
Example: `curl https://0.0.0.0:8080/movies/1 -X POST -H "Content-Type: application/json" -d '{ "name": "A Star is Born 2", "director": "Lady Gaga", "genre": "Comedy", "release_year": 2024, "rating": "R"}'`

### GET /actors/{actor_id}/patch
Updates an existing actor profile, with revised details related to the actor's name, age, gender, or profile image
Roles authorized: executive producer
Example: `curl https://0.0.0.0:8080/actors/1 -X POST -H "Content-Type: application/json" -d '{ "name": "Ana de Armas", "age": 32, "gender": "Female" , "image_link": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/62/Ana_de_Armas_GQ_2018_2.png/165px-Ana_de_Armas_GQ_2018_2.png"}'`

### GET /movies/{movie_id}/delete
Deletes a movie project from the database
Roles authorized: executive producer
Example: `curl https://0.0.0.0:8080/movies/1/delete`

### GET /actors/{actor_id}/delete
Deletes an actor profile from the database
Roles authorized: executive producer
Example: `curl https://0.0.0.0:8080/actors/1/delete`

### GET /cast/create
Returns the form to cast an actor for a movie project
Roles authorized: executive producer
Example: `curl https://0.0.0.0:8080/cast/create`

### POST /cast/create
Casts an actor for an upcoming movie project by appending the actor to the movie's cast in the database
Roles authorized: executive producer
Example: `curl https://0.0.0.0:8080/cast/create -X POST -H "Content-Type: application/json" -d '{ "name": "The Pink Panther 2", "director": "Nancy Meyers", "genre": "Action", "release_year": 2022, "rating": "G", "cast": "Ana de Armas"}'`



