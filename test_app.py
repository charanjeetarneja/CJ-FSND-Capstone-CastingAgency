from ast import Pass
from datetime import datetime
import os
import json
os.environ["env"]="test"
import unittest
from app import create_app
from models import DATABASE_URI
from flask_sqlalchemy import SQLAlchemy
from models import db,setup_db, Movie, Actor, create_tables_for_test

ASSISTANT_TOKEN = os.getenv('ASSISTANT_TOKEN')
DIRECTOR_TOKEN = os.getenv('DIRECTOR_TOKEN')
PRODUCER_TOKEN = os.getenv('PRODUCER_TOKEN')

class ActorsTestCase(unittest.TestCase):
    "This class include testcases for actors API endpoints (without RBAC)"
    
    def setUp(self):
        self.assistant = ASSISTANT_TOKEN
        self.director = DIRECTOR_TOKEN
        self.producer = PRODUCER_TOKEN
        self.app=create_app()
        self.client = self.app.test_client()
        setup_db(self.app)
        with self.app.app_context():
            create_tables_for_test()
    
    def tearDown(self):
        #"not relevant in our case"
        db.session.close()
        Pass

    def test_get_actors_negative(self):
        response=self.client.get("/actors",headers={
                                     "Authorization": "Bearer {}"
                                     .format(self.producer)
                                 })
        r_data=json.loads(response.data)
        self.assertFalse(r_data['success'],"success attribute in response json was True")
        self.assertEqual(int(r_data['error']),404,"error code is not 404")


    def test_post_an_actor(self):
        t_actor = {"name":"CJ", "age":36,"gender":"male"}
        response=self.client.post("/actors",headers={
                                     "Authorization": "Bearer {}"
                                     .format(self.producer)
                                 },json=t_actor)
        r_data=json.loads(response.data)
        self.assertTrue(r_data['success'],"success attribute in response json was false")
        i_actor=Actor.query.get(r_data['actors']['id'])
        t_actor["id"]=r_data['actors']['id']
        self.assertEqual(i_actor.serialized_actor(),t_actor,"Actor in test case and the actor posted in DB are not same")

    def test_get_actors_postitive(self):
        t_actor = {"name":"CJ", "age":35,"gender":"male"}
        response=self.client.post("/actors",headers={
                                     "Authorization": "Bearer {}"
                                     .format(self.producer)
                                 },json=t_actor)
        response=self.client.get("/actors",headers={
                                     "Authorization": "Bearer {}"
                                     .format(self.producer)
                                 })
        r_data=json.loads(response.data)
        self.assertTrue(r_data['success'],"success attribute in response json was false")
        self.assertGreaterEqual(len(r_data['actors']),1,"actors are not getting returned")        

    def test_post_an_actor_negative(self):
        t_actor = {"age":35,"gender":"male"}
        response=self.client.post("/actors",headers={
                                     "Authorization": "Bearer {}"
                                     .format(self.producer)
                                 },json=t_actor)
        r_data=json.loads(response.data)
        self.assertFalse(r_data['success'],"success attribute in response json was false")
        self.assertEqual(int(r_data['error']),400,"error code is not 400")

    def test_patch_an_actor(self):
        t_actor = {"name":"CJ", "age":36,"gender":"male"}
        response=self.client.post("/actors",headers={
                                     "Authorization": "Bearer {}"
                                     .format(self.producer)
                                 },json=t_actor)
        id=json.loads(response.data)['actors']['id']
        t_actor_upd = {"name":"Charanjeet"}
        response_upd=self.client.patch(f'/actors/{id}',json=t_actor_upd,headers={
                                     "Authorization": "Bearer {}"
                                     .format(self.producer)
                                 })
        r_data=json.loads(response_upd.data)
        self.assertTrue(r_data['success'],"success attribute in response json was false")
        t_actor["name"]=t_actor_upd['name']
        t_actor["id"]=id
        self.assertEqual(r_data["actor"],t_actor,"Actor in test case and the actor posted in DB are not same")
        
    def test_patch_an_actor_negative(self):
        id=99999
        t_actor_upd = {"name":"Charanjeet"}
        response_upd=self.client.patch(f'/actors/{id}',json=t_actor_upd,headers={
                                     "Authorization": "Bearer {}"
                                     .format(self.producer)
                                 })
        r_data=json.loads(response_upd.data)
        self.assertFalse(r_data['success'],"success attribute in response json was true")
        self.assertEqual(int(r_data['error']),404,"error code is not 404")

    def test_delete_an_actor(self):
        t_actor = {"name":"CJ", "age":36,"gender":"male"}
        response=self.client.post("/actors",json=t_actor,headers={
                                     "Authorization": "Bearer {}"
                                     .format(self.producer)
                                 })
        id=json.loads(response.data)['actors']['id']
        response_upd=self.client.delete(f'/actors/{id}',headers={
                                     "Authorization": "Bearer {}"
                                     .format(self.producer)
                                 })
        r_data=json.loads(response_upd.data)
        self.assertTrue(r_data['success'],"success attribute in response json was false")
        self.assertEqual(r_data['id'],id,"Actor inserted hasn't been deleted")
    
    def test_delete_an_actor_negative(self):
        id=999999
        response_upd=self.client.delete(f'/actors/{id}',headers={
                                     "Authorization": "Bearer {}"
                                     .format(self.producer)
                                 })
        r_data=json.loads(response_upd.data)
        self.assertFalse(r_data['success'],"success attribute in response json was true")
        self.assertEqual(int(r_data['error']),404,"error code is not 404")


