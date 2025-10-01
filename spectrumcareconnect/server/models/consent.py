from extensions import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime, timezone


class Consent(db.Model, SerializerMixin):
    __tablename__ = 'consents'

    id = db.Column(db.Integer, primary_key= True)
    scope = db.Column(db.Enum('medical_reports','progress','school_sharing','all'))
    status = db.Column(db.Enum('in_process','granted','revoked'))
    created_at =db.Column(db.Datetime, default=datetime.now(timezone.utc))
    expiry_date = db.Column(db.Datetime, default=datetime.now(timezone.utc))



    child_id = db.Column(db.Integer, db.ForeignKey('child_profiles.id'), nullable=False )
    granted_to_user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
