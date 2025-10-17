from extensions import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime, timezone

class ProgressEntry(db.Model,SerializerMixin):
    __tablename__ = 'progress_entries'


    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Decimal)
    notes = db.Column(db.Text)
    recorded_by_user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    recorded_at = db.Column(db.Datetime, default=datetime.now(timezone.utc))
    created_at = db.Column(db.Datetime, default=datetime.now(timezone.utc))
    




    # relations
    child_id = db.Column(db.Integer, db.ForeignKey('child_profiles.id'), nullable=False)
    progress_metric_id = db.Column(db.Integer, db.ForeignKey('progress_metrics.id'))
    session_id = db.Column(db.Integer, db.ForeignKey('sessions.id'))
    
    # relationship
    child_profile = db.relationship('ChildProfile', back_populates='progress_entries', foreign_keys= [child_id])
    progress_metric =db.relationship('ProgressMetric', back_populates='progress_entries', foreign_keys=[progress_metric_id])
    session = db.relationship('Session', back_populates='progress_entries', foreogn_keys=[session_id])