from extensions import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime, timezone

class GroupRole(db.Model, SerializerMixin):
    __tablename__ = 'group_roles'


    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String) # "owner", "moderator", "member"
    assigned_at = db.Column(db.Datetime, default=datetime.now(timezone.now))
    
    # relations
    support_group_id = db.Column(db.Integer, db.ForeignKey('support_groups.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    # relationships
    support_group = db.relationship('SupportGroup', back_populates='group_role', foreing_keys=[support_group_id])
    users = db.relationship('User', back_populates='group_roles', foreign_keys=[user_id])

    serialize_rules = ('-support_group.support_group','-users.group_roles',)

    def __repr__(self):
        return f"<GroupRole id={self.id} role={self.role} assigned_at={self.assigned_at} support_group_id={self.support_group_id} user_id={self.user_id}>"