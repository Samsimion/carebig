from extensions import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime, timezone


class Achievement( db.Model, SerializerMixin):
    __tablename__ = 'achievements'


    id = db.Column(db.Integer, primary_key=True)
    badge_name = db.Column(db.String)
    description = db.Column(db.Text)
    earned_at = db.Column(db.Datetime, default=datetime.now(timezone.utc))
    created_at = db.Column(db.Datetime, default=datetime.now(timezone.utc))


    child_id =db.Column(db.Integer, db.ForeignKey('child_profiles.id'))
    goal_id = db.Column(db.Integer, db.ForeignKey('goals.id'))