class MoviesTestCase(unittest.TestCase):
    "This class include testcases for movies API endpoints (without RBAC)"
    def setUp(self):
        self.assistant = ASSISTANT_TOKEN
        self.director = DIRECTOR_TOKEN
        self.producer = PRODUCER_TOKEN
        self.app=create_app()
        self.client = self.app.test_client()
        setup_db(self.app)
        with self.app.app_context():
            create_tables_for_test()
    
    def tearDown(self):
        #"not relevant in our case"
        db.session.close()
        Pass

    def test_get_movies_negative(self):
        response=self.client.get("/movies",headers={
                                     "Authorization": "Bearer {}"
                                     .format(self.producer)
                                 })
        r_data=json.loads(response.data)
        self.assertFalse(r_data['success'],"success attribute in response json was True")
        self.assertEqual(int(r_data['error']),404,"error code is not 404")

    def test_post_a_movies(self):
        t_movie = {"title":"Sully", "release_date":"2022-12-22"}
        response=self.client.post("/movies",json=t_movie,headers={
                                     "Authorization": "Bearer {}"
                                     .format(self.producer)
                                 })
        r_data=json.loads(response.data)
        self.assertTrue(r_data['success'],"success attribute in response json was false")
        i_movie=Movie.query.get(r_data['movies']['id'])
        t_movie["id"]=r_data['movies']['id']
        #t_movie["release_date"]=datetime.date.fromisoformat(t_movie["release_date"])
        self.assertEqual(i_movie.serialized_movie(),t_movie,"Movie in test case and the movie posted in DB are not same")

    def test_get_movies_postitive(self):
        t_movie  = {"title":"Sully", "release_date":"2022-12-22"}
        response=self.client.post("/movies",json=t_movie,headers={
                                     "Authorization": "Bearer {}"
                                     .format(self.producer)
                                 })
        response=self.client.get("/movies",headers={
                                     "Authorization": "Bearer {}"
                                     .format(self.producer)
                                 })
        r_data=json.loads(response.data)
        self.assertTrue(r_data['success'],"success attribute in response json was false")
        self.assertGreaterEqual(len(r_data['movies']),1,"movies are not getting returned")        

    def test_post_a_movie_negative(self):
        t_movie  = {"title":"Sully"}
        response=self.client.post("/movies",json=t_movie,headers={
                                     "Authorization": "Bearer {}"
                                     .format(self.producer)
                                 })
        r_data=json.loads(response.data)
        self.assertFalse(r_data['success'],"success attribute in response json was false")
        self.assertEqual(int(r_data['error']),400,"error code is not 400")

    def test_patch_a_movie(self):
        t_movie  = {"title":"Sully", "release_date":"2022-12-22"}
        response=self.client.post("/movies",json=t_movie,headers={
                                     "Authorization": "Bearer {}"
                                     .format(self.producer)
                                 })
        id=json.loads(response.data)['movies']['id']
        t_movie_upd = {"title":"Terminal"}
        response_upd=self.client.patch(f'/movies/{id}',json=t_movie_upd,headers={
                                     "Authorization": "Bearer {}"
                                     .format(self.producer)
                                 })
        r_data=json.loads(response_upd.data)
        self.assertTrue(r_data['success'],"success attribute in response json was false")
        t_movie["title"]=t_movie_upd["title"]
        t_movie["id"]=id
        self.assertEqual(r_data["movie"],t_movie,"Movie in test case and the movie posted in DB are not same")
        
    def test_patch_a_movie_negative(self):
        id=99999
        t_movie_upd = {"title":"Terminal"}
        response_upd=self.client.patch(f'/movies/{id}',json=t_movie_upd,headers={
                                     "Authorization": "Bearer {}"
                                     .format(self.producer)
                                 })
        r_data=json.loads(response_upd.data)
        self.assertFalse(r_data['success'],"success attribute in response json was true")
        self.assertEqual(int(r_data['error']),404,"error code is not 404")

    def test_delete_a_movie(self):
        t_movie  = {"title":"Sully", "release_date":"2022-12-22"}
        response=self.client.post("/movies",json=t_movie,headers={
                                     "Authorization": "Bearer {}"
                                     .format(self.producer)
                                 })
        id=json.loads(response.data)['movies']['id']
        response_upd=self.client.delete(f'/movies/{id}',headers={
                                     "Authorization": "Bearer {}"
                                     .format(self.producer)
                                 })
        r_data=json.loads(response_upd.data)
        self.assertTrue(r_data['success'],"success attribute in response json was false")
        self.assertEqual(r_data['id'],id,"Movie inserted hasn't been deleted")
    
    def test_delete_a_movie_negative(self):
        id=999999
        response_upd=self.client.delete(f'/movies/{id}',headers={
                                     "Authorization": "Bearer {}"
                                     .format(self.producer)
                                 })
        r_data=json.loads(response_upd.data)
        self.assertFalse(r_data['success'],"success attribute in response json was true")
        self.assertEqual(int(r_data['error']),404,"error code is not 404")

