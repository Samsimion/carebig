from extensions import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime, timezone

class Waitlist(db.Model, SerializerMixin):
    __tablename__ = 'waitlists'

    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Enum('waiting','notified','booked','cancelled', name='waitlist_status'))
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))
    
    # relations
    availability_slot_id = db.Column(db.Integer,db.ForeignKey('availability_slots.id', name="fk_waitlist_availability_slot_id"),nullable=False)
    parent_id = db.Column(db.Integer, db.ForeignKey('parent_profiles.id', name="fk_waitlist_parent_id"))
    child_id = db.Column(db.Integer, db.ForeignKey('child_profiles.id', name="fk_waitlist_child_id"))
    

    # relationships
    availability_slot = db.relationship('AvailabilitySlot', back_populates='waitlists',foreign_keys=[availability_slot_id])
    parent_profile= db.relationship('ParentProfile', back_populates='waitlists', foreign_keys=[parent_id])
    child_profile = db.relationship('ChildProfile', back_populates='waitlists', foreign_keys=[child_id])
    
    serialize_rules=('-availability_slot.waitlists','-parent_profile.waitlists','-child_profile.waitlists',)

    def __repr__(self):
        return f"<Waitlist id={self.id} status={self.status} created_at={self.created_at} availability_slot_id={self.availability_slot_id} parent_id={self.parent_id} child_id={self.child_id}>"