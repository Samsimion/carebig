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



    user_id =db.Column(db.Integer, db.ForeignKey('users.id'))
    entity_id = db.Column(db.Integer,db.ForeignKey('') )
