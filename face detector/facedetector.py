import cv2  


#file for all the faces that are detected by ai 
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


#choose an image 
#img = cv2.imread('appp.png')


#video capture 
webcam = cv2.VideoCapture(0) 


#forever frames baby 
while True: 

#read the current frame
    successful_frame_read, frame = webcam.read() 
    

#covert to grayscale 
    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#face detect
    face_coordinates = trained_face_data.detectMultiScale(frame) 

#draw rectangles around the face 
    for (x, y, w, h) in face_coordinates:
        from random import randrange
        cv2.rectangle(frame, (x, y), (x+w, y+h), (randrange(256), randrange(256), randrange(256)), 2) 

    cv2.imshow ('Clever Programmer Face Detector' , frame )  
    key = cv2.waitKey(1)

    #stop if S key is pressed
    if key ==83 or key==115:
        break 
### Release the videocapture object 
webcam.release()

####Code Complete 
print("Thanks for using the application BOSS!!!") 
