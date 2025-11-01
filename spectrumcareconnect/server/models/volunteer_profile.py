
from extensions import db
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime, timezone


class VolunteerProfile(db.Model, SerializerMixin):
    __tablename__='volunteer_profiles'

  
    id= db.Column(db.Integer, primary_key=True)
    skills = db.Column(db.String)
    availability =db.Column(db.String)
    created_at =db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))
    is_deleted =db.Column(db.Boolean, default=False)
    achived_at= db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))



    #relations
    user_id= db.Column(db.Integer,db.ForeignKey('users.id', name="fk_volunteerprofile_user_id"))


    #relationships
    user=db.relationship('User', back_populates='volunteer_prof', foreign_keys=[user_id])
    volunteer_assignment= db.relationship('VolunteerAssignment', back_populates='volunteer_prof_assign',foreign_keys='VolunteerAssignment.volunteer_id')

    serialize_rules=('user.volunteer_prof','volunteer_assignment.volunteer_prof_assign',)

    def __repr__(self):
        return f"<VolunteerProfile id={self.id} skills='{self.skills}' availability='{self.availability}' created_at={self.created_at} updated_at={self.updated_at} is_deleted={self.is_deleted} achived_at={self.achived_at} user_id={self.user_id}>"