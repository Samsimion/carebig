from extensions import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime, timezone

class MedicalHistory(db.Model, SerializerMixin):
    __tablename__ = 'medical_histories'

    id = db.Column(db.Integer, primary_key=True)
    allergies = db.Column(db.Text)
    medications = db.Column(db.Text)
    past_surgeries = db.Column(db.Text)
    emergency_notes = db.Column(db.Text)
    created_at = db.Column(db.Datetime, default=datetime.now(timezone.utc))
    
    
    updated_by_user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    child_id = db.Column(db.Integer, db.ForeignKey('child_profiles.id'))
    condition_id = db.Column(db.Integer, db.ForeignKey('conditions.id'))
