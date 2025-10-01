from extensions import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime, timezone

class Appointment(db.Model, SerializerMixin):
    __tablename__ ='appointments'

    id = db.Column(db.Integer, primary_key=True)

    type =db.Column(db.Enum('medical','educational','other'))
    scheduled_at = db.Column(db.Datetime)
    status = db.Column(db.Enum('scheduled','completed','cancelled'))
    notes =db.Column(db.Text)
    created_at = db.Column(db.Datetime, default=datetime.now(timezone.utc))    


    child_id = db.Column(db.Integer, db.ForeignKey('child_profiles.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False) #doctor/therapist/teacher
