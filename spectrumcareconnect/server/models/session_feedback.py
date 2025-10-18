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
    
    # relations
    session_id = db.Column(db.Integer, db.ForeignKey('sessions.id'))
    therapist_id = db.Column(db.Integer, db.ForeignKey('therapist_profiles.id'))
    
    # relationship
    session = db.relationship('Session', back_populates='sessionfeedback', foreign_keys=[session_id])
    therapist_profile = db.relationship('TherapistProfile', back_populates='sessionfeedback', foreign_keys=[therapist_id])

    serialize_rules=('-session.sessionfeedback','-therapist_profile.sessionfeedback',)

    def __repr__(self):
        return f"<SessionFeedback id={self.id} self_reflection='{self.self_reflection}' peer_review='{self.peer_review}' created_at={self.created_at} session_id={self.session_id} therapist_id={self.therapist_id}>"