from extensions import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime, timezone


class Message(db.Model, SerializerMixin):
    __tablename__ = 'messages'

    id = db.Column(db.Integer, primary_key=True)
    content =db.Column(db.Text)
    is_read =db.Column(db.Boolean)
    created_at = db.Column(db.Datetime, default=datetime.now(timezone.utc))


    #relations
    sender_id = db.Column(db.Integer , db.ForeignKey('users.id'), nullable=False)
    receiver_id = db.Column(db.Integer, db.ForeignKey('users.id'),nullable=False)
    
    #relationships
    sender_user= db.relationship('User',back_populates='sender_message', foreign_keys=[sender_id])
    receiver_user = db.relationship('User', back_populates='receiver_message', foreign_keys=[receiver_id])
    
    serialize_rules = ('-sender_user.sender_message','-receiver_user.receiver_message',)

    def __repr__(self):
        return f"<Message id={self.id} content={self.content} is_read={self.is_read} created_at={self.created_at} sender_id={self.sender_id} receiver_id={self.receiver_id}>"