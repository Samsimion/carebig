from extensions import db, bycrypt
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
    status = db.Column(db.Enum('active','inactive','suspended'),nullable=False)
    created_at= db.Column(db.DateTime,default=datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    last_login_at= db.Column(db.DateTime,default=datetime.now(timezone.utc))
    is_deleted =db.Column(db.Boolean, default=False)
    archived_at =db.Column(db.DateTime, default=datetime.now(timezone.utc))


    


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
    medical_reports = db.relationship('User', back_populates='uploaded_by_user', foreign_keys='MedicalReport.uploaded_by_user_id', cascade='all, delete-orphan')
    medical_history = db.relationship('MedicalHistory', back_populates='updated_by_user', foreign_keys='MedicalHistory.updated_by_user_id', cascade='all, delete-orphan')
    audit_log_user = db.relationship('AuditLog', back_populates='user', foreign_keys='AuditLog.user_id',cascade='all, delete-orphan' )
    audit_log_entity = db.relationship('AuditLog', back_populates='entity_user', foreign_keys='AuditLog.entity_id', cascade='all, delete-orphan')
    notifications = db.relationship('Notification', back_populates='user', foreign_keys='Notification.user_id', cascade='all, delete-orphan')
    resources = db.relationship('Resource', back_populates='uploaded_by_user', foreign_keys='Resource.uploaded_by_user_id', cascade='all, delete-orphan')

    #password handling property

    @hybrid_property
    def password(self):
        return self._password_hash
    

    @password.setter
    def password(self, plain_password):
        self._password_hash =bycrypt.generate_password_hash(plain_password).decode('utf-8')


    def check_password(self, plain_password):
        return bycrypt.check_password_hash(self._password_hash, plain_password)




