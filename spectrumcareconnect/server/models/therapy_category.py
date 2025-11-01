from extensions import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime, timezone

class TherapyCategory(db.Model, SerializerMixin):
    __tablename__='therapy_categories' 


    id =db.Column(db.Integer, primary_key=True)
    name =db.Column(db.String(150))
    description= db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc)) 

    #relations

    #relationships
    therapy_type = db.relationship('TherapyType', back_populates='therapy_category', foreign_keys='TherapyType.category_id', cascade='all, delete-orphan')

    serialize_rules =('-therapy_type.therapy_category',)

    def __repr__(self):
        return f"<TherapyCategory id={self.id} name='{self.name}' description='{self.description}' created_at={self.created_at} updated_at={self.updated_at}>"