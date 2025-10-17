from extensions import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime, timezone

class TherapytypeCondition(db.Model, SerializerMixin):
    __tablename__ ='therapytype_conditions'

    id= db.Column(db.Integer, nullable=False)
    

    effectiveness_level = db.Column(db.Enum('high','moderate','emerging','unknown'))
    notes = db.Column(db.Text)
    created_at = db.Column(db.Datetime, default=datetime.now(timezone.utc))


    #relations
    therapy_type_id =db.Column(db.Integer, db.ForeignKey('therapy_types.id'), nullable=False)
    condition_id =db.Column(db.Integer, db.ForeignKey('conditions.id'), nullable=False)

    #relationship
    therapy_type = db.relationship('TherapyType', back_populates='therapytype_condition', foreign_keys=[therapy_type_id])
    condition = db.relationship('Condition', back_populates='therapytype_condition', foreign_keys=[condition_id])