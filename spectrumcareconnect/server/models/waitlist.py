from extensions import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime, timezone

class Waitlist(db.Model, SerializerMixin):
    __tablename__ = 'waitlists'

    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Enum('waiting','notified','booked','cancelled'))
    created_at = db.Column(db.Datetime, default=datetime.now(timezone.utc))

    availability_slot_id = db.Column(db.Integer,db.ForeignKey('availability_slots.id'))
    parent_id = db.Column(db.Integer, db.ForeignKey('parent_profiles.id'))
    child_id = db.Column(db.Integer, db.ForeignKey('child_profiles.id'))
