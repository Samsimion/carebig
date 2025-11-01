from extensions import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime, timezone


class Review(db.Model, SerializerMixin):
    __tablename__ = 'reviews'
    __table_args__ = (
        db.CheckConstraint('rating >=1 AND rating <= 5', name='valid_rating_range'),
    )

    id  = db.Column(db.Integer, primary_key= True)
    rating = db.Column(db.Integer)
    comment = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))


    # relations
    session_id= db.Column(db.Integer, db.ForeignKey('sessions.id', name="fk_review_session_id"))
    parent_id= db.Column(db.Integer, db.ForeignKey('parent_profiles.id', name="fk_review_parent_id"))

    # relationship
    session = db.relationship('Session', back_populates='reviews',foreign_keys= [session_id] )
    parent_profile = db.relationship('ParentProfile', back_populates='reviews', foreign_keys=[parent_id])

    serialize_rules =('-session.reviews','-parent_profile.reviews')

    def __repr__(self):
        return f"<Review id={self.id} rating={self.rating} comment={self.comment} created_at={self.created_at} session_id={self.session_id} parent_id={self.parent_id}>"

