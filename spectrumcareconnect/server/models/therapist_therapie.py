from extensions import db
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime, timezone


class Therapist_therapies(db.Model, SerializerMixin):
    __tablename__ = 'therapist_therapies'

    id =db.Column(db.Integer, primary_key=True)
    therapist_id =db.Column(db.Integer, db.ForeignKey('therapist_profiles.id'), nullable=False)
    therapy_type_id = db.Column(db.Integer, db.ForeignKey('therapy_types.id'), nullable=False)
    qualification_notes = db.Column(db.Text)
    experience_years = db.Column(db.Integer)
    is_primary_speciality = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.Datetime, default= datetime.now(timezone.utc))



    
