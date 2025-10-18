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
    
    # relaions
    child_id = db.Column(db.Integer, db.ForeignKey('child_profiles.id'))
    session_id = db.Column(db.Integer, db.ForeignKey('sessions.id'))
    
    # relationships
    child_profile = db.relationship('ChildProfile', back_populates='AIanalysis', foreign_keys=[child_id])
    session = db.relationship('Session', back_populates='AIanalysis', foreign_keys=[session_id] )
    
    serialize_rules = ('-child_profile.AIanalysis', '-session.AIanalysis',)

    def __repr__(self):
        return f"<AiAnalysis id={self.id} analysis_type={self.analysis_type} result_json='{self.result_json}' child_id={self.id} session_id={self.session_id}>"