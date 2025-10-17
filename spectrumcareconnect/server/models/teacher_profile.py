from extensions import db
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime, timezone


class TeacherProfile(db.Model,SerializerMixin):
    __tablename__='teacher_profiles'

    id = db.Column(db.Integer,primary_key=True)
    
    date_of_birth = db.Column()
    gender = db.Column(db.Enum('male', 'female','others', 'preffered_not_to_say'))
    address_line1 = db.Column(db.String(130))
    address_line2 =db.Column(db.String(130))
    city = db.Column(db.String)
    state_province =db.Column(db.String)
    postal_code = db.Column(db.String(130))
    country= db.Column(db.String(130))
    license_authority =db.Column(db.String(250))
    specialty_summary =db.Column(db.String())
    experience_years =db.Column(db.Integer)
    rating_avg=db.Column(db.Integer, decimal(10,1), max(5))
    verified =db.Columne(db.Boolean, default=False)
    profile_photo_url= db.Column(db.String(130))
    created_at =db.Column(db.DateTime, default= datetime.now(timezone.utc))
    updated_at =db.Column(db.Datetime, default=datetime.now(timezone.utc))
    is_deleted =db.Column(db.Boolean, default=False) 
    archived_at =db.Column(db.Datetime, default=datetime.now(timezone.utc))

    #relations
    user_id =db.Column(db.Integer, db.ForeignKey('teacher_profiles.id'), nullable=False, unique=True)

    #relationship
    user= db.relationship('User', back_populates='techer_prof', foreign_keys=[user_id])
    school_report_share = db.relationship('SchoolReportShare', back_populates='teacher_profile', foreign_keys='SchoolReportShare.teacher_id', cascade='all, delete-orphan')

