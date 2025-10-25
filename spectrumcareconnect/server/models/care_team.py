from extensions import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime, timezone

class CareTeam(db.Model, SerializerMixin):
    __tablename__ = 'care_teams'

    id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    end_date = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    
    
    # relations
    child_id = db.Column(db.Integer, db.ForeignKey('child_profiles.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    # relationships
    child_profile = db.relationship('ChildProfile', back_populates='careteam', foreign_keys=[child_id])
    user = db.relationship('User', back_populates='careteam', foreign_keys=[user_id] )
    role = db.relationship('ROle', back_populates='careteam', foreign_keys=[role_id])


    serialize_rules = ('-child_profile.careteam', '-user.careteam',)

    def __repr__(self):
        return f"<CareTeam id={self.id} start_date={self.start_date} end_date={self.end_date} role={self.role} child_id={self.child_id} user_id={self.user_id}>"