from extensions import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime, timezone

class Notification(db.Model, SerializerMixin):
    __tablename__ ='notifications'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Enum('session_booked','session_cancelled','goal_achieved','payment_received','donation_received','report_shared','general', name='notification_type'))
    message = db.Column(db.Text)
    is_read = db.Column(db.Boolean, default=False)
    related_entity_type = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    priority = db.Column(db.Enum('low', 'medium', 'high', name='notification_priority'))
    link_url = db.Column(db.String)

    related_entity_id = db.Column(db.Integer, nullable=True)



    # relations
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', name="fk_notification_user_id"))

    #relationship
    user = db.relationship('User', back_populates='notifications', foreign_keys=[user_id] )

    serialize_rules = ('-user.notifications',)

    def __repr__(self):
        return f"<Notification id={self.id} type={self.type} message={self.message} is_read={self.is_read} related_entity_type={self.related_entity_type} created_at={self.created_at} related_entity_id={self.related_entity_id} user_id={self.user_id} >"