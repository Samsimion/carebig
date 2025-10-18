from extensions import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime, timezone

class SupportGroup(db.Model, SerializerMixin):
    __tablename__ = 'support_groups'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description= db.Column(db.Text)
    created_at = db.Column(db.Datetime, default=datetime.now(timezone.utc))
    


    # relationships
    group_members = db.relationship('GroupMember', back_populates='support_groups', foreign_keys='GroupMember.support_group_id', cascade='all, delete-orphan')
    group_posts = db.relationship('GroupPost', back_populates='support_groups', foreign_keys='GroupPost.support_group_id', cascade='all, delete-orphan')
    group_events = db.relationship('GroupEvent', back_populates='support_groups', foreign_keys='GroupEvent.support_group_id', cascade='all, delete-orphan')
    group_report = db.relationship('GroupReport', back_populates='support_group', foreign_keys='GroupReport.support_group_id', cascade='all, delete-orphan' )
    group_ban = db.relationship('GroupBan',back_populates='support_group', foreign_keys='GroupBan.support_group_id', cascade='all, delete-orphan')
    group_setting = db.relationship('GroupSetting', back_populates='support_group', foreign_keys='GroupSetting.support_group_id', cascade='all, delete-orphan' )
    group_setting = db.relationship('GroupRole', back_populates='support_group', foreign_keys='GroupRole.support_group_id', cascade='all, delete-orphan' )

    serialize_rules =('-group_members.support_groups','-group_posts.support_groups', '-group_events.support_groups', '-group_report.support_group','-group_ban.support_group', '-group_setting.support_group', '-group_setting.support_group',)

    def __repr__(self):
        return f"<SupportGroup id={self.id} name='{self.name}' description='{self.description}' created_at={self.created_at}>"