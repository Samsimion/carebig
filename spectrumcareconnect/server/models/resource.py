from extensions import db
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime, timezone

class Resource(db.Model, SerializerMixin):
    __tablename__ = 'resources'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.Text)
    file_url = db.Column(db.String)
    category = db.Column(db.Enum('guide','exercise','worksheet','video','other',name='resource_category'))
    is_public = db.Column(db.Boolean, default=False)
    language_code = db.Column(db.String)
    created_at= db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))
    # relations
    uploaded_by_user_id = db.Column(db.Integer, db.ForeignKey('users.id', name="fk_resource_uploadedbyuser_id"))

    # relationships
    uploaded_by_user = db.relationship('User', back_populates='resources', foreign_keys=[uploaded_by_user_id])

    serialize_rules = ('-uploaded_by_user.resources',)

    def __repr__(self):
        return f"<Resource id={self.id} title='{self.title}' description='{self.description}' file_url='{self.file_url}' category={self.category} is_public={self.is_public} language_code='{self.language_code}' created_at={self.created_at} uploaded_by_user_id={self.uploaded_by_user_id}>"
        