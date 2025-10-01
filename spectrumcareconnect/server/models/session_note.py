from extensions import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime, timezone

class SessionNote(db.Model, SerializerMixin):
    __tablename__ ='session_notes'

    id = db.Column(db.Integer, primary_key=True)
    summary = db.Column(db.Text)
    detailed_notes= db.Column(db.Text)
    recommendations = db.Column(db.Text)
    shared_with_parent= db.Column(db.Boolean, default=False)
    shared_with_school=db.Column(db.Boolean, default=False)
    created_at = db.Column(db.Datetime, default=datetime.now(timezone.utc))
    updated_at = db.Column(db.Datetime, default=datetime.now(timezone.utc))




    session_id = db.Column(db.Integer, db.ForeignKey('sessions.id'))
    therapist_id = db.Column(db.Integer, db.ForeignKey('therapist_profiles.id'))
    child_id = db.Column(db.Integer, db.ForeignKey('child_profiles.id'))