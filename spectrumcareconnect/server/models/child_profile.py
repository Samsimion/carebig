from extensions import db
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime , timezone

class ChildProfile(db.Model, SerializerMixin):
    __tablename__='child_profiles'

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String)
    date_of_birth= db.COlumn(db.Datetime)
    gender = db.Column(db.Enum('male', 'female', 'other', 'prefer_not_to_say'))
    profile_photo_url= db.Column(db.String)
    diagnosis_notes= db.Column(db.String)
    support_level =db.Column(db.Enum('level_1', 'level_2', 'level_3'))
    education_setting = db.Column(db.Enum('mainstream', 'special_school', 'home_school', 'none'))
    communication_mode= db.Column(db.Enum('verbal', 'non_verbal', 'aac_device','sign_language','mixed'))
    allergies = db.Column(db.Text)
    interests =db.Column(db.Text)
    medical_notes= db.Column(db.Text)
    created_at =db.Column(db.Datetime, default= datetime.now(timezone.utc))
    updated_at= db.Column(db.Datetime, default= datetime.now)
    is_deleted= db.Column(db.Boolean, default=True)




    primary_diagnosis_id = db.Column(db.Integer, db.ForeignKey('conditions.id', nullable=False))
    organization_id =db.Column(db.Integer, db.ForeignKey('organizations.id'), nullable=False)


    #relationships
    Volunteer_Assignment= db.relationship('VolunteerAssignment', back_populates='child_volunteer_assign', foreign_keys='VolunteerAssignment.child_id')
    condition = db.relationship('Condition', back_populates='child_profile', foreign_keys=[primary_diagnosis_id])
    organization = db.relationship('Organization', back_populates='child_profile', foreign_keys=[organization_id])
    child_therapist = db.relationship('ChildTherapist', back_populates='child_profiles', foreign_keys='ChildTherapist.therapist_id', cascade='all, delete-orphan')
    appointments= db.relationship('Appointment', back_populates='child_profiles', foreign_keys='Appointment.child_id', cascade='all, delete-orphan')
    parent_child_links = db.relationship('ParentChildLink', back_populates='child_profiles', foreign_keys='ParentChildLink.child_id', cascade='all, delete-orphan')
    consent = db.relationship('Consent', back_populates='child_profile', foreign_keys='Consent.child_id', cascade='all, delete-orphan')
    sessions = db.relationship('Session', back_populates='child_profiles', foreign_keys='Session.child_id' , cascade='all, delete-orphan')
    progress_entries = db.relationship('ProgressEntry', back_populates= 'child_profile', foreign_keys='ProgressEntry.child_id', cascade= 'all, delete-orphan')
    goals = db.relationship('Goal', back_populates= 'child_profile', foreign_keys='Goal.child_id', cascade ='all, delete-orphan')
    achievements = db.relationship('Achievement', back_populates='child_profile', foreign_keys='Achievement.child_id', cascade='all, delete-orphan')
    medical_reports = db.relationship('MedicalReport', back_populates='child_profile', foreign_keys= 'ChildProfile.child_id', cascade='all, delete-orphan')
    medical_history = db.relationship('MedicalHistory', back_populates='child_profile', foreign_keys='MedicalHistory.child_id', cascade='all, delete-orphan')
    waitists = db.relationship('Waitlist', back_populates='child_profile', foreign_keys='Waitlist.child_id', cascade='all, delete-orphan')