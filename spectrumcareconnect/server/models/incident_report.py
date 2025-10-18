from extensions import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime, timezone

class IncidentReport(db.Model, SerializerMixin):
    __tablename__ = 'incident_reports'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text)
    severity = db.Column(db.Enum('low','medium','high','critical'))
    status = db.Column(db.Enum('open','reviewed','resolved','archived'))
    created_at = db.Column(db.Datetime, datetime.now(timezone.utc))
    updated_at = db.Column(db.Datetime, datetime.now(timezone.utc))
    
    

    # relations
    child_id = db.Column(db.Integer, db.ForeignKey('child_profiles.id'))
    reported_by_user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    # relationship
    child_profile = db.relationship('ChildProfile',back_populates='incident_report', foreign_keys=[child_id])
    reported_by = db.relationship('User', back_populates='incident_report', foreign_keys=[reported_by_user_id])

    serialize_rules =('-child_profile.incident_report','reported_by.incident_report',)

    def __repr__(self):
        return f"<IncidentReport id={self.id} description='{self.description}' severity={self.severity} status={self.status} created_at={self.created_at} updated_at={self.updated_at} child_id={self.child_id} reported_by_user_id={self.reported_by_user_id}>"