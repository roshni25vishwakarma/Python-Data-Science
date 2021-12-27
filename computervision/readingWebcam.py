import cv2

#img = cv2.imread("shin.png")

#print(img)

#cv2.imshow("my window",img)
#cv2.waitKey(5000)

cap = cv2.VideoCapture(0)
classifier = cv2.CascadeClassifier("haarcascade.xml")
while True:
    ret, frame = cap.read()
    faces = classifier.detecMultiscale(frame)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y),(x+W, y+h),(0,0,255)
         cv2.imshow("my web",frame)
      
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cv2.destroyAllWindows()
cap.release()
