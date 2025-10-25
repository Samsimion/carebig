from extensions import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime, timezone


class Consent(db.Model, SerializerMixin):
    __tablename__ = 'consents'

    id = db.Column(db.Integer, primary_key= True)
    scope = db.Column(db.Enum('medical_reports','progress','school_sharing','all',name='consent_scope'))
    status = db.Column(db.Enum('requested','granted','revoked', name='consent_status'))
    created_at =db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    expiry_date = db.Column(db.DateTime, nullable=True)


    #relations
    child_id = db.Column(db.Integer, db.ForeignKey('child_profiles.id'), nullable=False )
    granted_to_user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    #relationship
    child_profile = db.relationship('ChildProfile', back_populates='consent', foreign_keys=[child_id])
    user = db.relationship('User', back_populates='consent', foreign_keys=[granted_to_user_id])
    
    serialize_rules = ('-child_profile.consent','-user.consent',)

    def __repr__(self):
        return f"<Consent id={self.id} scope={self.scope} status={self.status} child_id={self.child_id} granted_to_user_id={self.granted_to_user_id}>"
    