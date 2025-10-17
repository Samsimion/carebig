from extensions import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime, timezone

class GroupRole(db.Model, SerializerMixin):
    __tablename__ = 'group_roles'


    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String) # "owner", "moderator", "member"
    assigned_at = db.Column(db.Datetime, default=datetime.now(timezone.now))

    group_id = db.Column(db.Integer, db.ForeignKey('support_groups.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))