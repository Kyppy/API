import unittest
from flask import json
from app import create_app

app = create_app()

class TestUsers(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.data ={
            "id":800,
            "createdOn":"21-02-2018",
            "createdBy":1010010,
            "type":"red-flag",
            "location":"15N,30N",
            "status":"Resolved",
            "Images":"[Image]",
            "Videos":"[Image]",
            "comment":"Police bribery witnessed."
             }
    
    def test_get_empty_record(self):
        response = self.app.get('/api/v1/red_flag/800')
        result = json.loads(response.data)
        self.assertEqual(result['status'],404)

    def test_get_all_empty_records(self):
        response = self.app.get('/api/v1/red_flags')
        result = json.loads(response.data)
        self.assertEqual(result['status'],200)
    
    def test_empty_comment_patch(self):
        response = self.app.get('/red_flag/800/comment', data=json.dumps(self.data), content_type='application/json')
        self.assertEqual(response.status_code,404)
    
    def test_empty_location_patch(self):
        response = self.app.get('/red_flag/800/location', data=json.dumps(self.data), content_type='application/json')
        self.assertEqual(response.status_code,404)
    
    def test_delete_empty_record(self):
        response = self.app.delete('/api/v1/red_flag/800')
        result = json.loads(response.data)
        self.assertEqual(result['status'],404)
   
    def test_post_record_and_get_record(self):
        response = self.app.post('/api/v1/red_flag/800', data=json.dumps(self.data), content_type='application/json')
        self.assertEqual(response.status_code,200)
        response = self.app.get('/api/v1/red_flag/800')
        result = json.loads(response.data)
        self.assertEqual(result['status'],200)
    
    def test_post_record_twice(self):
        self.app.post('/api/v1/red_flag/800', data=json.dumps(self.data), content_type='application/json')
        response = self.app.post('/api/v1/red_flag/800', data=json.dumps(self.data), content_type='application/json')
        self.assertEqual(response.status_code,400)
    
    
    
      

