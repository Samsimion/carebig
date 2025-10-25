from extensions import db
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime, timezone

class Condition(db.Model, SerializerMixin):
    __tablename__= 'conditions'

    id =db.Column(db.Integer,primary_key=True, nullable=False )
    name= db.Column(db.String)
    code_icd10 =db.Column(db.String)
    
    code_icd = db.Column(db.String)
    description = db.Column(db.Text)
    severity_level = db.Column(db.Enum('mild','moderate','severe',name='severity_level'))
    common_therapies= db.Column(db.Text)
    is_active = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc) )
    updated_at=db.Column(db.DateTime ,default=lambda: datetime.now(timezone.utc))
    is_deleted= db.Column(db.Boolean, default=False)
    archived_at =db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    #relation
    category_id =db.Column(db.Integer, db.ForeignKey('condition_categories.id') ,nullable=False )

    #relationships
    condition_category = db.relationship('ConditionCategory', back_populates='condition', foreign_keys= [category_id])
    child_profile = db.relationship('ChildProfile', back_populates='condition', foreign_keys= 'ChildProfile.primary_diagnosis_id' ,cascade='all, delete-orphan')
    therapytype_condition = db.relationship('TherapytypeCondition', back_populates='condition', foreign_keys='TherapytypeCondition.condition_id', cascade='all, delete-orphan')
    session = db.relationship('Session', back_populates='conditions',foreign_keys='Session.condition_id' )
    progress_metrics = db.relationship('ProgressMetric', back_populates='condition' ,foreign_keys='ProgressMetric.condition_id', cascade='all, delete-orphan')
    medical_history = db.relationship('MedicalHistory', back_populates='condition', foreign_keys='MedicalHistory.condition_id', cascade='all, delete-orphan' )

    serialize_rules= ('-condition_category.condition','-child_profile.condition','-therapytype_condition.condition','-session.conditions','-progress_metrics.condition','-medical_history.condition',)

    def __repr__(self):
        return f"<Condition id={self.id} name='{self.name}'  code_icd10='{self.code_icd10}' code_icd='{self.code_icd}' description='{self.description}' severity_level={self.severity_level} common_therapies='{self.common_therapies}' is_active={self.is_active} category_id={self.category_id} >"