import cv2
import numpy as np

img = cv2.imread('data/souce.jpg', cv2.IMREAD_UNCHANGED)

print('Original Dimensions : ', img.shape)

scale_percent = 30 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
# resize image
resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

print('Resized Dimensions : ', resized.shape)



width1 =len(resized[0])
height1 = len(resized)


empty = np.zeros_like(resized)

red, green , blue = (2,1,0)

reds = resized[:,:,red]
greens = resized[:,:,green]
blues = resized[:,:,blue]

cv2.imshow('red', reds)

cv2.imshow('red', reds)
cv2.imshow('greens', greens)
cv2.waitKey(0)
cv2.destroyAllWindows()
