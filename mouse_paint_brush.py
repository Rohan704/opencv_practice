# import cv2
# import  numpy as np
# # img = cv2.imread("lena.jpg")
# # blank = np.zeros((512,512,3), np.uint8)
# # cv2.imshow("blank",blank)
# # cv2.waitKey(0)
#
# events = [i for i in dir(cv2) if 'EVENT' in i]
# print(events)
# drawing = False
# mode =True
# ix , iy = 1,1
#
# # mouse callback function
# def draw_circle(event,x,y,flags,param):
#     global ix , iy , mode, drawing
#
#     if event == cv2.EVENT_LBUTTONDOWN:
#         drawing = True
#         ix,iy  = x,y
#     elif event == cv2.EVENT_MOUSEMOVE:
#         if drawing == True:
#             if mode == True:
#                 cv2.rectangle(img,(ix,iy),(x,y),(0.255,0),-1)
#             else:
#                 cv2.circle(img,(x,y),5,(0,255,0),-1)
#     elif event == cv2.EVENT_LBUTTONUP:
#         drawing = False
#         if mode == True:
#             cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
#         else:
#             cv2.circle(img, (x, y), 5, (0, 0, 255), -1)
#
#
# # Create a black image, a window and bind the function to window
# img = np.zeros((512,512,3), np.uint8)
# cv2.namedWindow('image')
# cv2.setMouseCallback('image',draw_circle)
#
# while(1):
#     cv2.imshow('image',img)
#     k = cv2.waitKey(0) & 0xFF
#     if  k == ord('m'):
#         mode = not mode
#     elif k == ord('q'):
#         break
# cv2.destroyAllWindows()
#
#



import cv2
import numpy as np

# events = [i for i in dir(cv2) if 'EVENT' in i]
# print (events)


for i in dir(cv2):
    if 'EVENT' in i:
        # global events
        events = i

        print([events])



def draw_circle(event, x, y , flasgs, params):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x,y), 100, (255,0,0), -1)


img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow("image")
cv2.setMouseCallback('image', draw_circle)


while(1):
    cv2.imshow('image', img)
    if cv2.waitKey(20)  & 0xFF ==27:
        break
cv2.destroyAllWindows



