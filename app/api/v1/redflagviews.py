from flask import Flask, request
from flask_restful import Resource, Api

from .redflagmodels import RedFlagModel

class RedFlag(Resource, RedFlagModel):
	
	def __init__(self):
        self.incidents = RedFlagModel()
    
    def get(self, red_flag_id):
        incident = next(filter(lambda x: x['id'] == red_flag_id, self.incidents.db), None)
        return incident, 200 if incident else 404
    
class Red_flags(Resource):

class PatchLocation(Resource):

class PatchComment(Resource):







