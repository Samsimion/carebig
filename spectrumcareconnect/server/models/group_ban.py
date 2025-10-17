from extensions import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime, timezone

class GroupBan(db.Model, SerializerMixin):
    __tablename__ = 'group_bans'
    
    id = db.Column(db.Integer, primary_key=True)
    reason = db.Column(db.Text)
    banned_at = db.Column(db.Datetime, default=datetime.now(timezone.utc))
    


    group_id = db.Column(db.Integer, db.ForeignKey('support_groups.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    banned_by = db.Column(db.Integer, db.ForeignKey('users.id'))