from flask import (Flask, request, abort, jsonify, render_template,
                   session, flash, abort, url_for, redirect)
from flask_cors import CORS, cross_origin
from models import setup_db, Movie, Actor, db
from auth import AuthError, requires_auth
from forms import *
import os
from authlib.integrations.flask_client import OAuth
from config import SECRET_KEY
import json


AUTH0_CALLBACK_URL = os.getenv('AUTH0_CALLBACK_URL')
AUTH0_CLIENT_ID = os.getenv('AUTH0_CLIENT_ID')
AUTH0_CLIENT_SECRET = os.getenv('AUTH0_CLIENT_SECRET')
AUTH0_DOMAIN = os.getenv('AUTH0_DOMAIN')
AUTH0_BASE_URL = 'https://' + AUTH0_DOMAIN
AUTH0_AUDIENCE = os.getenv('AUTH0_AUDIENCE')


def create_app(test_config=None):
    app = Flask(__name__)
    app.config['SECRET_KEY'] = SECRET_KEY
    setup_db(app)
    CORS(app)

    oauth = OAuth(app)
    auth0 = oauth.register(
            'auth0',
            client_id=AUTH0_CLIENT_ID,
            client_secret=AUTH0_CLIENT_SECRET,
            api_base_url=AUTH0_BASE_URL,
            access_token_url='https://dev-1aweba2i.us.auth0.com' + '/oauth/token',
            authorize_url='https://dev-1aweba2i.us.auth0.com' + '/authorize',
            client_kwargs={
                'scope': 'openid profile email'
                    }
        )


    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                            'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods',
                            'GET,PATCH,POST,DELETE,OPTIONS')
        return response


    @app.route('/login', methods=['GET'])
    @cross_origin()
    def login():
        return auth0.authorize_redirect(
            redirect_uri=AUTH0_CALLBACK_URL,
            audience=AUTH0_AUDIENCE
        )


    @app.route('/logout')
    def log_out():
        session.clear()
        params = {'returnTo': url_for('index', _external=True),
                'client_id': AUTH0_CLIENT_ID}
        return redirect(AUTH0_BASE_URL + '/v2/logout?')


    @app.route('/post-login', methods=['GET'])
    @cross_origin()
    def post_login():
        token = auth0.authorize_access_token()
        session['token'] = token['access_token']
        return render_template('pages/home.html')


    @app.route('/home')
    def index():
        return render_template('pages/home.html')


    @app.route('/movies', methods=['GET'])
    @requires_auth('get:movies')
    def get_movies(payload):
        movies = Movie.query.all()
        movies = [movie.format() for movie in movies]
        if movies is None:
            return json.dumps({
			'success': False,
			'error': 'Resource not found'
		    }), 404
        return render_template('pages/movies.html',
                            data=movies, roles=payload["permissions"],
                            status_code=200)


    @app.route('/movies/<int:movie_id>', methods=['GET'])
    @requires_auth('get:movies')
    def get_movies_by_id(payload, movie_id):
        movie = Movie.query.get(movie_id)
        if movie is None:
            return json.dumps({
			'success': False,
			'error': 'Resource not found'
		    }), 404
        movie = [movie.format()]
        query_actors = Actor.query.filter_by(movie_id=movie_id).all()
        return render_template('pages/show_movie.html', data=movie,
                            actor_data=query_actors,
                            roles=payload["permissions"])


    @app.route('/actors', methods=['GET'])
    @requires_auth('get:actors')
    def get_actors(payload):
        actors = Actor.query.all()
        actors = [actor.format() for actor in actors]
        if actors is None:
            return json.dumps({
			'success': False,
			'error': 'Resource not found'
		    }), 404
        return render_template('pages/actors.html',
                            data=actors, roles=payload["permissions"],
                            status_code=200)


    @app.route('/actors/<int:actor_id>', methods=['GET'])
    @requires_auth('get:actors')
    def get_actors_by_id(payload, actor_id):
        actor = Actor.query.get(actor_id)
        if actor is None:
            return json.dumps({
			'success': False,
			'error': 'Resource not found'
		    }), 404
        actor = [actor.format()]
        return render_template('pages/show_actor.html',
                            roles=payload["permissions"], data=actor)


    @app.route('/actors/edit/<int:actor_id>', methods=['GET'])
    @requires_auth('get:actors')
    def edit_actor_get(payload, actor_id):
        form = ActorForm()
        actor = Actor.query.get(actor_id)
        if actor is None:
            return json.dumps({
			'success': False,
			'error': 'Resource not found'
		    }), 404
        actor = [actor.format()]
        return render_template('forms/edit_actor.html',
                            roles=payload["permissions"], form=form, data=actor)


    @app.route('/actors/edit/<int:actor_id>', methods=['POST'])
    @requires_auth('patch:actors')
    def edit_actor_post(payload, actor_id):
        error = False
        actor = Actor.query.get(actor_id)
        if actor is None:
            return json.dumps({
			'success': False,
			'error': 'Resource not found'
		    }), 404
        try:
            actor.name = request.form['name']
            actor.gender = request.form['gender']
            actor.age = request.form['age']
            actor.movie_id = request.form['movie_id']
            actor.picture_link = request.form['picture_link']
            db.session.commit()
        except Exception as ex:
            db.session.rollback()
            error = True
        finally:
            db.session.close()
        if error:
            flash('An error occurred. Actor ' + request.form['name'] +
                ' could not be updated.')
        else:
            flash('Actor ' + request.form['name'] +
                ' was successfully updated!')
        return redirect(url_for('get_actors',
                                roles=payload["permissions"], actor_id=actor_id))


    @app.route('/movies/edit/<int:movie_id>', methods=['GET'])
    @requires_auth('get:movies')
    def edit_movie_get(payload, movie_id):
        form = MovieForm()
        movie = Movie.query.get(movie_id)
        if movie is None:
            return json.dumps({
			'success': False,
			'error': 'Resource not found'
		    }), 404
        movie = [movie.format()]
        return render_template('forms/edit_movie.html',
                            roles=payload["permissions"], form=form, data=movie)


    @app.route('/movies/edit/<int:movie_id>', methods=['POST'])
    @requires_auth('patch:movies')
    def edit_movie_post(payload, movie_id):
        error = False
        movie = Movie.query.get(movie_id)
        if movie is None:
            return json.dumps({
			'success': False,
			'error': 'Resource not found'
		    }), 404
        try:
            movie.title = request.form['title']
            movie.release_date = request.form['release_date']
            movie.image_link = request.form['image_link']
            db.session.commit()
        except Exception as ex:
            db.session.rollback()
            error = True
        finally:
            db.session.close()
        if error:
            flash('An error occurred. Movie ' + request.form['title'] +
                ' could not be updated.')
        else:
            flash('Movie ' + request.form['title'] +
                ' was successfully updated!')
        return redirect(url_for('get_movies',
                        roles=payload["permissions"], movie_id=movie_id))


    @app.route('/movies/create', methods=['GET'])
    @requires_auth('post:movies')
    def create_movie_get(payload):
        form = MovieForm()
        return render_template('forms/new_movie.html',
                            roles=payload["permissions"], form=form)


    @app.route('/movies/create', methods=['POST'])
    @requires_auth('post:movies')
    def create_movie_post(payload):
        error = False
        try:
            movie = Movie(title=request.form.get('title'),
                        image_link=request.form.get('image_link'),
                        release_date=request.form.get('release_date'))
            db.session.add(movie)
            db.session.commit()
        except Exception as ex:
            db.session.rollback()
            error = True
        finally:
            db.session.close()
        if error:
            flash('An error occurred. Movie ' + request.form['title'] +
                ' could not be listed.')
        else:
            flash('Movie ' + request.form['title'] +
                ' was successfully listed!')
        return render_template('pages/home.html', roles=payload["permissions"])


    @app.route('/actors/create', methods=['GET'])
    @requires_auth('post:actors')
    def create_actor_get(payload):
        form = ActorForm()
        return render_template('forms/new_actor.html',
                            form=form, roles=payload["permissions"])


    @app.route('/actors/create', methods=['POST'])
    @requires_auth('post:actors')
    def create_actor_post(payload):
        error = False
        try:
            actor = Actor(name=request.form.get('name'),
                        age=request.form.get('age'),
                        gender=request.form.get('gender'),
                        picture_link=request.form.get('picture_link'),
                        movie_id=request.form.get('movie_id'))
            db.session.add(actor)
            db.session.commit()
        except Exception as ex:
            db.session.rollback()
            error = True
        finally:
            db.session.close()
        if error:
            flash('An error occurred. Actor ' + request.form['name'] +
                ' could not be listed.')
        else:
            flash('Actor ' + request.form['name'] +
                ' was successfully listed!')
        return render_template('pages/home.html', roles=payload["permissions"])


    @app.route('/movies/delete/<int:movie_id>')
    @requires_auth('delete:movies')
    def delete_movie(payload, movie_id):
        error = False
        movie = Movie.query.filter(Movie.id == movie_id)
        if movie is None:
            return json.dumps({
			'success': False,
			'error': 'Resource not found'
		    }), 404
        try:
            Movie.query.filter(Movie.id == movie_id).delete()
            db.session.commit()
            db.session.close()
        except Exception as ex:
            db.session.rollback()
            error = True
        finally:
            db.session.close()
        if error:
            flash('An error occurred. Movie ' + request.form['title'] +
                ' could not be deleted.')
        else:
            flash('Movie deleted')
        return render_template('pages/home.html', roles=payload["permissions"])


    @app.route('/actors/delete/<int:actor_id>')
    @requires_auth('delete:actors')
    def delete_actor(payload, actor_id):
        error = False
        actor = Actor.query.filter(Actor.id == actor_id)
        if actor is None:
            return json.dumps({
			'success': False,
			'error': 'Resource not found'
		    }), 404
        try:
            Actor.query.filter(Actor.id == actor_id).delete()
            db.session.commit()
            db.session.close()
        except Exception as ex:
            db.session.rollback()
            error = True
        finally:
            db.session.close()
        if error:
            flash('An error occurred. Actor ' + request.form['name'] +
                ' could not be deleted.')
        else:
            flash('Actor deleted')
        return render_template('pages/home.html', roles=payload["permissions"])


    @app.errorhandler(401)
    def unauthorized(error):
        return jsonify({
            "success": False,
            "error": 401,
            "message": "Unauthorized"
            }), 401


    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "Task Unprocessable"
            }), 422


    @app.errorhandler(404)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "Resource not found"
            }), 404


    @app.errorhandler(AuthError)
    def auth_error(error):
        return jsonify({
            "success": False,
            "error": error.status_code,
            "message": error.error['description']
            }), error.status_code
    
    return app

app = create_app()

if __name__ == '__main__':
    # app.run()
    app.run(host="127.0.0.1", port=8000, debug=True)
