from extensions import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime, timezone

class Child_therapist(db.Model, SerializerMixin):
    __tablename__ = 'child_therapists'

    id = db.Column(db.Integer, primary_key=True)
    relationship_type =db.Column(db.Enum('primary','secondary','temporary'))
    start_date = db.Column(db.Datetime)
    end_date = db.Column(db.Datetime)
    created_at =db.Column(db.Datetime, default= datetime.now(timezone.utc))
    is_deleted =db.Column(db.Boolean ,default=False)
    archived_at = db.Column(db.Datetime ,default =datetime.now(timezone.utc))


    child_id = db.Column(db.Integer, db.ForeignKey('child_profiles.id') ,nullable=False)
    therapist_id =db.Column(db.Integer, db.ForeignKey('therapist_profiles.id'))
