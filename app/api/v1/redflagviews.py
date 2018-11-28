from flask import Flask, request
from flask_restful import Resource, Api

from .redflagmodels import RedFlagModel

class RedFlag(Resource, RedFlagModel):
	
	def __init__(self):
        self.incidents = RedFlagModel()
    
    def get(self, red_flag_id):
        incident = next(filter(lambda x: x['id'] == red_flag_id, self.incidents.db), None)
        return incident, 200 if incident else 404
	
	def post(self, red_flag_id):
        if next(filter(lambda x: x['id'] == red_flag_id, self.incidents.db), None):
            return {"message":"A red-flag with id '{}' already exists.".format(red_flag_id)}, 400
        data = request.get_json(silent=True)
        self.incidents.store(data)
        return self.incidents.db
		
	def delete(self, red_flag_id):
        self.incidents.db = list(filter(lambda x: x['id'] != red_flag_id, self.incidents.db))
        return{'message':'Incident deleted'}, 200
    
class Red_flags(Resource):

	def __init__(self):
        self.incidents = RedFlagModel()

    def get(self):
        return self.incidents.db, 200

class PatchLocation(Resource):

class PatchComment(Resource):







