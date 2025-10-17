from extensions import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime,timezone

class Donation(db.Model, SerializerMixin):
    __tablename__ = 'donations'

    id = db.Column(db.Integer, primary_key=True)
    amount_cents = db.Column(db.Integer)
    currency_code = db.Column(db.String)
    status = db.Column(db.Enum('pending','completed','failed'))
    purpose = db.Column(db.Enum('general','child_support','therapy_fund','infrastructure','other'))

    created_at = db.Column(db.Datetime, datetime.now(timezone.utc))

    donor_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    organization_id = db.Column(db.Integer, db.ForeignKey('organizations.id'))
