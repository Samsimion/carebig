from extensions import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime, timezone


class Goal(db.Model, SerializerMixin):
    __tablename__ = 'goals'
    

    id = db.Column(db.Integer, primary_key=True)
    target_value = db.Column(db.Decimal)
    unit = db.Column(db.Vachar)
    start_date = db.Column(db.Datetime)
    due_date = db.Column(db.Datetime)
    status = db.Column(db.Enum('active', 'achieved', 'missed', 'archived'))
    created_at =db.Column(db.Datetime , default=datetime.now(timezone.utc))



    child_id = db.Column(db.Integer, db.ForeignKey('child_profiles.id'))
    metric_id = db.Column(db.Integer, db.ForeignKey('progress_metrics.id'))
    created_by_user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
