from extensions import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime, timezone

class GroupReport(db.Model, SerializerMixin):
    __tablename__ ='group_reports'
    id = db.Column(db.Integer, primary_key=True)
    reason = db.Column(db.Text)
    status = db.Column(db.String)
    created_at = db.Column(db.Datetime, default=datetime.now(timezone.utc))


    group_id = db.Column(db.Integer, db.ForeignKey('support_groups.id'))
    reported_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('group_posts.id'))
    comment_id = db.Column(db.Integer, db.ForeignKey('group_comments.id'))
