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

    # relations
    child_id = db.Column(db.Integer, db.ForeignKey('child_profiles.id'))
    session_id = db.Column(db.Integer, db.ForeignKey('sessions.id'))
    uploaded_by_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    # relationships
    child_profile = db.relationship('ChildProfile', back_populates='media_storage', foreign_keys=[child_id] )
    session = db.relationship('Session', back_populates='media_storage', foreign_keys=[session_id])
    uploaded_by = db.relationship('User' , back_populates='media_storage', foreign_keys=[uploaded_by_id])

    serialize_rules = ('-child_profile.media_storage','-session.media_storage','uploaded_by.media_storage',)

    def __repr__(self):
        return f"<MediaStorage id={self.id} file_url={self.file_url} file_type={self.file_type} description={self.description} is_sensitive={self.is_sensitive} created_at={self.created_at} child_id={self.child_id} session_id={self.session_id} uploaded_by_id={self.uploaded_by_id}>"