import unittest
from flask import json
from app import create_app

app = create_app()

class TestUsers(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.data ={"body"}
        self.data2 = [""]
    
    def test_get(self):
        response = self.app.get('/api/v1/red_flag/500')
        result = json.loads(response.data)
        self.assertEqual(result['status'],404)
      
    """
    def test_post(self):
        response = self.app.post('/',data=json.dumps(self.data), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(response.status_code,"user"), 201
    """

