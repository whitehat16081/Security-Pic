import cv2

def take_snapshot():
    #start the webcam
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=videoCaptureObject.read()

        #save the image
        cv2.imwrite("NewPicture1.jpg",frame)
        result=False
    
    #stop webcam
    videoCaptureObject.release()
    cv2.destroyAllWindows()

take_snapshot()