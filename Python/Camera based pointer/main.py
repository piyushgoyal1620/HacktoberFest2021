import cv2
import pyautogui

hand_cascade = cv2.CascadeClassifier("face.xml")
cap = cv2.VideoCapture(0)
cam_width  = cap.get(3) 
cam_height = cap.get(4)
width, height = pyautogui.size()

def moveMouse(x, y):
    move_x = (x * width) / cam_width
    move_y = (y * height) / cam_height
    
    pyautogui.moveTo(move_x, move_y)

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    hands = hand_cascade.detectMultiScale(gray, 1.9, 10)
    
    for (x,y,w,h) in hands:
        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        
        moveMouse(cam_width - x, y)
    
    frame = cv2.flip(frame, 1)

    
    cv2.imshow('Move Mouse', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()