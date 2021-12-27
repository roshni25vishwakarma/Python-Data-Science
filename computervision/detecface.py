import cv2

cap = cv2.VideoCapture(0)
classifier = cv2.CascadeClassifier("haarcascade.xml")
while True:
    ret, frame = cap.read()
    faces = classifier.detectMultiScale(frame)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y),(x+w, y+h),(0,0,255),3)
     
    cv2.imshow("my web",frame)
      
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cv2.destroyAllWindows()
cap.release()
 
 