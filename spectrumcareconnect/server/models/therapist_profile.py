from extensions import db
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime, timezone


class Therapist_profile(db.Model,SerializerMixin):
    __tablename__ = 'therapist_profiles'

    id= db.Column(db.Integer , primary_key=True)
    user_id =db.Column(db.Integer ,db.ForeignKey('users.id') ,nullable=False)
    date_of_birth= db.Column(db.String)
    gender =db.Column(db.Enum('male','female','other','prefer_not_to_say'))
    address_line1=db.Column(db.String(150))
    address_line2 =db.Column(db.String(150))
    city =db.Column(db.String(150))
    state_province =db.Column(db.String(150))
    postal_code =db.Column(db.String(150))
    country =db.Column(db.String(150))
    license_authority =db.Column(db.String)
    specialty_summary= db.Column(db.String)
    experience_years=db.Column(db.Integer)
    rating_avg =db.Column(decimal(3, 2))
    verified =db.Column(db.Boolean, default=False )
    profile_photo_url =db.String()
    created_at =db.Column(db.Enum('male','female','other','prefer_not_to_say'))
    address_line1=db.Column(db.String(150))
    address_line2 =db.Column(db.String(150))
    city =db.Column(db.String(150))
    state_province =db.Column(db.String(150))
    postal_code =db.Column(db.String(125))
    updated_at =db.Column(db.DateTime ,default=datetime.now(timezone.utc))
    is_deleted =db.Column(db.Boolean ,default=False)  
    archived_at =db.COlumn(db.DateTime ,default=datetime.now(timezone.utc))