from extensions import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime, timezone

class GroupComment(db.Model, SerializerMixin):
    __tablename__='group_comments'

    id= db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('group_posts.id'))
    user_id = db.Column(db.Integer, db.Foreigney('users.id'))
    created_at = db.Column(db.Datetime, default=datetime.now(timezone.utc))
