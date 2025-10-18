from extensions import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime,timezone

class GroupMember(db.Model, SerializerMixin):
    __tablename__ = 'group_members'
    id = db.Column(db.Integer, primary_key=True)
    joined_at  = db.Column(db.Datetime, default=datetime.now(timezone.utc))

    # relations
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    support_group_id = db.Column(db.Integer, db.ForeignKey('support_groups.id'))
    
    # relationships

    users = db.relationship('User', back_populates='group_members',foreign_keys=[user_id])
    support_groups = db.relationship('SupportGroup', back_populates='group_members', foreign_keys=[support_group_id])

    serialize_rules = ('-users.group_members','-support_groups.group_members',)

    def __repr__(self):
        return f"<GroupMember id={self.id} joined_at={self.joined_at} user_id={self.user_id} support_group_id={self.support_group_id}>"