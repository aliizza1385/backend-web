from initialize import db
from datetime import datetime


class Categori(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, unique=True, nullable=False)
    parent_category_id = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    products = db.relationship("Product", backref="categiri",cascade='all, delete-orphan', lazy=True)

    def __repr__(self):
        return '<Categori %r>' % self.id
    