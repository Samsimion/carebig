from extensions import db
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime, timezone


class VolunteerAssignment(db.Model, SerializerMixin):
    __tablename__ = 'volunteer_assignments'

    id= db.Column(db.Integer, primary_key=True)
    role_description = db.Column(db.Text)
    start_date = db.Column(db.Datetime)
    end_date=db.Column(db.Datetime)
    created_at= db.Column(db.Datetime, default=datetime.now(timezone.now))
    is_deleted= db.Column(db.Boolean, default=False)
    achieved_at = db.Column(db.Datetime, default=datetime.now(timezone.utc))


    #relations
    volunteer_id = db.Column(db.Integer, db.ForeignKey('volunteer_profiles.id'), nullable=False)
    child_id = db.Column(db.Integer, db.ForeignKey('child_profiles.id'))
    organization_id= db.Column(db.Integer, db.ForeignKey('organizations.id'))


    #relationship
    volunteer_prof_assign=db.relationship('VolunteerProfile', back_populates='volunteer_assignment', foreign_keys=[volunteer_id])
    child_volunteer_assign = db.relationship('ChildProfile', back_populates='Volunteer_Assignment', foreign_keys=[child_id])
    organization_volunteer_assignment =db.relationship('Organization', back_populates='Volunteer_assignment', foreign_keys= [organization_id])

    serialize_rules=('-volunteer_prof_assign.volunteer_assignment','child_volunteer_assign.Volunteer_Assignment','organization_volunteer_assignment.Volunteer_assignment',)

    def __repr__(self):
        return f"<VolunteerAssignment id={self.id} role_description='{self.role_description}' start_date={self.start_date} end_date={self.end_date} created_at={self.created_at} is_deleted={self.is_deleted} achieved_at={self.achieved_at} volunteer_id={self.volunteer_id} child_id={self.child_id} organization_id={self.organization_id}>"