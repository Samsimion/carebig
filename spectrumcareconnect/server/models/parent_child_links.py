from extensions import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime, timezone


class ParentChildLink(db.Model, SerializerMixin):
    __tablename__ = 'parent_child_links'

    id = db.Column(db.Integer, primary_key=True)
    parent_relationship = db.Column(db.Enum('mother','father','guardian','sibling','other'))
    created_at = db.Column(db.Datetime, default= datetime.now(timezone.utc))


    #relations
    parent_id = db.Column(db.Integer, db.ForeignKey('parent_profiles.id'), nullable=False)
    child_id= db.Column(db.Integer, db.ForeignKey('child_profiles.id') ,nullable=False)
    
    #relationships
    child_profiles = db.relationship('ChildProfile', back_populates='parent_child_links', foreign_keys=[child_id])
    parent_profiles = db.relationship('ParentProfile', back_populates='parent_child_links',foreign_keys=[parent_id])

    serialize_rules=('-child_profiles.parent_child_links','-parent_profiles.parent_child_links')

    def __repr__(self):
        return f"<ParentChildLink id={self.id} parent_relationship={self.parent_relationship} created_at={self.created_at} parent_id={self.parent_id} child_id={self.child_id}>"