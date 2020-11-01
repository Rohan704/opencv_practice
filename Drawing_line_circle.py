import  cv2
import numpy as np

img = cv2.imread("data/lena.jpg")
black = np.zeros((512,512,3),np.uint8)
print(black)
# cv2.imshow("black", black)
# cv2.waitKey(0)
cv2.line(black, (0,0),(512,512),(255,0,0),thickness=1)
cv2.circle(black,(412,240),10,(255,0,0),thickness=3)
cv2.rectangle(black,(384,0),(510,128),(0,255,0),3)
cv2.ellipse(black,(256,256),(100,50),0,0,180,255,-1)

pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines( black,pts,True,(0,255,255),5)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(black,'OpenCV',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)

cv2.imshow('img',img)
cv2.imshow("black", black)
cv2.waitKey(0)