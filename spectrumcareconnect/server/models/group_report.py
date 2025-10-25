from extensions import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime, timezone

class GroupReport(db.Model, SerializerMixin):
    __tablename__ ='group_reports'
    id = db.Column(db.Integer, primary_key=True)
    reason = db.Column(db.Text)
    status = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    # relations
    support_group_id = db.Column(db.Integer, db.ForeignKey('support_groups.id'))
    reported_by_user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    group_post_id = db.Column(db.Integer, db.ForeignKey('group_posts.id'))
    group_comment_id = db.Column(db.Integer, db.ForeignKey('group_comments.id'))

    # relationships
    support_group = db.relationship('SupportGroup', back_populates='group_report', foreign_keys=[support_group_id])
    reported_by_user = db.relationship('User', back_populates='group_report', foreign_keys=[reported_by_user_id])
    group_post = db.relationship('GroupPost', back_populates='group_report', foreign_keys=[group_post_id])
    group_comment = db.relationship('GroupComment', back_populates='group_report', foreign_keys=[group_comment_id])

    serialize_rules = ('-support_group.group_report','-reported_by_user.group_report','-group_post.group_report','-group_comment.group_report')

    def __repr__(self):
        return f"<GroupReport id={self.id} reason='{self.reason}' status='{self.status}' created_at={self.created_at} support_group_id={self.support_group_id} reported_by_user_id={self.reported_by_user_id} group_post_id={self.group_post_id} group_comment_id={self.group_comment_id}>"