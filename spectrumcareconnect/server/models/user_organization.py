from extensions import db
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime, timezone

class UserOrganization(db.Model, SerializerMixin):
    __tablename__ ='user_organizations'

    id = db.Column(db.Integer, primary_key=True)
    role= db.Column(db.Enum('member','staff','admin', name='user_role'))
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))


    # relations
    user_id= db.Column(db.Integer, db.ForeignKey('users.id'))
    organization_id = db.Column(db.Integer, db.ForeignKey('organizations.id'))
    
    # relationship
    users = db.relationship('User', back_populates='user_organization', foreign_keys=[user_id])
    organizations = db.relationship('Organization', back_populates='user_organizations', foreign_keys=[organization_id])

    serialize_rules=('-users.user_organization','-organizations.user_organizations',)

    def __repr__(self):
        return f"<UserOrganization id={self.id} role={self.role} created_at={self.created_at} user_id={self.user_id} organization_id={self.organization_id}>"