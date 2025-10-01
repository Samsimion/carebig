from extensions import db
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime, timezone

class Condition(db.Model, SerializerMixin):
    __tablename__= 'conditions'

    id =db.Column(db.Integer,primary_key=True, nullable=False )
    name= db.Column(db.String)
    code_icd10 =db.Column(db.String)
    category_id =db.Column(db.String, db.ForeignKey() ,nullable=False )
    code_icd = db.Column(db.String)
    description = db.Column(db.Text)
    severity_level = db.Column(db.Enum('mild','moderate','severe'))
    common_therapies= db.Column(db.Text)
    is_active = db.COlumn(db.Boolean)
    created_at = db.Column(db.Datetime, default=datetime.now(timezone.utc) )
    updated_at=db.Column(db.Datetime ,default=datetime.now(timezone.utc))
    is_deleted= db.Column(db.boolean, default=False)
    archived_at =db.Column(db.Datetime, default=datetime.now(timezone.utc))