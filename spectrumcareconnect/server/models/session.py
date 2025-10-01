from extensions import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import  hybrid_property
from datetime import datetime, timezone

class Sessions(db.Model, SerializerMixin):
    __tablename__ ='sessions'

    id = db.Column(db.Integer, primary_key=True)
    is_deleted = db.Column(db.Boolean, default=False)
    archieved_at = db.Column(db.Datetime, default =datetime.now(timezone.utc))
    price_cents = db.Column(db.Integer)
    created_at = db.Column(db.Datetime, default=datetime.now(timezone.utc))
    updated_at = db.Column(db.Datetime, default=datetime.now(timezone.utc))



    child_id = db.Column(db.Integer, db.ForeignKey('child_profiles.id'),nullable=False)
    therapist_id = db.Column(db.Integer, db.ForeignKey('therapist_profiles.id'))
    therapy_type_id = db.Column(db.Integer, db.ForeignKey('therapy_types.id'))
    condition_id = db.Column(db.Integer, db.ForeignKey('conditions.id'))
    availability_slot_id = db.Column(db.Integer, db.ForeignKey('availability_slots.id'))
    created_by_user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
