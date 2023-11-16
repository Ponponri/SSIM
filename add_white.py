import cv2
import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--input_img', default = 'ntust_cat.jpg') 
parser.add_argument('--output_img', default = 'ntust_cat_white.jpg') 
args = parser.parse_args()

img_path = args.input_img
img0 = cv2.imread(img_path, 0)
img_white = np.ones((img0.shape[1],img0.shape[0]), dtype=np.uint8) * 255

img1 = cv2.addWeighted(img0,0.5,img_white,0.5,0)
cv2.imwrite(args.output_img,img1)