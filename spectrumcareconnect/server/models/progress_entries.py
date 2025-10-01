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
    





    child_id = db.Column(db.Integer, db.ForeignKey('child_profiles.id'), nullable=False)
    metric_id = db.Column(db.Integer, db.ForeignKey('progress_metrics.id'))
    session_id = db.Column(db.Integer, db.ForeignKey('sessions.id'))
