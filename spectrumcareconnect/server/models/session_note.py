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
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))


    # relations
    session_id = db.Column(db.Integer, db.ForeignKey('sessions.id', name="fk_sessionnote_session_id"))
    therapist_id = db.Column(db.Integer, db.ForeignKey('therapist_profiles.id', name="fk_sessionnote_therapist_id"))
    child_id = db.Column(db.Integer, db.ForeignKey('child_profiles.id', name="fk_sessionnote_child_id"))

    # relationships
    session = db.relationship('Session', back_populates='session_notes', foreign_keys=[session_id])
    therapist_profile = db.relationship('TherapistProfile', back_populates='session_notes', foreign_keys=[therapist_id])
    child_profile = db.relationship('ChildProfile', back_populates='session_notes', foreign_keys=[child_id] )

    serialize_rules=('-session.session_notes','-therapist_profile.session_notes','-child_profile.session_notes',)

    def __repr__(self):
        return f"<SessionNote id={self.id} summary='{self.summary}' detailed_notes='{self.detailed_notes}' recommendations='{self.recommendations}' shared_with_parent={self.shared_with_parent} shared_with_school={self.shared_with_school} created_at={self.created_at} updated_at={self.updated_at} session_id={self.session_id} therapist_id={self.therapist_id} child_id={self.child_id}>"