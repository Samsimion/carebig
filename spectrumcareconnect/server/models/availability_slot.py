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

    # relations
    therapist_id = db.Column(db.Integer, db.ForeignKey('therapist_profiles.id'), nullable=False)


    # relationship
    therapist_profiles = db.relationship('TherapistProfile', back_populates='availaility_slots', foreign_keys=[therapist_id])
    sessions = db.relationship('Session', back_populates='availability_slots', foreign_keys='Session.availability_slot_id', cascade= 'all, delete-orphan')
    waitlists = db.relationship('Waitlist', back_populates='availability_slot', foreign_keys='Waitlist.availability_slot_id', cascade='all, delete-orphan')

    serialize_rules = ('-therapist_profiles.availaility_slots', '-sessions.availability_slots','-waitlists.availability_slot',)

    def __repr__(self):
        return f"<AvailabilitySlot id={self.id} start_time={self.start_time} end_time={self.end_time} status={self.status} location_type={self.location_type} meeting_link='{self.meeting_link}' therapist_id={self.therapist_id}>"