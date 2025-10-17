from extensions import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime, timezone

class MediaStorage(db.Model, SerializerMixin):
    __tablename__ = 'media_storages'

    id = db.Column(db.Integer, primary_key=True)
    file_url = db.Column(db.String)
    file_type = db.Column(db.Enum('image','video','audio','document'))
    description = db.Column(db.Text)
    is_sensitive = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.Datetime, default=datetime.now(timezone.utc))


    child_id = db.Column(db.Integer, db.ForeignKey('child_profiles.id'))
    session_id = db.Column(db.Integer, db.ForeignKey('sessions.id'))
    uploaded_by = db.Column(db.Integer, db.ForeignKey('users.id'))

