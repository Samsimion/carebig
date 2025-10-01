from extensions import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime , timezone

class AvailabilitySlot(db.Model, SerializerMixin):
    __tablename__ ='availability_slots'

    id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.Datetime)
    end_time = db.Column(db.Datetime)
    status = db.Column(db.Enum('open','booked', 'blocked'))
    location_type = db.Column(db.Enum('in_person', 'virtual', 'group'))
    meeting_link = db.Column(db.String) #Africa/Nairobi
    created_at =db.Column(db.Datetime, default=datetime.now(timezone.utc))
    updated_at = db.Column(db.Datetime, default=datetime.now(timezone.utc))




    therapist_id = db