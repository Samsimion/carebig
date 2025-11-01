from flask import Flask, request,make_response
from app import db, ma,jwt, cors,bcrypt,api
from flask_migrate import Migrate
from flask_restful import Api, Resource
from models import User, Role
from marshmallow import fields, validates, ValidationError
from datetime import timedelta, datetime
from extensions import jwt
from flask_jwt_extended import create_access_token
import re

class RegistrationAuthSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User
        load_instance = True
        include_fk = True

    id = ma.auto_field(dump_only=True)
    first_name = ma.auto_field()
    last_name = ma.auto_field()
    middle_name = ma.auto_field()
    email = ma.Email(required=True)
    password = ma.Str(required=True, load_only=True)
    status = ma.auto_field(dump_only=True)
    created_at= ma.auto_field(dump_only=True)
    updated_at = ma.auto_field(dump_only=True)
    last_login_at = ma.auto_field(dump_only=True)
    is_deleted = ma.auto_field(dump_only=True)
    achieved_at = ma.auto_field(dump_only=True)
    role_id = ma.auto_field()

    @validates('password')
    def validate_password(self,value,**kwargs):
        if len(value)< 8:
            raise ValidationError('password must e atleast 8 characters.')
        if not re.search(r"[A-Z]", value):
            raise ValidationError('password must contain at least one uppercase letter.')
        if not re.search(r"[0-9]", value):
            raise ValidationError('Password must contain at least one number.')
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", value):
            raise ValidationError('Password must contain at least one special character.')

    url = ma.Hyperlinks(
        {
            "self": ma.URLFor('registration'),
        }
                        
    )
registration_schema = RegistrationAuthSchema()

# login schema
class LoginSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User
        load_instance=True

    email = ma.Email(required=True)
    password = ma.Str(required=True, load_only=True)

    url =ma.Hyperlinks(
        {
            'self':ma.URLFor('login')
        }
    )
login_schema = LoginSchema()

class Index(Resource):
    def get(self):
        response_dict = {
            'registration':'welcome to the registration restful api'
        }

        response = make_response(
            response_dict,
            200,
        )

        return response
api.add_resource(Index, '/')

class Login(Resource):
    def post(self):
        """
        User Login endpoint
        ---
        tags:
          - Authenticator
        description: Login user in SpectrumCareConnect
        consumes:
          - application/json
        parameters:
          - in: body
            name: body
            description: User login data
            required: true
            schema:
              type: object
              properties:
                email:
                  type: string
                  example: johndoe@example.com
                password:
                  type: string
                  example: StrongPass123!
        responses:
          200:
            description: User login successfully
            schema:
              type: object
              properties:
                message:
                  type: string
                  example: User login successfully
                user_id:
                  type: integer
                  example: 5
          400:
            description: Invalid email or password
        """

      
        data=request.get_json()

        try:
            validated_data=login_schema.load(data)
        except Exception as e:
            return {"message":str(e)},400
        email = validated_data.email
        raw_password = data.get("password")
        
        user =User.query.filter_by(email=email, is_deleted=False).first()
        if not user or not user.check_password(raw_password):
            return {"message": "invalid credentials"},401
        user.last_login_at = datetime.now()
        db.session.commit()

        access_token = create_access_token(identity=user.id, expires_delta=timedelta(hours=1))
        return make_response(
            {
                "access_token":access_token,
                "user": login_schema.dump(user)
            },200
        )
        

  


class Registration(Resource):
    def post(self):

        """
        User Registration Endpoint
        ---
        tags:
          - Authentication
        description: Register a new user in SpectrumCareConnect
        consumes:
          - application/json
        parameters:
          - in: body
            name: body
            description: User registration data
            required: true
            schema:
              type: object
              properties:
                first_name:
                  type: string
                  example: John
                last_name:
                  type: string
                  example: Doe
                middle_name:
                  type: string
                  example: M
                email:
                  type: string
                  example: johndoe@example.com
                password:
                  type: string
                  example: StrongPass123!
                role_id:
                  type: integer
                  example: 1
        responses:
          201:
            description: User registered successfully
            schema:
              type: object
              properties:
                message:
                  type: string
                  example: User registered successfully
                user_id:
                  type: integer
                  example: 5
          400:
            description: Invalid input or duplicate email
        """

        data=request.get_json()

        try:
            validated_data = registration_schema.load(data)
        except Exception as e:
            return {'message':str(e)}, 400
        
        if User.query.filter_by(email=validated_data.email).first():
            return {'message':"Email already registered"}, 400
        
        

        new_user = User(
        first_name=validated_data.first_name,
        last_name=validated_data.last_name,
        middle_name=validated_data.middle_name,
        email=validated_data.email,
        password=data['password'],  # this triggers the setter and hashes it
        role_id=validated_data.role_id
    )


        db.session.add(new_user)
        db.session.commit()

        return make_response(
            {
            'message': 'User registered successfully',
            'registered': registration_schema.dump(new_user)
        },201
        )
    
