from flask import render_template, flash, request, redirect, url_for
from app import app, db
from app.models import Feedbacks
from werkzeug.security import generate_password_hash, check_password_hash
from app.webforms import FeedbackForm


# Create route decorator
@app.route('/')
def index():
    form = FeedbackForm()
    return render_template("index.html", form=form)

@app.route('/feedback', methods=['POST'])
def feedback():
    form = FeedbackForm()
    if form.validate_on_submit():
        feedback = Feedbacks(name=form.name.data, feedback=form.feedback.data)
        db.session.add(feedback)
        db.session.commit()
        flash("Feedback submitted successfully!")
        return redirect(url_for('index'))