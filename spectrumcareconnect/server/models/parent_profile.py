from extensions import db
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime, timezone

class ParentProfile(db.Model, SerializerMixin):
    __tablename__= 'parent_profiles'

    id= db.Column(db.Integer, primary_key=True, nullable=False)
    
    date_of_birth = db.Column(db.DateTime)
    gender =db.Column(db.Enum('male', 'female', 'other', 'prefer_not_to_say', name='parent_profile_gender'))
    address_line = db.Column(db.String(130))
    address_line2= db.Column(db.String(130))
    city = db.Column(db.String(130))
    state_province = db.Column(db.String(155))
    postal_code = db.Column(db.String(130))
    country = db.Column(db.String(155))
    preferred_language = db.Column(db.String(120))
    emergency_contact_phone = db.Column(db.String(20),nullable=False)
    occupation = db.Column(db.String(155))
    household_notes=db.Column(db.String())
    created_at= db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at= db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    is_deleted= db.Column(db.Boolean, default= False)
    archived_at =db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))


    #relations
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'),nullable=False , unique=True)

    #relationships
    
    user= db.relationship('User', back_populates= 'parent_prof', foreign_keys=[user_id])
    parent_child_links = db.relationship('ParentChildLink', back_populates='parent_profiles', foreign_keys='ParentChildLink.parent_id', cascade='all, delete-orphan')
    reviews = db.relationship('Review', back_populates='parent_profile', foreign_keys='Review.parent_id', cascade='all, delete-orphan')
    payment = db.relationship('Payment', back_populates='parent_profile', foreign_keys='Payment.parent_id', cascade='all, delete-orphan')
    waitlists = db.relationship('Waitlist', back_populates='parent_profile', foreign_keys='Waitlist.parent_id', cascade='all,  delete-orphan')

    serialize_rules = ('-user.parent_prof', '-parent_child_links.parent_profiles','-reviews.parent_profile','-payment.parent_profile','-waitlists.parent_profile',)

    def __repr__(self):
        return f"<ParentProfile id={self.id} date_of_birth={self.date_of_birth} gender={self.gender} address_line={self.address_line} address_line2={self.address_line2} city={self.city} state_province={self.state_province} postal_code={self.postal_code} country={self.country} preferred_language={self.preferred_language} emergency_contact_phone={self.emergency_contact_phone} occupation={self.occupation} household_notes={self.household_notes} created_at={self.created_at} updated_at={self.updated_at} is_deleted={self.is_deleted} archived_at={self.archived_at} user_id={self.user_id}>"