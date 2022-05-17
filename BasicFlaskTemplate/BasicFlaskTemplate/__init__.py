"""
The flask application package.
"""

from flask import Flask

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['png', 'jpg', 'jpeg']

import BasicFlaskTemplate.views
import BasicFlaskTemplate.upload