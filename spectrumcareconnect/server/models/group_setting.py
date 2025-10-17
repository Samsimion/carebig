from extensions import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime, timezone

class GroupSetting(db.Model, SerializerMixin):
    __tablename__ = 'group_settings'

    id = db.Column(db.Integer,primary_key=True)
    is_private = db.Column(db.Boolean, default=False)
    approved_required = db.Column(db.Boolean, default=False)

    group_id = db.Column(db.Integer, db.ForeignKey('support_groups.id'))