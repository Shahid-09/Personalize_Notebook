import datetime
import json
# from re import A
from flask import abort, jsonify, make_response, request, session
from flask_restful import Resource
from app import app
from app.md.model import User
from werkzeug.security import check_password_hash
import jwt

from app.md.serializer import UserSchema

class LoginView(Resource):

    def post(self):
        credentials=request.get_json()
        user=User.query.filter_by(username=credentials["username"]).first()
        if not user:
            abort(401)

        if not check_password_hash(user._password,credentials["password"]):
            abort(401)
        session['user_id']=user.id
        token = jwt.encode({'user_id' : user.id, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=60)}, app.config['SECRET_KEY'],algorithm="HS256")
        return jsonify({'token' : token})
        
        

