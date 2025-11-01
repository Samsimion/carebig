from extensions import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime, timezone

class MedicalReport(db.Model, SerializerMixin):
    __tablename__ ='medical_reports'

    id = db.Column(db.Integer, primary_key=True)
    report_type = db.Column(db.Enum('diagnosis', 'assessment', 'lab_result', 'doctor_note', 'therapy_plan','other', name='medical_report_type'))
    title =db.Column(db.String)
    description = db.Column(db.Text)
    file_url = db.Column(db.String)
    file_hash = db.Column(db.String)
    is_sensitive = db.Column(db.Boolean , default=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default= lambda: datetime.now(timezone.utc))
    is_deleted = db.Column(db.Boolean, default=False)
    archived_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))



    # relations
    child_id = db.Column(db.Integer, db.ForeignKey('child_profiles.id', name="fk_medicalreport_child_id"))
    uploaded_by_user_id = db.Column(db.Integer, db.ForeignKey('users.id', name="fk_medicalreport_uploadedbyuser_id"))

    # relationships
    child_profile = db.relationship('ChildProfile', back_populates='medical_reports', foreign_keys=[child_id])
    uploaded_by_user = db.relationship('User', back_populates='medical_reports', foreign_keys=[uploaded_by_user_id])
    school_report_share = db.relationship('SchoolReportShare', back_populates='medical_report', foreign_keys='SchoolReportShare.medical_report_id', cascade='all, delete-orphan')

    serialize_rules = ('-child_profile.medical_reports','-uploaded_by_user.medical_reports','-school_report_share.medical_report',)

    def __repr__(self):
        return f"<MedicalReport id={self.id} report_type={self.report_type} title={self.title} description={self.description} file_url={self.file_url} file_hash={self.file_hash} is_sensitive={self.is_sensitive} created_at={self.created_at} updated_at={self.updated_at} is_deleted={self.is_deleted} archived_at={self.archived_at} child_id={self.child_id} uploaded_by_user_id={self.uploaded_by_user_id}>"