from extensions import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime, timezone


class Parent_child_links(db.Model, SerializerMixin):
    __tablename__ = 'parent_child_links'

    id = db.Column(db.Integer, primary_key=True)
    parent_relationship = db.Column(db.Enum('mother','father','guardian','sibling','other'))
    created_at = db.Column(db.Datetime, default= datetime.now(timezone.utc))



    parent_id = db.Column(db.Integer, db.ForeignKey('parent_profiles.id'), nullable=False)
    child_id= db.Column(db.Integer, db.ForeignKey('child_profiles.id') ,nullable=False)
