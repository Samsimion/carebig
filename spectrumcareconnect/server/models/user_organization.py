from extensions import db
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime, timezone

class UserOrganization(db.Model, SerializerMixin):
    __tablename__ ='user_organizations'

    id = db.Column(db.Integer, primary_key=True)
    role= db.Column(db.Enum('member','staff','admin'))
    created_at = db.Column(db.Datetime, default=datetime.now(timezone.utc))


    # relations
    user_id= db.Column(db.Integer, db.ForeignKey('users.id'))
    organization_id = db.Column(db.Integer, db.ForeignKey('organizations.id'))
    
    # relationship
    