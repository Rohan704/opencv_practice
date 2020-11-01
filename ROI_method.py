# import cv2
# import sys
#
#
# faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#
# video_capture = cv2.VideoCapture(1)
#
# while True:
#     # Capture frame-by-frame
#     ret, img= video_capture.read()
#
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
#     # faces = faceCascade.detectMultiScale(
#     #     gray,
#     #     scaleFactor=1.1,
#     #     minNeighbors=5,
#     #     minSize=(30, 30),
#     #     flags=cv2.CASCADE_SCALE_IMAGE
#     # )
#
#     # Draw a rectangle around the faces
#     for (x, y, w, h) in faces:
#         cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
#
#     # Display the resulting frame
#     cv2.imshow('Video', frame)
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# # When everything is done, release the capture
# video_capture.release()
# cv2.destroyAllWindows()


import cv2 as cv
face = cv.CascadeClassifier('data/haarcascade_frontalface_default.xml')
eye = cv.CascadeClassifier('data/haarcascade_eye.xml')
cap = cv.VideoCapture(0)

while True:
    ret, img= cap.read()
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    faces = face.detectMultiScale(gray, 1.3,5)
    for (x,y,w,h) in faces:
        cv.rectangle(img,(x,y),(x+h,y+w),(255,0,0),2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]
        eyes = eye.detectMultiScale(roi_gray)
        for (ex,ey,eh,ew) in eyes:
            cv.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    cv.imshow('img', img)
    cv.imshow('gray',gray)
    k = cv.waitKey(30) & 0xff
    if k == ord('q'):
        break

cap.release()
cv.destroyAllWindows()