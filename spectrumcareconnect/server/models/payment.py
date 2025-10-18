from extensions import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime, timezone

class Payment(db.Model, SerializerMixin):
    __tablename__ = 'payments'

    id = db.Column(db.Integer, primary_key=True)
    amount_cents = db.Column(db.Integer)
    currency_code = db.Column(db.String)
    status = db.Column(db.Enum('pending','completed','failed','refunded'))
    expiry_date = db.Column(db.Datetime)
    Payment_method = db.Column(db.Enum('credit_card','paypal','bank_transfer','cash'))
    transaction_reference = db.Column(db.String)
    created_at = db.Column(db.Datetime, default=datetime.now(timezone.utc))
    updated_at = db.Column(db.Datetime, default=datetime.now(timezone.utc))


    # relations
    session_id = db.Column(db.Integer, db.ForeignKey('sessions.id'))
    parent_id = db.Column(db.Integer, db.ForeignKey('parent_profiles.id'))
    donor_id = db.Column(db.Integer, db.ForeignKey('donor_profiles.id'))
    organization_id = db.Column(db.Integer, db.ForeignKey('organizations.id'))

    # relationships
    session = db.relationship('Session', back_populates='payment', foreign_keys=[session_id] )
    parent_profile = db.relationship('ParentProfile', back_populates='payment', foreign_keys=[parent_id])
    donor = db.relationship('DonorProfile', back_populates='payments', foreign_keys=[donor_id])
    organization = db.relationship('Organization', back_populates='payment', foreign_keys=[organization_id])
    
    serialize_rules = ('-session.payment','-parent_profile.payment','-donor.payments','-organization.payment')

    def __repr__(self):
        return f"<Payment id={self.id} amount_cents={self.amount_cents} currency_code={self.currency_code} status={self.status} expiry_date={self.expiry_date} Payment_method={self.Payment_method} transaction_reference={self.transaction_reference} created_at={self.created_at} updated_at={self.updated_at} session_id={self.session_id} parent_id={self.parent_id} donor_id={self.donor_id} organization_id={self.organization_id} >"