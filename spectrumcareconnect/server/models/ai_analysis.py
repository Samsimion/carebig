from extensions import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime, timezone

class AiAnalysis(db.Model, SerializerMixin):
    __tablename__ ='AI_analysis'

    id = db.Column(db.Integer, primary_key=True)
    analysis_type = db.Column(db.Enum('progress_trend','risk_alert','recommendation'))
    result_json = db.Column(db.Text)
    created_at = db.Column(db.Datetime, default=datetime.now(timezone.utc))

    child_id = db.Column(db.Integer, db.ForeignKey('child_profiles.id'))
    session_id = db.Column(db.Integer, db.ForeignKey('sessions.id'))

