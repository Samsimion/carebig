from flask_sqlalchemy import SQLAlchemy
from flask_marshmellow import Marshmallow
from flask_jwt_extended import JWTManager
from flask_bycrpt import Bycrypt
from flask_cors import CORS


db=SQLAlchemy()
ma=Marshmallow()
jwt=JWTManager()
bycrypt= Bycrypt()
cors= CORS()
