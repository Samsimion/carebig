from extensions import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime, timezone

class CareTeam(db.Model, SerializerMixin):
    __tablename__ = 'care_teams'

    id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.Datetime, default=datetime.now(timezone.utc))
    end_date = db.Column(db.Datetime)
    created_at = db.Column(db.Datetime, default=datetime.now(timezone.utc))
    role = db.Column(db.Integer, db.Foreignkey('roles.id'))
    child_id = db.Column(db.Integer, db.ForeignKey('child_profiles.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
