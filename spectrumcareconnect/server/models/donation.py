from extensions import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime,timezone

class Donation(db.Model, SerializerMixin):
    __tablename__ = 'donations'

    id = db.Column(db.Integer, primary_key=True)
    amount_cents = db.Column(db.Integer, nullable=False)
    currency_code = db.Column(db.String, nullable=False)
    status = db.Column(db.Enum('pending','completed','failed', name='donation_status'))
    purpose = db.Column(db.Enum('general','child_support','therapy_fund','infrastructure','other', name='donation_purpose'))
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))
    created_at = db.Column(db.DateTime, default= lambda: datetime.now(timezone.utc))
    
    # relations
    donor_id = db.Column(db.Integer, db.ForeignKey('donor_profiles.id', name="fk_donation_donor_id"))
    organization_id = db.Column(db.Integer, db.ForeignKey('organizations.id', name="fk_donation_organization_id"))
    

    # relationship
    donors = db.relationship('DonorProfile', back_populates='donations', foreign_keys=[donor_id])
    organizations = db.relationship('Organization', back_populates='donations', foreign_keys=[organization_id])
    
    serialize_rules = ('-donors.donations','-organizations.donations',)

    def __repr__(self):
        return f"<Donation id={self.id} amount_cents={self.amount_cents} currency_code={self.currency_code} status={self.status} purpose={self.purpose} donor_id={self.donor_id} organization_id={self.organization_id}>"