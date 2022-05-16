"""
The flask application package.
"""



from flask import Flask
app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif']

import BasicFlaskTemplate.views
import BasicFlaskTemplate.upload