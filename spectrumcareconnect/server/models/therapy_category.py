from extensions import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime, timezone

class Therapy_category(db.Model, SerializerMixin):
    __tablename__='therapy_categories' 


    id =db.Column(db.Integer, primary_key=True)
    name =db.Column(db.String(150))
    description= db.Column(db.Text)
    created_at = db.Column(db.Datetime, default=datetime.now(timezone.utc))
    updated_at =db.Column(db.Datetime, default=datetime.now(timezone.utc))