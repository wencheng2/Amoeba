
# Handle uploads
from pathlib import Path
import os
#from sqlite3 import SQLITE_SAVEPOINT
from flask import Flask, render_template,redirect, request, url_for
from BasicFlaskTemplate import app
from werkzeug.utils import secure_filename

@app.route('/uploader', methods = ['POST'])
def upload_file():

    # Create a directory in a known location to save files to.
    uploads_dir = os.path.join(app.instance_path, 'uploads')
    os.makedirs(uploads_dir, mode=511, exist_ok=True)

    if request.method == 'POST':
      f = request.files['file']
      if (f.filename != ""):
          f.save(os.path.join(uploads_dir, secure_filename(f.filename)))
          return "File name: " + f.filename + " size"
    return redirect(url_for('test'))


def processFile():
    print("processFile")