class AuthTestCase(unittest.TestCase):
    "This class include testcases auth roles"
    def setUp(self):
        self.assistant = ASSISTANT_TOKEN
        self.director = DIRECTOR_TOKEN
        self.producer = PRODUCER_TOKEN
        self.app=create_app()
        self.client = self.app.test_client()
        setup_db(self.app)
        with self.app.app_context():
            create_tables_for_test()
    
    def tearDown(self):
        #"not relevant in our case"
        db.session.close()
        Pass

    def test_post_a_movies_producer(self):
        t_movie = {"title":"Sully", "release_date":"2022-12-22"}
        response=self.client.post("/movies",json=t_movie,headers={
                                     "Authorization": "Bearer {}"
                                     .format(self.producer)
                                 })
        r_data=json.loads(response.data)
        self.assertTrue(r_data['success'],"success attribute in response json was false")
        i_movie=Movie.query.get(r_data['movies']['id'])
        t_movie["id"]=r_data['movies']['id']
        self.assertEqual(i_movie.serialized_movie(),t_movie,"Movie in test case and the movie posted in DB are not same")

    def test_delete_a_movie_producer(self):
        t_movie  = {"title":"Sully", "release_date":"2022-12-22"}
        response=self.client.post("/movies",json=t_movie,headers={
                                     "Authorization": "Bearer {}"
                                     .format(self.producer)
                                 })
        id=json.loads(response.data)['movies']['id']
        response_upd=self.client.delete(f'/movies/{id}',headers={
                                     "Authorization": "Bearer {}"
                                     .format(self.producer)
                                 })
        r_data=json.loads(response_upd.data)
        self.assertTrue(r_data['success'],"success attribute in response json was false")
        self.assertEqual(r_data['id'],id,"Movie inserted hasn't been deleted")

    def test_post_a_movies_assitant(self):
        t_movie = {"title":"Sully", "release_date":"2022-12-22"}
        response=self.client.post("/movies",json=t_movie,headers={
                                     "Authorization": "Bearer {}"
                                     .format(self.assistant)
                                 })
        r_data=json.loads(response.data)
        self.assertFalse(r_data['success'],"success attribute in response json was True")
        self.assertEqual(int(r_data['error']),403,"error code is not 403")

    def test_delete_a_movie_assitant(self):
        t_movie  = {"title":"Sully", "release_date":"2022-12-22"}
        response=self.client.post("/movies",json=t_movie,headers={
                                     "Authorization": "Bearer {}"
                                     .format(self.producer)
                                 })
        id=json.loads(response.data)['movies']['id']
        response_upd=self.client.delete(f'/movies/{id}',headers={
                                     "Authorization": "Bearer {}"
                                     .format(self.assistant)
                                 })
        r_data=json.loads(response_upd.data)
        self.assertFalse(r_data['success'],"success attribute in response json was True")
        self.assertEqual(int(r_data['error']),403,"error code is not 403")

    def test_post_a_movies_director(self):
        t_movie = {"title":"Sully", "release_date":"2022-12-22"}
        response=self.client.post("/movies",json=t_movie,headers={
                                     "Authorization": "Bearer {}"
                                     .format(self.director)
                                 })
        r_data=json.loads(response.data)
        self.assertFalse(r_data['success'],"success attribute in response json was True")
        self.assertEqual(int(r_data['error']),403,"error code is not 403")

    def test_delete_a_movie_director(self):
        t_movie  = {"title":"Sully", "release_date":"2022-12-22"}
        response=self.client.post("/movies",json=t_movie,headers={
                                     "Authorization": "Bearer {}"
                                     .format(self.producer)
                                 })
        id=json.loads(response.data)['movies']['id']
        response_upd=self.client.delete(f'/movies/{id}',headers={
                                     "Authorization": "Bearer {}"
                                     .format(self.director)
                                 })
        r_data=json.loads(response_upd.data)
        self.assertFalse(r_data['success'],"success attribute in response json was True")
        self.assertEqual(int(r_data['error']),403,"error code is not 403")

if __name__ == "__main__":
    unittest.main()