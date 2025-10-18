from extensions import db
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime, timezone

class ConditionCategory(db.Model, SerializerMixin):
    __tablename__ = 'condition_categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    desription =db.Column(db.Text)
    created_at= db.Column(db.Datetime, default=datetime.now(timezone.utc))

    updated_at= db.Column(db.Datetime, default=datetime.now(timezone.utc))


    #relation

    #relationship
    condition =db.relationship('Condition', back_populates='condition_category', foreign_keys='Condition.category_id')

    def __repr__(self):
        return f"<ConditionCategory id={self.id} name='{self.name}' desription='{self.desription}'>"