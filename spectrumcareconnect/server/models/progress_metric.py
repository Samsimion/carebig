from extensions import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime, timezone


class ProgressMetric(db.Model, SerializerMixin):
    __tablename__ = 'progress_metrics'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.Text)
    measurement_unit = db.Column(db.String)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    # relation
    therapy_type_id = db.Column(db.Integer, db.ForeignKey('therapy_types.id', name="fk_progressmetrics_therapytype_id"))
    condition_id = db.Column(db.Integer, db.ForeignKey('conditions.id', name="fk_progressmetrics_condition_id"))

    # relationship
    therapy_type = db.relationship('TherapyType', back_populates='progress_metrics', foreign_keys=[therapy_type_id])
    condition = db.relationship('Condition', back_populates='progress_metrics', foreign_keys=[condition_id])
    progress_entries = db.relationship('ProgressEntry', back_populates='progress_metric', foreign_keys='ProgressEntry.progress_metric_id', cascade='all, delete-orphan')
    goals = db.relationship('Goal', back_populates='progress_metric', foreign_keys='Goal.progress_metric_id',cascade='all, delete-orphan' )
    

    serialize_rules=('-therapy_type.progress_metrics','-condition.progress_metrics','-progress_entries.progress_metric','-goals.progress_metric',)

    def __repr__(self):
        return f"<ProgressMetric id={self.id} name={self.name} description={self.description} measurement_unit={self.measurement_unit} is_active={self.is_active} created_at={self.created_at} therapy_type_id={self.therapy_type_id} condition_id={self.condition_id}>"
    