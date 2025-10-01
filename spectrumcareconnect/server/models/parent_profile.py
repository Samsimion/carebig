from extensions import db, bycrypt
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime, timezone

class Parent_profile(db.Model, SerializerMixin):
    __tablename__= 'parent_profiles'

    id= db.Column(db.Integer, primary_key=True, nullable=False)
    
    date_of_birth = db.Column(db.DateTime)
    gender =db.Column(db.Enum('male', 'female', 'other', 'prefer_not_to_say'))
    address_line = db.Column(db.String(130))
    address_line2= db.Column(db.String(130))
    city = db.Column(db.String(130))
    state_province = db.Column(db.String(155))
    postal_code = db.Column(db.String(130))
    country = db.Column(db.String(155))
    preferred_language = db.Column(db.String(120))
    emergency_contact_phone = db.Column(db.String(20),nullable=False)
    occupation = db.Column(db.String(155))
    household_notes=db.Column(db.String())
    created_at= db.Column(db.DateTime, default=datetime.now(timezone.utc))
    updated_at= db.Column(db.DateTime, default=datetime.now(timezone.utc))
    is_deleted= db.Column(db.Boolean, default= False)
    archived_at =db.Column(db.DateTime, default=datetime.now(timezone.utc))


    #relations
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'),nullable=False , unique=True)

    #relationships

    user= db.relationship('User', back_populates= 'parent_prof')


