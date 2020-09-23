import cv2
flag = [i for i in dir(cv2) if i.startswith('COLOR_')]
print(flag)

img = cv2.imread('cat.jpeg', flags=cv2.COLOR_BGR2GRAY)
