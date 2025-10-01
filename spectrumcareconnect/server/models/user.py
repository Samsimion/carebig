from extensions import db, bycrypt
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime, timezone

class User(db.Model,SerializerMixin):
    __tablename__= 'users'
    

    id=db.Column(db.Integer, primary_key=True)
    first_name=db.Column(db.String(120), unique=True,nullable=False)
    last_name = db.Column(db.String(120),nullable=False)
    middle_name =db.Column(db.String(120))
    email= db.Column(db.String(120), unique=True,nullable=False)
    _password_hash= db.Column(db.String(255), nullable=False)
    status = db.Column(db.Enum('active','inactive','suspended'),nullable=False)
    created_at= db.Column(db.DateTime,default=datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    last_login_at= db.Column(db.DateTime,default=datetime.now(timezone.utc))
    is_deleted =db.Column(db.Boolean, default=False)
    archived_at =db.Column(db.DateTime, default=datetime.now(timezone.utc))


    


    # relations
    role_id= db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False)
    


    # relationships
    role = db.relationship('Role', back_populates= 'users',foreign_keys=[role_id])
    parent_prof =db.relationship('Parent_profile', back_populates='user',foreign_keys= 'Parent_profile.user_id',uselist=False, cascade='all, delete-orphan')
    admin_prof= db.relationship('Admin_profile', back_populates= 'user', foreign_keys= 'Admin_profile.user_id', uselist=False, cascade='all, delete-orphan')


    #password handling property

    @hybrid_property
    def password(self):
        return self._password_hash
    

    @password.setter
    def password(self, plain_password):
        self._password_hash =bycrypt.generate_password_hash(plain_password).decode('utf-8')


    def check_password(self, plain_password):
        return bycrypt.check_password_hash(self._password_hash, plain_password)




