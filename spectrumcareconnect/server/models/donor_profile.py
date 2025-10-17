from extensions import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime, timezone

class DonorProfile(db.Model,SerializerMixin):
    __tablename__ = 'donor_profiles'

    id = db.Column(db.Integer, primary_key=True)
    organization_name = db.Column(db.String(120))
    donation_focus_area = db.Column(db.String(100))  # e.g. "Health", "Education"
    total_donations = db.Column(db.Float, default=0.0)
    donations_count = db.Column(db.Integer, default=0)
    bio = db.Column(db.Text)
    joined_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, onupdate=datetime.now(timezone.utc))

 




    # relations
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, unique=True)

    # relationship
    users = db.relationship('User', back_populates='donor_profile', foreign_keys=[user_id])
    payments = db.relationship('Payment',back_populates='donor', foreign_keys='Payment.donor_id', cascade='all, delete-orphan' )