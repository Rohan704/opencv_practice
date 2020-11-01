# import numpy as np
# import cv2
# import matplotlib.pyplot as plt
# img = cv2.imread("lena.jpg", -1)
# print(img)
# cv2.imshow('image', img)
# k = cv2.waitKey(0) & 0xff
#
# if k == 27:
#     cv2.destroyAllWindows()
# elif k == ord('s'):
#     cv2.imwrite('lena_copy.png', img)
#     cv2.destroyAllWindows()
# elif k == ord('m'):
#     plt.imshow(img, cmap='gray', interpolation= 'bicubic')
#     plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
#     plt.show()




# life stream capture image using cammera
import cv2
cap = cv2.VideoCapture(0);
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640, 480))
print(cap.isOpened())

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        print(ret-cap.set(3,320))
        print(ret-cap.set(4,240))
        print(ret)

        # out.write(frame)
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # cv2.imshow('gray', frame)
        imgcanny = cv2.Canny(frame, 100, 200)
        cv2.imshow('canny', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
# out.release()
cv2.destroyAllWindows()
#
# #
#
#
# cap.release()
# cv2.destroyAllWindows()
#



# shape and ressize


# # # img = np.zeros([512, 512, 3], np.uint8)
# img = cv2.line(img , (0, 0), (177, 177), (147, 96, 44), 5)
# #
# img = cv2.arrowedLine(img, (0,255), (255,255), (255, 0, 0), 10)
# img = cv2.rectangle(img, (384, 0), (510, 128), (0, 0, 255), 10)
# font = cv2.FONT_HERSHEY_COMPLEX
# img = cv2.putText(img, 'openCv', (0, 500), font, 4, (0, 255, 255), 10, cv2.LINE_AA)




# import numpy as np
# import cv2
# import matplotlib.pyplot as plt
#
# img = cv2.imread("lena.jpg")
# imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# cv2.imshow("img", img)
# cv2.imshow("hsv", imgHSV)
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('gray', gray)
# plt.imshow(gray,cmap='gray' ,interpolation= 'bicubic',)
# plt.show()
# canny = cv2.Canny(img,100,100)
# cv2.imshow('canny',canny)
# cv2.waitKey(0)
#
import numpy as np
# import cv2
# cap = cv2.VideoCapture(0)
# while(True):
#     ret, frame = cap.read()
#     # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     cv2.imshow('frame',frame)
#     print(frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#     elif cv2.waitKey(1) & 0xFF == ord('c'):
#         canny = cv2.Canny(frame , 100,100)
#         cv2.imshow('canny', canny)
#     elif cv2.waitKey(0) & 0xFF == ord('s'):
#         fourcc = cv2.VideoWriter_fourcc(*'xvid')
#         out = cv2.VideoWriter('output.avi')
# # When everything done, release the capture
# cap.release()
# cv2.destroyAllWindows()


