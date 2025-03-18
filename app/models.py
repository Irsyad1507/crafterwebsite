from datetime import datetime
from app import db

# Create Blog Post Model
class Feedbacks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    feedback = db.Column(db.Text)
    date_submitted = db.Column(db.DateTime, default=datetime.utcnow)