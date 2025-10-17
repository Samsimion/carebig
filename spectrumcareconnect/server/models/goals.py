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


    # relations
    child_id = db.Column(db.Integer, db.ForeignKey('child_profiles.id'))
    progress_metric_id = db.Column(db.Integer, db.ForeignKey('progress_metrics.id'))
    created_by_user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


    # relationships
    child_profile = db.relationship('ChildProfile', back_populates='goals', foreign_keys=[child_id])
    progress_metric = db.relationship('ProgressMetric', back_populates='goals', foreign_keys=[progress_metric_id])
    created_by_user = db.relationship('User', back_populates='goals', foreign_keys=[created_by_user_id])
    achievements = db.relationship('Achievement', back_populates='goal', foreign_keys='Achievement.goal_id', cascade='all, delete-orphan')
