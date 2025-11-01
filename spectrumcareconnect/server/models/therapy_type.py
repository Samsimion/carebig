from extensions import db
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime, timezone

class TherapyType(db.Model, SerializerMixin):
    __tablename__ = 'therapy_types'

    id= db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description= db.Column(db.Text)
    session_length_min = db.Column(db.Integer)
    recomendation_frequency = db.Column(db.String)
    delivery_modes= db.Column(db.Text)
    is_active= db.Column(db.Boolean, default=False)
    created_at= db.Column(db.DateTime, default=lambda:  datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))
    
    #relations
    category_id = db.Column(db.Integer, db.ForeignKey('therapy_categories.id', name="fk_therapytype_category_id"))

    #relationship
    therapy_category = db.relationship('TherapyCategory', back_populates= 'therapy_type', foreign_keys= [category_id])
    therapist_therapie  = db.relationship('TherapistTherapies', back_populates='therapy_type', foreign_keys='TherapistTherapies.therapy_type_id',cascade='all, delete-orphan')
    therapytype_condition = db.relationship('TherapytypeCondition', back_populates='therapy_type', foreign_keys='TherapytypeCondition.therapy_type_id',cascade='all, delete-orphan')
    session = db.relationship('Session', back_populates='therapy_type', foreign_keys='Session.therapy_type_id', cascade='all, delete-orphan')
    progress_metrics = db.relationship('ProgressMetric', back_populates='therapy_type', foreign_keys='ProgressMetric.therapy_type_id', cascade='all, delete-orphan')
    
    serialize_rules =('-therapy_category.therapy_type', '-therapist_therapie.therapy_type', '-therapytype_condition.therapy_type', '-session.therapy_type', '-progress_metrics.therapy_type',)

    def __repr__(self):
        return f"<TherapyType id={self.id} name='{self.name}' description='{self.description}' session_length_min={self.session_length_min} recomendation_frequency='{self.recomendation_frequency}' delivery_modes='{self.delivery_modes}' is_active={self.is_active} created_at={self.created_at} updated_at={self.updated_at} category_id={self.category_id}>"