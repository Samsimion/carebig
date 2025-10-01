from extensions import db
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime, timezone

class Therapy_type(db.Model, SerializerMixin):
    __tablename__ = 'therapy_types'

    id= db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description= db.Column(db.Text)
    session_length_min = db.Column(db.Integer)
    recomendation_frequency = db.Column(db.String)
    delivery_modes= db.Column(db.Text)
    is_active= db.Column(db.Boolean, default=False)
    created_at= db.Column(db.Datetime, default= datetime.now(timezone.utc))
    updated_at = db.Column(db.Datetime,default=datetime.now(timezone.utc))
    


    category_id = db.Column(db.Integer, db.ForeignKey('therapy_categories.id'))
