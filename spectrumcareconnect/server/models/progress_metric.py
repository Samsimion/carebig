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
    created_at = db.Column(db.Datetime, default=datetime.now(timezone.utc))


    therapy_type_id = db.Column(db.Integer, db.ForeignKey('therapy_types.id'))
    condition_id = db.Column(db.Integer, db.ForeignKey('conditions.id'))