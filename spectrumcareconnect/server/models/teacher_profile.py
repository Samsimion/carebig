from extensions import db
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime, timezone


class TeacherProfile(db.Model,SerializerMixin):
    __tablename__='teacher_profiles'
    __table_args__ = (
        db.CheckConstraint('rating_avg <= 5', name='valid_avg_rating'),
    )

    id = db.Column(db.Integer,primary_key=True)
    
    date_of_birth = db.Column(db.DateTime)
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
    rating_avg=db.Column(db.Numeric(2,1), default=0)
    verified =db.Column(db.Boolean, default=False)
    profile_photo_url= db.Column(db.String(130))
    created_at =db.Column(db.DateTime, default= lambda: datetime.now(timezone.utc))
    updated_at =db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    is_deleted =db.Column(db.Boolean, default=False) 
    achieved_at =db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    #relations
    user_id =db.Column(db.Integer, db.ForeignKey('teacher_profiles.id'), nullable=False, unique=True)

    #relationship
    user= db.relationship('User', back_populates='techer_prof', foreign_keys=[user_id])
    school_report_share = db.relationship('SchoolReportShare', back_populates='teacher_profile', foreign_keys='SchoolReportShare.teacher_id', cascade='all, delete-orphan')

    serialize_rules=('-user.techer_prof','-school_report_share.teacher_profile',)

    def __repr__(self):
        return f"<TeacherProfile id={self.id} date_of_birth={self.date_of_birth} gender={self.gender} address_line1='{self.address_line1}' address_line2='{self.address_line2}' city='{self.city}' state_province='{self.state_province}' postal_code='{self.postal_code}' country='{self.country}' license_authority='{self.license_authority}' specialty_summary='{self.specialty_summary}' experience_years={self.experience_years} rating_avg={self.rating_avg} verified={self.verified} profile_photo_url='{self.profile_photo_url}' created_at={self.created_at} updated_at={self.updated_at} is_deleted={self.is_deleted} achieved_at={self.achieved_at} user_id={self.user_id}>"