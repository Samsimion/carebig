from extensions import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime, timezone

class SessionFeedback(db.Model, SerializerMixin):
    __tablename__ = 'session_feedbacks'

    id = db.Column(db.Integer, primary_key=True)
    self_reflection =db.Column(db.Text)
    peer_review = db.Column(db.Text)
    created_at = db.Column(db.Datetime, default=datetime.now(timezone.utc))


    session_id = db.Column(db.Integer, db.ForeignKey('sessions.id'))
    therapist_id = db.Column(db.Integer, db.ForeignKey('therapist_profiles.id'))