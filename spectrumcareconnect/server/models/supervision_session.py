from extensions import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime, timezone


class SupervisionSession(db.Model, SerializerMixin):
    __tablename__ ='supervision_sessions'

    id = db.Column(db.Integer, primary_key=True)
    notes = db.Column(db.Text)
    created_at = db.Column(db.Datetime, default=datetime.now(timezone.utc))
    
    # relations
    junior_therapist_id = db.Column(db.Integer, db.ForeignKey('therapist_profiles.id'))
    senior_therapist_id = db.Column(db.Integer, db.ForeignKey('therapist_profiles.id'))
    session_id = db.Column(db.Integer, db.ForeignKey('sessions.id'))

    # relationships
    junior_therapist = db.relationship('TherapistProfile', back_populates='supervision_session', foreign_keys=[junior_therapist_id])
    senior_therapist=db.relationship('TherapistProfile', back_populates='senior_supervision_session', foreign_keys=[senior_therapist_id])
    sessions = db.relationship('Session', back_populates='supervision_session', foreign_keys=[session_id])
    
    serialize_rules = ('-junior_therapist.supervision_session', '-senior_therapist.senior_supervision_session','sessions.supervision_session',)

    def __repr__(self):
        return f"<SupervisionSession id={self.id} notes={self.notes} created_at={self.created_at} junior_therapist_id={self.junior_therapist_id} senior_therapist_id={self.senior_therapist_id} session_id={self.session_id}>"