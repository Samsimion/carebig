from extensions import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime, timezone

class Appointment(db.Model, SerializerMixin):
    __tablename__ ='appointments'

    id = db.Column(db.Integer, primary_key=True)

    type =db.Column(db.Enum('medical','educational','other', name='appointment_type'))
    scheduled_at = db.Column(db.DateTime)
    status = db.Column(db.Enum('scheduled','completed','cancelled', name='appointment_status'))
    notes =db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))    

    #relations
    child_id = db.Column(db.Integer, db.ForeignKey('child_profiles.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False) #doctor/therapist/teacher
    
    #relationship
    child_profiles = db.relationship('ChildProfile', back_populates='appointments', foreign_keys=[child_id])
    users = db.relationship('User', back_populates='appointments', foreign_keys=[user_id])
    
    serialize_rules = ('-child_profiles.appointments', '-users.appointments',)


    def __repr__(self):
        return f"<Appointment id={self.id} type={self.type}  scheduled_at={self.scheduled_at} status={self.status} notes='{self.notes}' child_id={self.child_id} user_id={self.user_id}>"