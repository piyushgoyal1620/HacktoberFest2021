from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
from imutils.video import VideoStream
import numpy as np
import argparse
import imutils
import time
import cv2
import os

def detect_and_predict_mask(frame, faceNet, maskNet):
    (h,w)=frame.shape[:2]
    blob=cv2.dnn.blobFromImage(frame,1.0,(300,300),(104.0,177.0,123.0))

    faceNet.setInput(blob)
    detections=faceNet.forward()


    faces=[]
    locs=[]
    preds=[]

    for i in range(0,detections.shape[2]):
        confidence=detections[0,0,i,2]

        if(confidence>args["confidence"]):
            box=detections[0,0,i,3:7]*np.array([w,h,w,h])
            (startX, startY, endX, endY)=box.astype("int")
            (startX, startY)=(max(0,startX), max(0,startY))
            (endX,endY)=(min(w-1,endX), min(h-1,endY))


            face=frame[startY:endY, startX:endX]
            face=cv2.cvtColor(face,cv2.COLOR_BGR2RGB)
            face=cv2.resize(face,(224, 224))
            face=img_to_array(face)
            face=preprocess_input(face)
            face=np.expand_dims(face, axis=0)

            faces.append(face)
            locs.append((startX,startY,endX,endY))


    if(len(faces)>0):
        preds=maskNet.predict(faces)

    return (locs, preds)

ap=argparse.ArgumentParser()
ap.add_argument("-f","--face",type=str,default="face_detector", help= "path to face detector model directory")
ap.add_argument("-m","--model",type=str,default="mask_detector.model",help="path to trained face mask detector model")
ap.add_argument("-c","--confidence",type=float,default=0.5, help="minimum probability to filter weak detections")
args=vars(ap.parse_args())


print(" Loading face detector Model .......")
prototxtPath=os.path.sep.join([args["face"],"deploy.prototxt"])
weightsPath=os.path.sep.join([args["face"],"res10_300x300_ssd_iter_140000.caffemodel"])
faceNet=cv2.dnn.readNet(prototxtPath,weightsPath)

print(" Loading face mask detector model.....")
maskNet=load_model(args["model"])

print("Starting video stream....")
vs=VideoStream(src=0).start()
time.sleep(2.0)
print("Opening camera to take real time image")

def color_box():
    if( mask > withoutmask):
        label= "Mask ( you can enter )"
        color = (0,0,255)
    else:
        label=" No mask ( you can not enter "
        color=(0,255,0)


while True:
    frame=vs.read()
    frame=imutils.resize(frame,width=1250)
    (locs,preds)=detect_and_predict_mask(frame, faceNet,maskNet)

    for (box,pred) in zip(locs,preds):

        (startX, startY, endX , endY ) = box

        (mask,withoutMask)=pred
        label="Mask you can enter" if mask > withoutMask else " No mask ( you can not enter "

        color= (0,255,0) if label == " Mask You can enter " else (0,0,255)

        cv2.putText(frame,label,(startX,startY - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.45, color, 2)
        cv2.rectangle(frame,(startX,startY),( endX,endY),color, 2)

    cv2.imshow("frame",frame)
    key=cv2.waitKey(1) & 0xFF
    if(key==ord("q")):
        break
cv2.destroyAllWindows()
vs.stop()
