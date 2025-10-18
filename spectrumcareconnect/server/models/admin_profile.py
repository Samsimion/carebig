
from extensions import db
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime, timezone

class AdminProfile(db.Model, SerializerMixin):
    __tablename__= 'admin_profiles'

    id =db.Column(db.Integer, primary_key=True)
    job_title = db.Column(db.String)          #System Admin, Data Manager
    department=  db.Column(db.String) #optional, e.g., IT, Support
    permissions_level =db.Column(db.Enum('super_admin', 'manager', 'support') )# can refine later
    notes = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    updated_at =db.Column(db.DateTime, default=datetime.now(timezone.utc))
    is_deleted = db.Column(db.Boolean, default=False) 
    archived_at =db.Column(db.DateTime, default=datetime.now(timezone.utc))


    #relations 
    user_id =db.Column(db.Integer, db.ForeignKey('users.id') , nullable=False, unique=True) 



    #relationships

    user= db.relationship('User', back_populates='admin_prof', foreign_keys=[user_id])
    
    serialize_rules = ('-user.admin_prof',)

    def __repr__(self):
        return f"<AdminProfile id={self.id} job_title='{self.job_title}' department='{self.department}' permissions_level='{self.permissions_level}' notes='{self.notes}' user_id='{self.user_id}' >"
