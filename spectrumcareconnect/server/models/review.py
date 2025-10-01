from extensions import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime, timezone


class Review(db.Model, SerializerMixin):
    __tablename__ = 'reviews'

    id  = db.Column(db.Integer, primary_key= True)
    rating = db.Column(db.Integer, max(5))
    comment = db.Column(db.Text)
    created_at = db.Column(db.Datetime, default=datetime.now(timezone.utc))




    session_id= db.Column(db.Integer, db.ForeignKey('sessions.id'))
    parent_id= db.Column(db.Integer, db.ForeignKey('parent_profiles.id'))
