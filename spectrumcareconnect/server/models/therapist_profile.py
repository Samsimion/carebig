from extensions import db
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime, timezone


class TherapistProfile(db.Model,SerializerMixin):
    __tablename__ = 'therapist_profiles'
    __table_args__ =(
        db.CheckConstraint('rating_avg<=5',name='valid_avg_rating' ),
    )


    id= db.Column(db.Integer , primary_key=True)
    
    date_of_birth= db.Column(db.String)
    gender =db.Column(db.Enum('male','female','other','prefer_not_to_say', name='therapist_gender'))
    address_line1=db.Column(db.String(150))
    address_line2 =db.Column(db.String(150))
    city =db.Column(db.String(150))
    state_province =db.Column(db.String(150))
    postal_code =db.Column(db.String(150))
    country =db.Column(db.String(150))
    license_authority =db.Column(db.String)
    specialty_summary= db.Column(db.String)
    experience_years=db.Column(db.Integer)
    rating_avg =db.Column(db.Numeric(2,1), default=False)
    verified =db.Column(db.Boolean, default=False )
    profile_photo_url =db.String()
    created_at =db.Column(db.Enum('male','female','other','prefer_not_to_say'))
    address_line1=db.Column(db.String(150))
    address_line2 =db.Column(db.String(150))
    city =db.Column(db.String(150))
    state_province =db.Column(db.String(150))
    postal_code =db.Column(db.String(125))
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))
    is_deleted =db.Column(db.Boolean ,default=False)  
    achieved_at =db.Column(db.DateTime ,default=lambda: datetime.now(timezone.utc))

    #relations
    user_id =db.Column(db.Integer ,db.ForeignKey('users.id', name="fk_therapistprofile_user_id") ,nullable=False)

    #relationship
    user=db.relationship('User', back_populates='therapist_prof', foreign_keys=[user_id])
    therapist_therapie = db.relationship('TherapistTherapies', back_populates='therapist_profile',foreign_keys='TherapistTherapies.therapist_id',cascade='all, delete-orphan')
    child_therapist = db.relationship('ChildTherapist', back_populates='therapist_profile', foreign_keys='ChildTherapist.therapist_id',cascade='all, delete-orphan')
    availability_slots= db.relationship('AvailabilitySlot', back_populates='therapist_profiles', foreign_keys= 'AvailabilitySlot.therapist_id', cascade='all, delete-orphan')
    sessions = db.relationship('Session', back_populates='therapist_profiles', foreign_keys='Session.therapist_id', cascade='all, delete-orphan')
    session_notes = db.relationship('SessionNote', back_populates='therapist_profile', foreign_keys='SessionNote.therapist_id', cascade='all, delete-orphan')
    sessionfeedback = db.relationship('SessionFeedback', back_populates='therapist_profile', foreign_keys='SessionFeedback.therapist_id', cascade='all, delete-orphan')
    supervision_session =db.relationship('SupervisionSession', back_populates='junior_therapist', foreign_keys='SupervisionSession.junior_therapist_id', cascade='all, delete-orphan')
    senior_supervision_session= db.relationship('SupervisionSession', back_populates='senior_therapist', foreign_keys='SupervisionSession.senior_therapist_id', cascade='all, delete-orphan')

    serialize_rules = ('-user.therapist_prof', '-therapist_therapie.therapist_profile', '-child_therapist.therapist_profile', '-availability_slots.therapist_profiles', '-sessions.therapist_profiles', '-session_notes.therapist_profile', '-sessionfeedback.therapist_profile', '-supervision_session.junior_therapist', '-senior_supervision_session.senior_therapist',)

    def __repr__(self):
        return f"<TherapistProfile id={self.id} date_of_birth={self.date_of_birth} gender={self.gender} address_line1='{self.address_line1}' address_line2='{self.address_line2}' city='{self.city}' state_province='{self.state_province}' postal_code='{self.postal_code}' country='{self.country}' license_authority='{self.license_authority}' specialty_summary='{self.specialty_summary}' experience_years={self.experience_years} rating_avg={self.rating_avg} verified={self.verified} profile_photo_url='{self.profile_photo_url}' created_at={self.created_at} address_line1='{self.address_line1}' address_line2='{self.address_line2}' city='{self.city}' state_province='{self.state_province}' postal_code='{self.postal_code}' updated_at={self.updated_at} is_deleted={self.is_deleted} achieved_at={self.achieved_at} user_id={self.user_id}>"