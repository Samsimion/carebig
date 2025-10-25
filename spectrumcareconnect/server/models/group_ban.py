from extensions import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime, timezone

class GroupBan(db.Model, SerializerMixin):
    __tablename__ = 'group_bans'
    
    id = db.Column(db.Integer, primary_key=True)
    reason = db.Column(db.Text)
    banned_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    
 
    # relations
    support_group_id = db.Column(db.Integer, db.ForeignKey('support_groups.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    banned_by_user_id= db.Column(db.Integer, db.ForeignKey('users.id'))

    # relationships
    support_group = db.relationship('SupportGroup', back_populates='group_bans',foreign_keys=[support_group_id])
    user = db.relationship('User', back_populates= 'group_ban',foreign_keys=[user_id])
    banned_by_user = db.relationship('User', back_populates= 'groupban_by',foreign_keys=[banned_by_user_id])
    
    serialize_rules = ('-support_group.group_bans', '-user.group_ban','-banned_by_user.groupban_by',)

    def __repr__(self):
        return f"<GroupBan id={self.id} reason='{self.reason}' banned_at={self.banned_at} support_group_id={self.support_group_id} user_id={self.user_id} banned_by_user_id={self.banned_by_user_id}>"