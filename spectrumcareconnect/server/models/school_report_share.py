from extensions import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime,timezone

class SchoolReportShare(db.Model, SerializerMixin):
    __tablename__ = 'school_report_shares'

    id =db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    # relations
    medical_report_id = db.Column(db.Integer, db.ForeignKey('medical_reports.id', name="fk_schoolreportshare_medicalreport_id"),nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher_profiles.id', name="fk_schoolreportshare_teacher_id"),nullable=False)

    # relationships
    medical_report = db.relationship('MedicalReport', back_populates='school_report_share', foreign_keys=[medical_report_id])
    teacher_profile = db.relationship('TeacherProfile', back_populates='school_report_share', foreign_keys=[teacher_id])

    serialize_rules=('-medical_report.school_report_share','-teacher_profile.school_report_share',)

    def __repr__(self):
        return f"<SchoolReportShare id={self.id} created_at={self.created_at} medical_report_id={self.medical_report_id} teacher_id={self.teacher_id}>"