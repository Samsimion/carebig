from extensions import db
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime, timezone


class TherapistTherapies(db.Model, SerializerMixin):
    __tablename__ = 'therapist_therapies'

    id =db.Column(db.Integer, primary_key=True)
    
    qualification_notes = db.Column(db.Text)
    experience_years = db.Column(db.Integer)
    is_primary_speciality = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    #relations
    therapist_id =db.Column(db.Integer, db.ForeignKey('therapist_profiles.id', name="fk_therapisttherapie_therapist_id"), nullable=False)
    therapy_type_id = db.Column(db.Integer, db.ForeignKey('therapy_types.id', name="fk_therapisttherapie_therapy_type_id"), nullable=False)

    #relationship
    therapist_profile = db.relationship('TherapistProfile', back_populates='therapist_therapie', foreign_keys=[therapist_id])
    therapy_type = db.relationship('TherapyType', back_populates='therapist_therapie', foreign_keys=[therapy_type_id])

    serialize_rules =('-therapist_profile.therapist_therapie','-therapy_type.therapist_therapie',)

    def __repr__(self):
        return f"<TherapistTherapies id={self.id} qualification_notes='{self.qualification_notes}' experience_years={self.experience_years} is_primary_speciality={self.is_primary_speciality} created_at={self.created_at} therapist_id={self.therapist_id} therapy_type_id={self.therapy_type_id}>"