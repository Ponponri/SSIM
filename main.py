import numpy as np
import cv2
import matplotlib.pyplot as plt
import argparse

L=255

parser = argparse.ArgumentParser()
parser.add_argument('--input_img0', default = 'ntust_cat.jpg') 
parser.add_argument('--input_img1', default = 'ntust_cat_white.jpg') 
parser.add_argument('--c1', default = 1/np.sqrt(L), type=int)
parser.add_argument('--c2', default = 1/np.sqrt(L), type=int)
args = parser.parse_args()

c1 = args.c1
c2 = args.c2

img0_path = args.input_img0
img1_path = args.input_img1

img0 = cv2.imread(img0_path, 0)
img1 = cv2.imread(img1_path, 0)

# Mean
u0 = np.mean(img0)
u1 = np.mean(img1)

# Variance 0
img0_tmp = np.ones((img0.shape[1],img0.shape[0]),dtype=np.uint8)
img0_tmp = img0_tmp*u0
var0 = np.mean(np.multiply((img0 - img0_tmp), (img0 - img0_tmp)))
print(f'u0:\t{u0}')
print(f'var0:\t{var0}')

# Variance 1
img1_tmp = np.ones((img1.shape[1],img1.shape[0]),dtype=np.uint8)
img1_tmp = img1_tmp*u1
var1 = np.mean(np.multiply((img1 - img1_tmp), (img1 - img1_tmp)))
print(f'u1:\t{u1}')
print(f'var1:\t{var1}')

# Covariance
cov = np.mean(np.multiply((img0 - img0_tmp), (img1 - img1_tmp)))
print(f'cov:\t{cov}')

L=255
c1=1/np.sqrt(L)
c2=1/np.sqrt(L)
ssim0 = ((2*u0*u1 + pow(c1*L,2))*(2*cov + pow(c2*L,2)))/((pow(u0,2)+pow(u1,2)+pow(c1*L,2))*(var0+var1+pow(c2*L,2)))
print(f'ssim:\t{ssim0}')

fig = plt.figure()
plt.suptitle(f'u0: {u0}, var0: {var0}\nu1: {u1}, var1: {var1}\ncovariance: {cov}\nssim: {ssim0}')
plt.subplot(121)
plt.title(img0_path)
plt.imshow(cv2.cvtColor(img0,cv2.COLOR_BGR2RGB))
plt.subplot(122)
plt.title(img1_path)
plt.imshow(cv2.cvtColor(img1,cv2.COLOR_BGR2RGB))
fig.tight_layout()
plt.show()