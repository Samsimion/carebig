from extensions import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime, timezone

class Notification(db.Model, SerializerMixin):
    __tablename__ ='notifications'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Enum('session_booked','session_cancelled','goal_achieved','report_shared','general'))
    message = db.Column(db.Text)
    is_read = db.Column(db.Boolean, default=False)
    related_entity_type = db.Column(db.String)
    created_at = datetime.now(db.Datetime, default=datetime.now(timezone.utc))

    related_entity_id =db.Column(db.Integer, db.ForeignKey())



    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))