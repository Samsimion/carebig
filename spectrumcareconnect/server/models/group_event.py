from extensions import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime, timezone

class GroupEvent(db.Model, SerializerMixin):
    __tablename__ = 'group_events'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.Text)
    event_date = db.Column(db.Datetime)
    location = db.Column(db.String)
    created_at = db.Column(db.Datetime, default=datetime.now(timezone.utc))

    # relations
    created_by_user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    support_group_id = db.Column(db.Integer, db.ForeignKey('support_groups.id'))

    # relationships
    created_by_user = db.relationship('User', back_populates='group_events', foreign_keys=[created_by_user_id], uselist=False)
    support_groups = db.relationship('SupportGroup', back_populates='group_events' ,foreign_keys=[support_group_id])

    serialize_rules = ('-created_by_user.group_events', '-support_groups.group_events',)

    def __repr__(self):
        return f"<GroupEvent id={self.id} title='{self.title}' description='{self.description}' event_date={self.event_date} location='{self.location}' created_at={self.created_at} created_by_user_id={self.created_by_user_id} support_group_id={self.support_group_id}>"