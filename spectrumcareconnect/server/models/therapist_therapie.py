from extensions import db
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime, timezone


class TherapistTherapies(db.Model, SerializerMixin):
    __tablename__ = 'therapist_therapies'

    id =db.Column(db.Integer, primary_key=True)
    
    qualification_notes = db.Column(db.Text)
    experience_years = db.Column(db.Integer)
    is_primary_speciality = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.Datetime, default= datetime.now(timezone.utc))

    #relations
    therapist_id =db.Column(db.Integer, db.ForeignKey('therapist_profiles.id'), nullable=False)
    therapy_type_id = db.Column(db.Integer, db.ForeignKey('therapy_types.id'), nullable=False)

    #relationship
    therapist_profile = db.relationship('TherapistProfile', back_populates='therapist_therapie', foreign_keys=[therapist_id])
    therapy_type = db.relationship('TherapyType', back_populates='therapist_therapie', foreign_keys=[therapy_type_id])




    
