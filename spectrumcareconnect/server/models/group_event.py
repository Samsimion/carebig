from extensions import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime, timezone

class GroupEvent(db.Model, SerializerMixin):
    __tablename__ = 'group_events'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.Text)
    event_date = db.Column(db.Datetime)
    location = db.Column(db.String)
    created_at = db.Column(db.Datetime, default=datetime.now(timezone.utc))


    created_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    group_id = db.Column(db.Integer, db.ForeignKey('support_groups.id'))