from extensions import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import  hybrid_property
from datetime import datetime, timezone

class Session(db.Model, SerializerMixin):
    __tablename__ ='sessions'

    id = db.Column(db.Integer, primary_key=True)
    is_deleted = db.Column(db.Boolean, default=False)
    completed_at = db.Column(db.DateTime, default =lambda: datetime.now(timezone.utc))
    price_cents = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    achieved_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))


    # relations
    child_id = db.Column(db.Integer, db.ForeignKey('child_profiles.id'),nullable=False)
    therapist_id = db.Column(db.Integer, db.ForeignKey('therapist_profiles.id'))
    therapy_type_id = db.Column(db.Integer, db.ForeignKey('therapy_types.id'))
    condition_id = db.Column(db.Integer, db.ForeignKey('conditions.id'))
    availability_slot_id = db.Column(db.Integer, db.ForeignKey('availability_slots.id'))
    created_by_user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    # relationship
    child_profiles= db.relationship('ChildProfile', back_populates='sessions', foreign_keys=[child_id])
    therapist_profiles = db.relationship('TherapistProfile' ,back_populates='sessions', foreign_keys=[therapist_id])
    therapy_type = db.relationship('TherapyType', back_populates='session', foreign_keys=[therapy_type_id])
    conditions = db.relationship('Condition', back_populates='session', foreign_keys=[condition_id])
    availability_slots= db.relationship('AvailabilitySlot', back_populates='sessions', foreign_keys=[availability_slot_id])
    created_user = db.relationship('User', back_populates='sessions', foreign_keys=[created_by_user_id])
    reviews = db.relationship('Review', back_populates='session', foreign_keys='Review.session_id', cascade='all, delete-orphan')
    progress_entries = db.relationship('ProgressEntry', back_populates='session',foreign_keys='ProgressEntry.session_id', cascade='all, delete-orphan')
    session_notes = db.relationship('SessionNote', back_populates='session', foreign_keys='SessionNote.session_id', cascade='all, delete-orphan')
    payment = db.relationship('Payment', back_populates='session', foreign_keys='Payment.session_id', cascade='all, delete-orphan')
    session_feedback = db.relationship('SessionFeedback', back_populates='session', foreign_keys='SessionFeedback.session_id', cascade='all, delete-orphan')
    supervision_session = db.relationship('SupervisionSession', back_populates='sessions', foreign_keys='SupervisionSession.session_id', cascade='all, delete-orphan')
    media_storage = db.relationship('MediaStorage', back_populates='session', foreign_keys='MediaStorage.session_id', cascade='all, delete-orphan')
    ai_analysis = db.relationship('AiAnalysis', back_populates='session', foreign_keys='AiAnalysis.session_id', cascade='all, delete-orphan')

    serialize_rules= ('-child_profiles.sessions','-therapist_profiles.sessions','-therapy_type.session','-conditions.session','-availability_slots.sessions', '-created_user.sessions', '-reviews.session', '-progress_entries.session', '-session_notes.session', '-payment.session', '-session_feedback.session', '-supervision_session.sessions', '-media_storage.session', '-ai_analysis.session',)

    def __repr__(self):
        return f"<Session id={self.id} is_deleted={self.is_deleted} achieved_at={self.achieved_at} price_cents={self.price_cents} created_at={self.created_at} updated_at={self.updated_at} child_id={self.child_id} therapist_id={self.therapist_id} therapy_type_id={self.therapy_type_id} condition_id={self.condition_id} availability_slot_id={self.availability_slot_id} created_by_user_id={self.created_by_user_id}>"