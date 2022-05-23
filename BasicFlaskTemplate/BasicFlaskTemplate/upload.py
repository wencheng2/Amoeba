
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
import cv2
import matplotlib.pyplot as plt
import numpy as np


#File extensions
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

#upload the image to this service and produce graph result
#images are saved in a local directory (['UPLOAD_FOLDER']) and currently not removed
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
		plt = process_image(os.path.join(basedir, app.config['UPLOAD_FOLDER'], fname))
		export_name = "graph_"+fname
		plt.savefig(os.path.join(basedir, app.config['UPLOAD_FOLDER'], export_name))
		plt.close()

		#returns to the test page with data.. should make this index?
		return render_template("result.html", generated_graph=os.path.join(app.config['UPLOAD_FOLDER'], export_name), provided_image=os.path.join(app.config['UPLOAD_FOLDER'], fname))
	else:
		return redirect(request.url)

@app.route('/uploads/<filename>')
def display_image(filename):
	print('display_image filename: ' + filename + "\n")
	return send_from_directory(app.config["UPLOAD_FOLDER"], filename)


def process_image(path):
	# Reading the image on OpenCV
	img = cv2.imread(path)
	result = img.copy()

	# Convert colour format from BGR to HSV
	image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
 
	# Set range of blue colour in HSV
	lower_blue = np.array([110,100,100])
	upper_blue = np.array([130,255,255])
	# Set blue mask
	mask_blue = cv2.inRange(image, lower_blue, upper_blue)
	result_blue = cv2.bitwise_and(result, result, mask= mask_blue)

	# Set range of green colour in HSV
	lower_green = np.array([50, 100, 100])
	upper_green = np.array([70, 255, 255]) 
	
	# Set green mask
	mask_green = cv2.inRange(image, lower_green, upper_green)
	result_green = cv2.bitwise_and(result, result, mask= mask_green)

	# Set range of red colour in HSV
	lower_red = np.array([-10,100,100])
	upper_red = np.array([10,255,255])
	
	# Set red mask
	mask_red = cv2.inRange(image, lower_red, upper_red)
	result_red = cv2.bitwise_and(result, result, mask= mask_red)

	# Set range of pink colour in HSV
	lower_pink = np.array([131,100,100])
	upper_pink = np.array([160,255,255])
	
	# Set red mask
	mask_pink = cv2.inRange(image, lower_pink, upper_pink)
	result_pink = cv2.bitwise_and(result, result, mask= mask_pink)

	# Set up code to close windows when user hits any key
	cv2.waitKey(0)
	cv2.destroyAllWindows()

	# Count number of white pixels 
	# (each white pixel corresponds to a coloured pixed in a defined range).
	# Then divide by image size to get percentage of pixels 
	# in that specific colour in the original image. 
	blue = cv2.countNonZero(mask_blue)
	green = cv2.countNonZero(mask_green)
	red = cv2.countNonZero(mask_red)
	pink = cv2.countNonZero(mask_pink)
	total_bgr = blue + green + red + pink

	# Calculate % of colour in image
	colorPercentBlue = (blue/total_bgr * 100) 
	colorPercentGreen = (green/total_bgr * 100) 
	colorPercentRed = (red/total_bgr * 100) 

	# Draw up data in an image
	# Creating dataset
	colours = ['Blue', 'Green', 'Red']
	data = [colorPercentBlue, colorPercentGreen, colorPercentRed]

	# Creating plot with bar graph
	plt.figure(figsize = (8, 8))
	fig = plt.bar(colours, data, color = colours, width = 0.4)

	# Annotate bars and label image
	for p in fig.patches:
		plt.annotate(format(p.get_height(), '.1f'), 
					   (p.get_x() + p.get_width() / 2., p.get_height()), 
					   ha = 'center', va = 'center', 
					   xytext = (0, 9), 
					   textcoords = 'offset points')
	plt.xlabel("Colours in Image")
	plt.ylabel("Percentage (%)")
	plt.title("Percentage of Colours")
	return plt