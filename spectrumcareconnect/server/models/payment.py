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



    session_id = db.Column(db.Integer, db.ForeignKey('sessions.id'))
    parent_id = db.Column(db.Integer, db.ForeignKey('parent_profiles.id'))
    donor_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    organization_id = db.Column(db.Integer, db.ForeignKey('organizations.id'))