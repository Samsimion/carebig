from extensions import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime, timezone


class Message(db.Model, SerializerMixin):
    __tablename__ = 'messages'

    id = db.Column(db.Integer, primary_key=True)
    content =db.Column(db.Text)
    is_read =db.Column(db.Boolean)
    created_at = db.Column(db.Datetime, default=datetime.now(timezone.utc))




    sender_id = db.Column(db.Integer , db.ForeignKey('users.id'), nullable=False)
    receiver_id = db.Column(db.Integer, db.ForeignKey('users.id'),nullable=False)
