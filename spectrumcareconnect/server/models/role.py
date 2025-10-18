from extensions import db
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime, timezone


class Role(db.Model,SerializerMixin):
    __tablename__ = 'roles'

    id= db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(120),nullable=False)
    description = db.Column(db.Text)
    created_at =db.Column(db.DateTime, default=datetime.now(timezone.utc))
    updated_at= db.Column(db.DateTime, default=datetime.now(timezone.utc))
    is_deleted =db.Column(db.Boolean)
    achieved_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))

   
    


    # relationships
    users = db.relationship('User', back_populates='role', foreign_keys='User.role_id')

    serialize_rules =('-users.role')

    def __repr__(self):
        return f"<Role id={self.id} name={self.name} description={self.description} created_at={self.created_at} updated_at={self.updated_at} is_deleted={self.is_deleted} achieved_at={self.achieved_at}>"