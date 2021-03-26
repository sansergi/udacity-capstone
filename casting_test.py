import json
import unittest
import os
from flask.globals import session
from flask.json import jsonify
from flask_sqlalchemy import SQLAlchemy
from models import *
from app import app, create_app

class CastingAgencyTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.database_host = os.environ.get("DB_HOST_TEST")
        self.database_user = os.environ.get("DB_USER_TEST")
        self.database_password = os.environ.get("DB_PASSWORD_TEST")
        self.database_name = os.environ.get("DB_NAME_TEST")
        self.database_path =\
            "postgresql://{}:{}@{}/{}".\
            format(
                self.database_user,
                self.database_password,
                self.database_host,
                self.database_name)
        setup_db(self.app, self.database_path)

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.create_all()

        self.casting_assistant_token = os.environ.get('casting_assistant_token')
        self.casting_director_token = os.environ.get('casting_director_token')
        self.executive_producer_token = os.environ.get('executive_producer_token')
        self.casting_assistant_header = {"Authorization": "Bearer {}".
                                         format(self.casting_assistant_token)}
        self.casting_director_header = {"Authorization": "Bearer {}".
                                        format(self.casting_director_token)}
        self.executive_producer_header = {"Authorization": "Bearer {}".
                                          format(self.executive_producer_token)}

    def tearDown(self):

        pass

    def test_get_all_movies(self):
        res = self.client.get('/movies', 
                              headers=self.casting_assistant_header)
        self.assertEqual(res.status_code, 200)
    
    def test_get_movie_error(self):
        res = self.client.get('/movies/22', 
                              headers=self.casting_assistant_header)
        self.assertEqual(res.status_code, 404)

    def test_edit_movie_error(self):
        res = self.client.post('/movies/edit/11', 
                               headers=self.casting_assistant_header)
        self.assertEqual(res.status_code, 401)

    def test_add_new_movie(self):
        res = self.client.post('/movies/create',
                                    data=dict(title="test",
                                              release_date="3/19/2021",
                                              image_link="https://test"),
                                    headers=self.casting_assistant_header)
        self.assertEqual(res.status_code, 401)

    def test_get_all_actors(self):
        res = self.client.get('/actors', 
                              headers=self.casting_assistant_header)
        self.assertEqual(res.status_code, 200)

    def test_get_actor_error(self):
        res = self.client.get('/actors/22', 
                              headers=self.casting_assistant_header)
        self.assertEqual(res.status_code, 404)

    def test_edit_actor_error(self):
        res = self.client.post('/actors/edit/11', 
                               headers=self.casting_assistant_header)
        self.assertEqual(res.status_code, 401)

    def test_add_new_actor(self):
        response = self.client.post('/actors/create',
                                    data=dict(name="test",
                                              age=0,
                                              picture_link="https://test",
                                              gender="male"),
                                    headers=self.casting_assistant_header
                                    )
        self.assertEqual(response.status_code, 401)

if __name__ == "__main__":
    unittest.main()
