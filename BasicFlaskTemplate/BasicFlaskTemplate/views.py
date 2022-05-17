"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from BasicFlaskTemplate import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Amoeba',
        year=datetime.now().year,
    )

