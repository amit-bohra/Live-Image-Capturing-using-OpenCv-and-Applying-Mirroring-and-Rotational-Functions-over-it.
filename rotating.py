import cv2
import numpy as np
v=cv2.VideoCapture(0)
ret,i=v.read()
img=cv2.cvtColor(i,cv2.COLOR_BGR2GRAY)
tmg=np.array(img)
cv2.imshow('new',img)
while(True):
    key=cv2.waitKey(0)
    if key==ord('a'):
        cv2.imshow('new',img.T)
    elif key==ord('d'):
        cv2.imshow('new',img.T[:,-1::-1])
    elif key==ord('w'):
        tmg=img[0:,:]
        cv2.imshow('new',img)
    elif key==ord('s'):
        cv2.imshow('new',img[-1::-1,:])
    elif key==ord('q'):
        cv2.destroyAllWindows()
        v.release()
        quit()
