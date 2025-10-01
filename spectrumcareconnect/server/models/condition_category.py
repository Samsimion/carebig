from extensions import db
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime, timezone

class Condition_category(db.Model, SerializerMixin):
    __tablename__ = 'condition_categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    desription =db.Column(db.Text)
    created_at= db.Column(db.Datetime, default=datetime.now(timezone.utc))

    updated_at= db.Column(db.Datetime, default=datetime.now(timezone.utc))