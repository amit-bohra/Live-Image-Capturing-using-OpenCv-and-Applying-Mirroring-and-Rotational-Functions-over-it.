import cv2
v=cv2.VideoCapture(0)
ret,i=v.read()
img=cv2.cvtColor(i,cv2.COLOR_BGR2GRAY)
tmg=img
cv2.imshow('new',img)
while(True):
    key=cv2.waitKey(0)
    if key==ord('a'):
        tmg=tmg[:,-1::-1]
        cv2.imshow('new',tmg)
    elif key==ord('s'):
        tmg=tmg[-1::-1,:]
        cv2.imshow('new',tmg)
    elif key==ord('q'):
        cv2.destroyAllWindows()
        v.release()
        quit()
