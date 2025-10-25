from extensions import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime, timezone

class GroupComment(db.Model, SerializerMixin):
    __tablename__='group_comments'

    id= db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    

    # relations
    group_post_id = db.Column(db.Integer, db.ForeignKey('group_posts.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    # relationships
    group_posts = db.relationship('GroupPost', back_populates='group_comments', foreign_keys=[group_post_id])
    users = db.relationship('User', back_populates='group_comments', foreign_keys=[user_id])
    group_reports = db.relationship('GroupReport', back_populates='group_comment', foreign_keys='GroupReport.group_comment_id', cascade='all, delete-orphan')

    serialize_rules = ('-group_posts.group_comments','-users.group_comments','-group_reports.group_comment',)

    def __repr__(self):
        return f"<GroupComment id={self.id} content='{self.content}' created_at={self.created_at} group_post_id={self.group_post_id} user_id={self.user_id}>"