from extensions import db
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime , timezone

class ChildProfile(db.Model, SerializerMixin):
    __tablename__='child_profiles'

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String)
    date_of_birth= db.Column(db.DateTime)
    gender = db.Column(db.Enum('male', 'female', 'other', 'prefer_not_to_say', name='childs_gender'))
    profile_photo_url= db.Column(db.String)
    diagnosis_notes= db.Column(db.String)
    support_level =db.Column(db.Enum('level_1', 'level_2', 'level_3', name='childs_severity_support_level'))
    education_setting = db.Column(db.Enum('mainstream', 'special_school', 'home_school', 'none', name='education_settings'))
    communication_mode= db.Column(db.Enum('verbal', 'non_verbal', 'aac_device','sign_language','mixed', name='communication_method'))
    allergies = db.Column(db.Text)
    interests =db.Column(db.Text)
    medical_notes= db.Column(db.Text)
    created_at =db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at= db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    is_deleted= db.Column(db.Boolean, default=False)




    primary_diagnosis_id = db.Column(db.Integer, db.ForeignKey('conditions.id'), nullable=False)
    organization_id =db.Column(db.Integer, db.ForeignKey('organizations.id'), nullable=False)


    #relationships
    volunteer_assignment= db.relationship('VolunteerAssignment', back_populates='child_volunteer_assign', foreign_keys='VolunteerAssignment.child_id',cascade='all, delete-orphan')
    condition = db.relationship('Condition', back_populates='child_profile', foreign_keys=[primary_diagnosis_id])
    organization = db.relationship('Organization', back_populates='child_profile', foreign_keys=[organization_id])
    child_therapist = db.relationship('ChildTherapist', back_populates='child_profile', foreign_keys='ChildTherapist.child_id', cascade='all, delete-orphan')
    appointments= db.relationship('Appointment', back_populates='child_profiles', foreign_keys='Appointment.child_id', cascade='all, delete-orphan')
    parent_child_links = db.relationship('ParentChildLink', back_populates='child_profiles', foreign_keys='ParentChildLink.child_id', cascade='all, delete-orphan')
    consent = db.relationship('Consent', back_populates='child_profile', foreign_keys='Consent.child_id', cascade='all, delete-orphan')
    sessions = db.relationship('Session', back_populates='child_profiles', foreign_keys='Session.child_id' , cascade='all, delete-orphan')
    progress_entries = db.relationship('ProgressEntry', back_populates= 'child_profile', foreign_keys='ProgressEntry.child_id', cascade= 'all, delete-orphan')
    goals = db.relationship('Goal', back_populates= 'child_profile', foreign_keys='Goal.child_id', cascade ='all, delete-orphan')
    achievements = db.relationship('Achievement', back_populates='child_profile', foreign_keys='Achievement.child_id', cascade='all, delete-orphan')
    medical_reports = db.relationship('MedicalReport', back_populates='child_profile', foreign_keys= 'MedicalReport.child_id', cascade='all, delete-orphan')
    medical_history = db.relationship('MedicalHistory', back_populates='child_profile', foreign_keys='MedicalHistory.child_id', cascade='all, delete-orphan')
    waitlists = db.relationship('Waitlist', back_populates='child_profile', foreign_keys='Waitlist.child_id', cascade='all, delete-orphan')
    incident_report = db.relationship('IncidentReport', back_populates='child_profile', foreign_keys='IncidentReport.child_id', cascade='all, delete-orphan')
    media_storage = db.relationship('MediaStorage', back_populates='child_profile', foreign_keys='MediaStorage.child_id', cascade='all, delete-orphan')
    AIanalysis =  db.relationship('AiAnalysis', back_populates='child_profile', foreign_keys='AiAnalysis.child_id', cascade='all, delete-orphan')
    careteam = db.relationship('CareTeam', back_populates='child_profile', foreign_keys='CareTeam.child_id', cascade='all, delete-orphan')

    serialize_rules =('-volunteer_assignment.child_volunteer_assign', '-condition.child_profile','-organization.child_profile','-child_therapist.child_profile','-appointments.child_profiles','-parent_child_links.child_profiles','-consent.child_profile','-sessions.child_profiles','-progress_entries.child_profile','-goals.child_profile','-achievements.child_profile','-medical_reports.child_profile','-medical_history.child_profile','-waitists.child_profile','-incident_report.child_profile','-media_storage.child_profile','-AIanalysis.child_profile','-careteam.child_profile',)

    def __repr__(self):
        return f"<ChildProfile id={self.id} full_name='{self.full_name}' date_of_birth={self.date_of_birth} gender={self.gender} profile_photo_url='{self.profile_photo_url}' diagnosis_notes='{self.diagnosis_notes}' support_level={self.support_level} education_setting={self.education_setting} communication_mode={self.communication_mode} allergies='{self.allergies}' interests='{self.interests}' medical_notes='{self.medical_notes}' primary_diagnosis_id={self.primary_diagnosis_id} organization_id={self.organization_id} >"