from extensions import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime, timezone

class ChildTherapist(db.Model, SerializerMixin):
    __tablename__ = 'child_therapists'

    id = db.Column(db.Integer, primary_key=True)
    relationship_type =db.Column(db.Enum('primary','secondary','temporary'))
    start_date = db.Column(db.Datetime)
    end_date = db.Column(db.Datetime)
    created_at =db.Column(db.Datetime, default= datetime.now(timezone.utc))
    is_deleted =db.Column(db.Boolean ,default=False)
    archived_at = db.Column(db.Datetime ,default =datetime.now(timezone.utc))

    #relation
    child_id = db.Column(db.Integer, db.ForeignKey('child_profiles.id') ,nullable=False)
    therapist_id =db.Column(db.Integer, db.ForeignKey('therapist_profiles.id'))
    
    #relationship
    child_profiles = db.relationship('ChildProfile', back_populates='child_therapist', foreign_keys=[child_id])
    therapist_profile = db.relationship('TherapistProfile',back_populates='child_therapist', foreign_keys=[therapist_id])
