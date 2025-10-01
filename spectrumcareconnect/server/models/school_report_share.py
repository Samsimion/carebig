from extensions import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime,timezone

class SchoolReportShare(db.Model, SerializerMixin):
    __tablename__ = 'school_report_shares'

    id =db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.Datetime, default=datetime.now(timezone.utc))

    report_id = db.Column(db.Integer, db.ForeignKey('medical_reports.id'))
    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher_profiles.id'))


