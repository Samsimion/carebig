from extensions import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime, timezone


class AuditLog(db.Model, SerializerMixin):
    __tablename__ = 'audit_logs'

    id = db.Column(db.Integer, primary_key=True)
    action = db.Column(db.String)
    entity_type = db.Column(db.String)
    old_values = db.Column(db.Text)
    new_values = db.Column(db.Text)
    ip_address = db.Column(db.String)
    device_info = db.Column(db.String)
    created_at =db.Column(db.Datetime, default=datetime.now(timezone.utc))


    # relations
    user_id =db.Column(db.Integer, db.ForeignKey('users.id'))
    entity_id = db.Column(db.Integer,db.ForeignKey('users.id') )

    # relationships
    user = db.relationship('User',back_populates='audit_log_user', foreign_keys=[user_id] )
    entity_user = db.relationship('User', back_populates='audit_log_entity', foreign_keys=[entity_id])

