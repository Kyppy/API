from flask import Flask, request
from flask_restful import Resource, Api

from .redflagmodels import RedFlagModel

class RedFlag(Resource, RedFlagModel):

    def __init__(self):
        self.incidents = RedFlagModel()
    
    def get(self, red_flag_id):
        incident = next(filter(lambda x: x['id'] == red_flag_id, self.incidents.db), None)
        return {"status":200,"data":incident} if incident else {"status":404,"message":"An incident with id '{}' does not exist.".format(red_flag_id)}
    
    def post(self, red_flag_id):
        data = request.get_json(silent=True)
        if data['id'] != red_flag_id:
            return {"message":"'id'{} provided by request body and 'id' {} provided by url do not match".format(data['id'],red_flag_id)}, 400
        if next(filter(lambda x: x['id'] == red_flag_id, self.incidents.db), None):
            return {"message":"A red-flag with id '{}' already exists.".format(red_flag_id)}, 400

        self.incidents.store(data)
        return {"status":201,"data":{"id":red_flag_id,"message":"created red-flag record"}}
    
    def delete(self, red_flag_id):
        incident = next(filter(lambda x: x['id'] == red_flag_id, self.incidents.db), None)
        if incident == None:
            return {"status":404,"message":"An incident with id '{}' does not exist.".format(red_flag_id)}
        else:
            self.incidents.db = list(filter(lambda x: x['id'] != red_flag_id, self.incidents.db))
            return {"status":200,"data":{"id":red_flag_id,"message":"red-flag record has been deleted"}}
    
class RedFlags(Resource):

    def __init__(self):
        self.incidents = RedFlagModel()

    def get(self):
        return{"status":200,"data":self.incidents.db} 

class PatchLocation(Resource):

    def __init__(self):
        self.incidents = RedFlagModel()

    def patch(self, red_flag_id):
        data = request.get_json(silent=True)
        if data['id'] != red_flag_id:
            return{"message":"'id'{} provided by request body and 'id' {} provided by url do not match".format(data['id'],red_flag_id)}, 400

        incident = next(filter(lambda x: x['id'] == red_flag_id, self.incidents.db), None)
        if incident is None:
            return{"message":"A red-flag incident with id '{}' does not exist.".format(red_flag_id)}, 404

        elif data['location'] == None:
            return{"message":"No location patch data was sent."}, 404

        else:
            incident['location']= data['location']
        return {"status":200,"data":{"id":red_flag_id,"message":"Updated red-flag record's location"}}

class PatchComment(Resource):

    def __init__(self):
        self.incidents = RedFlagModel()

    def patch(self, red_flag_id):
        data = request.get_json(silent=True)
        if data['id'] != red_flag_id:
            return{"message":"'id'{} provided by request body and 'id' {} provided by url do not match".format(data['id'],red_flag_id)}, 400
        incident = next(filter(lambda x: x['id'] == red_flag_id, self.incidents.db), None)
        if incident is None:
            return{"message":"A red-flag incident with id '{}' does not exist.".format(red_flag_id)}, 404

        elif data['comment'] == None:
            return{"message":"No comment patch data was sent."}, 400
        
        else:
            incident['comment']= data['comment']
        return {"status":200,"data":{"id":red_flag_id,"message":"Updated red-flag record's comment"}}






