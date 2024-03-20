
from flask_restful import Api
from flask import Blueprint
from app.auth.controllers.login import LoginView
# from app.auth.controllers.logout import LogOutView

from app.auth.controllers.signup import SignUpView


auth_blueprint =Blueprint("auth",__name__,url_prefix="/auth")
api=Api(auth_blueprint)

# http://127.0.0.1:5000/api/auth/signup/
api.add_resource(LoginView,"/login/") 
api.add_resource(SignUpView,"/signup/")
# api.add_resource(LogOutView,"/logout/")