from extensions import db
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime , timezone

class Child_profile(db.Model, SerializerMixin):
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