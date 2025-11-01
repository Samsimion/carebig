from extensions import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime, timezone

class GroupSetting(db.Model, SerializerMixin):
    __tablename__ = 'group_settings'

    id = db.Column(db.Integer,primary_key=True)
    is_private = db.Column(db.Boolean, default=False)
    approved_required = db.Column(db.Boolean, default=False)

    # relations
    support_group_id = db.Column(db.Integer, db.ForeignKey('support_groups.id', name="fk_groupsetting_supportgroup_id"))

    # relationships
    support_group = db.relationship('SupportGroup', back_populates='group_setting', foreign_keys=[support_group_id])

    serialize_rules= ('-support_group.group_setting',)

    def __repr__(self):
        return f"<GroupSetting id={self.id} is_private={self.is_private} approved_required={self.approved_required} support_group_id={self.support_group_id} >"