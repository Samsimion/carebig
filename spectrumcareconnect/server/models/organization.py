from extensions import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime, timezone

class Organization(db.Model, SerializerMixin):
    __tablename__ ='organizations'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    type = db.Column(db.Enum('school','clinic','ngo','other'))
    address = db.Column(db.Text)
    created_at = db.Column(db.Datetime, default=datetime.now(timezone.utc)) 


    #relations

    #relationships
    Volunteer_assignment = db.relationship('VolunteerAssignment', back_populates='organization_volunteer_assignment', foreign_keys='VolunteerAssignment.organization_id', cascade='all, delete-orphan')
    child_profile = db.relationship('ChildProfile',back_populates='organization', foreign_keys='ChildProfile.organization_id', cascade='all , delete-orphan' )
    payment = db.relationship('Payment', back_populates='organization', foreign_keys='Payment.organization_id', cascade='all, delete-orphan')