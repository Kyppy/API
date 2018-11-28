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

	def __init__(self):
        self.incidents = RedFlagModel()

    def patch(self, red_flag_id):
        data = request.get_json(silent=True)
        incident = next(filter(lambda x: x['id'] == red_flag_id, self.incidents.db), None)
        if incident is None:
            return{"message":"A red-flag incident with id '{}' does not exist.".format(red_flag_id)}, 404

        elif data['location'] == None:
            return{"message":"No location patch data was sent."}, 400
        
        else:
            incident['location']= data['location']
        return self.incidents.db, 200

class PatchComment(Resource):

	def __init__(self):
        self.incidents = RedFlagModel()

    def patch(self, red_flag_id):
        data = request.get_json(silent=True)
        incident = next(filter(lambda x: x['id'] == red_flag_id, self.incidents.db), None)
        if incident is None:
            return{"message":"A red-flag incident with id '{}' does not exist.".format(red_flag_id)}, 404

        elif data['comment'] == None:
            return{"message":"No comment patch data was sent."}, 400
        
        else:
            incident['comment']= data['comment']
        return self.incidents.db, 200







