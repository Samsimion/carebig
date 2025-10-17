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
    
    


    child_id = db.Column(db.Integer, db.ForeignKey('child_profiles.id'))
    reported_by = db.Column(db.Integer, db.ForeignKey('users.id'))
