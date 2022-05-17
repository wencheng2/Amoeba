
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
from BasicFlaskTemplate import ImageColorProcessor as ICP
import matplotlib.pyplot as plt

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

		#process the image and display graph
		plt = ICP.start(os.path.join(basedir, app.config['UPLOAD_FOLDER'], fname), 10)
		
		#producedGraph = os.path.join(app.config['UPLOAD_FOLDER'], fname)
		export_name = "graph_"+fname
		plt.savefig(os.path.join(basedir, app.config['UPLOAD_FOLDER'], export_name))
		plt.close()
		#returns to the test page with data.. should make this index?
		return render_template("test.html", generated_graph=os.path.join(app.config['UPLOAD_FOLDER'], export_name), provided_image=os.path.join(app.config['UPLOAD_FOLDER'], fname))
		#return render_template("test.html", generated_graph=os.path.join(app.config['UPLOAD_FOLDER'], export_name))
		#return render_template("test.html", basedir + "export.png")
	else:
		return redirect(request.url)


@app.route('/uploads/<filename>')
def display_image(filename):
	print('display_image filename: ' + filename + "\n")
	return send_from_directory(app.config["UPLOAD_FOLDER"], filename)