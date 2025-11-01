from extensions import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime, timezone

class GroupPost(db.Model, SerializerMixin):
    __tablename__ = 'group_posts'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    # relations
    support_group_id = db.Column(db.Integer, db.ForeignKey('support_groups.id', name="fk_grouppost_supportgroup_id"))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', name="fk_grouppost_user_id"))

    # relationships
    support_groups = db.relationship('SupportGroup', back_populates='group_posts', foreign_keys=[support_group_id])
    users = db.relationship('User', back_populates='group_posts', foreign_keys=[user_id])
    group_comments = db.relationship('GroupComment', back_populates='group_posts', foreign_keys='GroupComment.group_post_id', cascade='all, delete-orphan')
    group_report = db.relationship('GroupReport', back_populates='group_post', foreign_keys='GroupReport.group_post_id', cascade='all, delete-orphan')

    serialize_rules =('-support_groups.group_posts','-users.group_posts','-group_comments.group_posts','-group_report.group_post',)

    def __repr__(self):
        return f"<GroupPost id={self.id} content='{self.content}' created_at={self.created_at} support_group_id={self.support_group_id} user_id={self.user_id}>"