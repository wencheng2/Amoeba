
# Handle uploads
from fileinput import filename
from pathlib import Path
import os
from queue import Full
from re import A
#from sqlite3 import SQLITE_SAVEPOINT
from flask import Flask, render_template,redirect, request, url_for, send_from_directory
from BasicFlaskTemplate import app
from werkzeug.utils import secure_filename


ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/uploader', methods = ['POST'])
def upload_image():
	if 'file' not in request.files:
		return redirect(request.url)
	file = request.files['file']
	if file.filename == '':
		return redirect(request.url)
	if file and allowed_file(file.filename):
		fname = secure_filename(file.filename)
		print("Fname:"+fname)
		basedir = os.path.abspath(os.path.dirname(__file__))
		file.save(os.path.join(basedir, app.config['UPLOAD_FOLDER'], fname))
		return render_template("test.html", provided_image=os.path.join(app.config['UPLOAD_FOLDER'], fname))
	else:
		return redirect(request.url)


@app.route('/uploads/<filename>')
def display_image(filename):
	print('display_image filename: ' + filename + "\n")
	return send_from_directory(app.config["UPLOAD_FOLDER"], filename)