from collections import Counter
from sklearn.cluster import KMeans
from matplotlib import colors
import matplotlib.pyplot as plt
import numpy as np
import cv2


def start(imagePath, numClusters):
    if numClusters is None:
        numClusters = 5
    
    #pass image into here...
    image = cv2.imread(imagePath)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    modified_image = prep_image(image)
    #output image file
    return color_analysis(modified_image, numClusters)

def rgb_to_hex(rgb_color):
    #print(rgb_color)
    hex_color = "#"
    for i in rgb_color:
        i = int(i)
        hex_color += ("{:02x}".format(i))
    return hex_color


def prep_image(raw_img):
    modified_img = cv2.resize(raw_img, (900, 600), interpolation = cv2.INTER_AREA)
    modified_img = modified_img.reshape(modified_img.shape[0]*modified_img.shape[1], 3)
    
    return modified_img

    

def color_analysis(img, numClusters):
    clf = KMeans(numClusters)
    colorlabel = clf.fit_predict(img)
    center_colors = clf.cluster_centers_

    counts = Counter(colorlabel)
    ordered_colors = [center_colors[i] for i in counts.keys()]
    hex_colors = [rgb_to_hex(ordered_colors[i]) for i in counts.keys()]
    
    #Minimal Pie graph
    plt.pie(counts.values(), colors = hex_colors)
    return plt


def get_percentage(value):
    return 



