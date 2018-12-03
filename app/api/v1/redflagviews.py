from flask import Flask, request
from flask_restful import Resource

from .redflagmodels import RedFlagModel

incidents = RedFlagModel()
class RedFlag(Resource, RedFlagModel):
    pass







