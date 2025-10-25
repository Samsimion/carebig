from extensions import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime, timezone

class Organization(db.Model, SerializerMixin):
    __tablename__ ='organizations'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    types = db.Column(db.Enum('school','clinic','ngo','other', name='type_of_organization'))
    address = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc)) 


    #relations
    #relationships
    volunteer_assignment = db.relationship('VolunteerAssignment', back_populates='organization_volunteer_assignment', foreign_keys='VolunteerAssignment.organization_id', cascade='all, delete-orphan')
    child_profile = db.relationship('ChildProfile',back_populates='organization', foreign_keys='ChildProfile.organization_id', cascade='all , delete-orphan' )
    payment = db.relationship('Payment', back_populates='organization', foreign_keys='Payment.organization_id', cascade='all, delete-orphan')
    user_organizations = db.relationship('UserOrganization', back_populates='organizations', foreign_keys='UserOrganization.organization_id', cascade='all , delete-orphan' )
    donations = db.relationship('Donation', back_populates='organizations', foreign_keys='Donation.organization_id', cascade='all, delete-orphan' )

    serialize_rules= ('-volunteer_assignment.organization_volunteer_assignment','-child_profile.organization','-payment.organization','-user_organizations.organizations','-donations.organizations',)

    def __repr__(self):
        return f"<Organization id={self.id} name='{self.name}' types={self.types} address='{self.address}' created_at={self.created_at}>"