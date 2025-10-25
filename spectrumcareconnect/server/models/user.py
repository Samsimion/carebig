from extensions import db, bcrypt
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime, timezone

class User(db.Model,SerializerMixin):
    __tablename__= 'users'
    

    id=db.Column(db.Integer, primary_key=True)
    first_name=db.Column(db.String(120), unique=True,nullable=False)
    last_name = db.Column(db.String(120),nullable=False)
    middle_name =db.Column(db.String(120))
    email= db.Column(db.String(120), unique=True,nullable=False)
    _password_hash= db.Column(db.String(255), nullable=False)
    status = db.Column(db.Enum('active','inactive','suspended', name='user_status'),nullable=False)
    created_at= db.Column(db.DateTime,default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    last_login_at= db.Column(db.DateTime,default=lambda: datetime.now(timezone.utc))
    is_deleted =db.Column(db.Boolean, default=False)
    achieved_at =db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))



    


    # relations
    role_id= db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False)
    


    # relationships
    role = db.relationship('Role', back_populates= 'users',foreign_keys=[role_id])
    donor_profile = db.relationship('DonorProfile', back_populates='user', foreign_keys='DonorProfile.user_id', uselist=False, cascade='all, delete-orphan')
    parent_prof =db.relationship('ParentProfile', back_populates='user',foreign_keys= 'ParentProfile.user_id',uselist=False, cascade='all, delete-orphan')
    admin_prof= db.relationship('AdminProfile', back_populates= 'user', foreign_keys= 'AdminProfile.user_id', uselist=False, cascade='all, delete-orphan')
    teacher_prof = db.relationship('TeacherProfile', back_populates='user', foreign_keys='TeacherProfile.user_id',uselist=False, cascade='all, delete-orphan')
    therapist_prof=db.relationship('TherapistProfile',back_populates='user', foreign_keys='TherapistProfile.user_id', uselist=False, cascade='all, delete-orphan')
    volunteer_prof = db.relationship('VolunteerProfile',back_populates='user', foreign_keys='VolunteerProfile.user_id',uselist=False,cascade='all, delete-orphan' )
    appointments = db.relationship('Appointment', back_populates='users', foreign_keys='Appointment.user_id', cascade='all, delete-orphan')
    
    sender_message=db.relationship('Message',back_populates='sender_user', foreign_keys='Message.sender_id', cascade='all, delete-orphan')
    receiver_message= db.relationship('Message',back_populates='receiver_user', foreign_keys='Message.receiver_id', cascade='all, delete-orphan')
    consent = db.relationship('Consent', back_populates='user', foreign_keys='Consent.granted_to_user_id', cascade='all, delete-orphan')
    sessions = db.relationship('Session', back_populates='created_user', foreign_keys='Session.created_by_user_id', cascade='all, delete-orphan')
    goals= db.relationship('Goal', back_populates='created_by_user', foreign_keys='Goal.created_by_user_id', cascade='all, delete-orphan')
    medical_reports = db.relationship('MedicalReport', back_populates='uploaded_by_user', foreign_keys='MedicalReport.uploaded_by_user_id', cascade='all, delete-orphan')
    medical_history = db.relationship('MedicalHistory', back_populates='updated_by_user', foreign_keys='MedicalHistory.updated_by_user_id', cascade='all, delete-orphan')
    audit_log_user = db.relationship('AuditLog', back_populates='user', foreign_keys='AuditLog.user_id',cascade='all, delete-orphan' )
    audit_log_entity = db.relationship('AuditLog', back_populates='entity_user', foreign_keys='AuditLog.entity_id', cascade='all, delete-orphan')
    notifications = db.relationship('Notification', back_populates='user', foreign_keys='Notification.user_id', cascade='all, delete-orphan')
    resources = db.relationship('Resource', back_populates='uploaded_by_user', foreign_keys='Resource.uploaded_by_user_id', cascade='all, delete-orphan')
    user_organization= db.relationship('UserOrganization', back_populates='users', foreign_keys='UserOrganization.user_id', cascade='all, delete-orphan')
    group_members = db.relationship('GroupMember', back_populates='users', foreign_keys='GroupMember.user_id', cascade='all, delete-orphan')
    group_posts = db.relationship('GroupPost', back_populates='users', foreign_keys='GroupPost.user_id', cascade='all, delete-orphan')
    group_comments = db.relationship('GroupComment', back_populates='users', foreign_keys='GroupComment.user_id', cascade='all, delete-orphan')
    group_report = db.relationship('GroupReport', back_populates='reported_by_user', foreign_keys='GroupReport.reported_by_user_id', cascade='all, delete-orphan')
    group_ban = db.relationship('GroupBan', back_populates='user', foreign_keys='GroupBan.user_id', cascade='all, delete-orphan')
    groupban_by = db.relationship('GroupBan', back_populates='banned_by_user', foreign_keys='GroupBan.banned_by_user_id', cascade='all, delete-orphan')
    incident_report = db.relationship('IncidentReport', back_populates='reported_by', foreign_keys='IncidentReport.reported_by_user_id', cascade='all, delete-orphan')
    media_storage = db.relationship('MediaStorage', back_populates='uploaded_by', foreign_keys='MediaStorage.uploaded_by_id', cascade='all, delete-orphan')
    careteam = db.relationship('CareTeam', back_populates='user', foreign_keys='CareTeam.user_id', cascade='all, delete-orphan')
    group_roles = db.relationship('GroupRole', back_populates='users', foreign_keys='GroupRole.user_id', cascade='all, delete-orphan')
    progress_entry=db.relationship('ProgressEntry', back_populates='users', foreign_keys='ProgressEntry.recorded_by_user_id', cascade='all, delete-orphan')

    serialize_rules=('-role.users', '-donor_profile.user','-parent_prof.user','-admin_prof.user','-teacher_prof.user','-therapist_prof.user','-volunteer_prof.user','-appointments.users', '-sender_message.sender_user', '-receiver_message.receiver_user','-consent.user', '-sessions.created_user','-goals.created_by_user','-medical_reports.uploaded_by_user','-medical_history.updated_by_user','-audit_log_user.user','-audit_log_entity.entity_user','-notifications.user','-resources.uploaded_by_user','-user_organization.users','-group_members.users','-group_posts.users','-group_comments.users','-group_report.reported_by_user','-group_ban.user','-groupban_by.banned_by_user','-incident_report.reported_by','-media_storage.uploaded_by','-careteam.user','-group_roles.users',)
    

    #password handling property

    @hybrid_property
    def password(self):
        return self._password_hash
    

    @password.setter
    def password(self, plain_password):
        self._password_hash =bcrypt.generate_password_hash(plain_password).decode('utf-8')


    def check_password(self, plain_password):
        return bcrypt.check_password_hash(self._password_hash, plain_password)
    
    def __repr__(self):
        return f"<User id={self.id} first_name='{self.first_name}'last_name='{self.last_name}' middle_name='{self.middle_name}' email='{self.email}' _password_hash='{self._password_hash}' status={self.status} created_at={self.created_at} updated_at={self.updated_at} last_login_at={self.last_login_at} is_deleted={self.is_deleted} achieved_at={self.achieved_at} role_id={self.role_id}>"
    