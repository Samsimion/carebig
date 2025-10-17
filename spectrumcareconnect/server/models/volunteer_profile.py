
from extensions import db
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime, timezone


class VolunteerProfile(db.Model, SerializerMixin):
    __tablename__='volunteer_profiles'

  
    id= db.Column(db.Integer, primary_key=True)
    skills = db.Column(db.String)
    availability =db.Colimn(db.String)
    created_at =db.Column(db.DateTime, default= datetime.now(timezone.utc))
    updated_at =db.Column(db.DateTime, default= datetime.now(timezone.utc))
    is_deleted =db.Column(db.Boolean, default=False)
    archived_at= db.Column(db.DateTime, default= datetime.now(timezone.utc))



    #relations
    user_id= db.Column(db.Integer, primary_key=True)


    #relationships
    user=db.relationship('User', back_populates='volunteer_prof', foreign_keys=[user_id])
    volunteer_assignemnt= db.relationship('VolunteerAssignment', back_populates='volunteer_prof_assign',foreign_keys='VolunteerAssignment.volunteer_id')





