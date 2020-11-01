import cv2
cap = cv2.VideoCapture(0);
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('out.avi',fourcc, 20.0, (640, 480))
print(cap.isOpened())

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        print(ret-cap.set(3,320))
        print(ret-cap.set(4,240))
        print(ret)
        frame = cv2.flip(frame, 0)

        out.write(frame)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('gray', frame)
        # imgcanny = cv2.Canny(frame, 100, 200)
        # cv2.imshow('canny', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
out.release()
cv2.destroyAllWindows()