from extensions import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime,timezone

class GroupMember(db.Model, SerializerMixin):
    __tablename__ = 'group_members'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    group_id = db.Column(db.Integer, db.ForeignKey('support_groups.id'))
    joined_at  = db.Column(db.Datetime, default=datetime.now(timezone.utc))
    