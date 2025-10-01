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
    category = db.Column(db.Enum('guide','exercise','worksheet','video','other'))
    is_public = db.Column(db.Boolean, default=False)
    language_code = db.Column(db.String)
    created_at= db.Column(db.Datetime, default=datetime.now(timezone.utc))
    uploaded_by_user_id = db.Column(db.Integer, db.ForeignKey('users.id'))