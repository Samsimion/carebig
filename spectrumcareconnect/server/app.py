from flask import Flask, make_response,send_from_directory,jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api,Resource
from flask_migrate import Migrate
from flask_socketio import SocketIO
from flasgger import Swagger

from config import Config
from marshmallow import ValidationError
from datetime import timedelta
from flask_jwt_extended import jwt_required
from extensions import db, ma,jwt,bcrypt,cors

app = Flask(__name__,
    static_url_path='',
    static_folder='../client/dist',
    template_folder='../client/dist'
            )

app.config.from_object(Config)
socketio = SocketIO(app, cors_allowed_origins="*")


db.init_app(app)
ma.init_app(app)
jwt.init_app(app)
bcrypt.init_app(app)
cors.init_app(app, resources={ r"/api/spectrumcareconnect/*": {"origins": "http://localhost:5173"}}, supports_credentials=True)
api=Api(app)
swagger=Swagger(app)

from models import *
migrate = Migrate(app,db)

#routes
from routes.auth_routes import Registration,Login


# api endpoint
api.add_resource(Registration, '/api/registration', endpoint='registration')
api.add_resource(Login, '/api/login', endpoint="login")