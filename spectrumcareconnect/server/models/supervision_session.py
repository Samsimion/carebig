from extensions import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime, timezone


class SupervisionSession(db.Model, SerializerMixin):
    __tablename__ ='supervision_sessions'

    id = db.Column(db.Integer, primary_key=True)
    notes = db.Column(db.Text)
    created_at = db.Column(db.Datetime, default=datetime.now(timezone.utc))

    junior_therapist_id = db.Column(db.Integer, db.ForeignKey('therapist_profiles.id'))
    senior_therapist_id = db.Column(db.Integer, db.ForeignKey('therapist_profiles.id'))
    session_id = db.Column(db.Integer, db.ForeignKey('sessions.id'))