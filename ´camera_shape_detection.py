import cv2
import numpy as np
import time
import datetime
from datetime import datetime


now = datetime.now() # current date and time

cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_COMPLEX

while True:
       
    Distance_triangle=np.array([0])
    Distance_square=np.array([0])
    Distance_pentagone=np.array([0])
    Distance_hexagone=np.array([0])
    #assigning distance (camera to shape ) variables to each shape
    
    
    timestamped_camera_readings = np.ndarray((0,), np.float32)
    #assigning an array to hold multiple timestamped distances
    timestamp_ms= time.time()
    #millisecond timestamping
    
    
    _, frame = cap.read()
    #assigning frames as  captured video
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #converting captured frame from BGR to HSV

    low_H = 0
    low_S = 0
    low_V = 70
    high_H = 255
    high_S = 255
    high_V = 255
    # my  filtering values for shape colors
    # from following link we can filter any interested color
    #  https://docs.opencv.org/3.4/da/d97/tutorial_threshold_inRange.html 

    lower_red = np.array([low_H, low_S, low_V])
    upper_red = np.array([high_H, high_S, high_V])
    ##defining lower and upper limits of thresholding

    mask = cv2.inRange(hsv, lower_red, upper_red)
    #executing thresholding operation and saving result in the name mask
    kernel = np.ones((5, 5), np.uint8)
    #create an array for erode function
    mask = cv2.erode(mask, kernel)
    # doing erode masking
    

    # find  contours in our filtered frame
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    
    
    for cnt in contours[1:]:
    # considering countours from 1 because from practical experiencde whole frame is often considered as a contour
        area = cv2.contourArea(cnt)
        # area of detected contour
        approx = cv2.approxPolyDP(cnt, 0.02*cv2.arcLength(cnt, True), True)
        #It predicts a pixel connected contour to a shape
        x = approx.ravel()[0]
        y = approx.ravel()[1]
        # detected shape type label text placement 
        perimeter = cv2.arcLength(cnt,True)
        # find perimeter
        
        

        if area > 200:
         # we consider contour if it has area above 200 pixel*pixel to eliminate small detections
            cv2.drawContours(frame, [approx], 0, (0, 0, 0), 5)
            #drawing predicted contour in frame 

            if len(approx) == 3:
            #when approx contour's length is 3 we decide it's triangle
                cv2.putText(frame, "triangle " , (x, y), font, 1, (0, 0, 0))
                # displaying name 
                Distance_triangle=(((154*58)/(perimeter/3))*0.2645)
                print("At",timestamp_ms,"timestamp" , "Triangle found in :",Distance_triangle,"cm")
                
                
            elif len(approx) == 4:
                cv2.putText(frame, "square", (x, y), font, 1, (0, 0, 0))                
                Distance_square=(((154*58)/(perimeter/4))*0.2645)
                print("At",timestamp_ms,"timestamp" , "Square found in :" ,Distance_square,"cm")
                
            elif len(approx) == 5:
                cv2.putText(frame, "Pentogon", (x, y), font, 1, (0, 0, 0))                           
                Distance_pentagone=(((154*58)/(perimeter/5))*0.2645)
                print("At",timestamp_ms,"timestamp" , "Pentagone found in :" ,Distance_pentagone,"cm")
                
                
            elif len(approx) == 6:
                cv2.putText(frame, "6angle", (x, y), font, 1, (0, 0, 0))             
                Distance_hexagone=(((154*58)/(perimeter/6))*0.2645)               
                print("At",timestamp_ms,"timestamp" , "Hexogone found in :" ,Distance_hexagone,"cm")
                
                
            elif len(approx) > 6 :
                cv2.putText(frame, "Circle", (x, y), font, 1, (0, 0, 0))
                pass
                
            

    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)
    #displaying mask and Frame
    
    write_fmtt = " ".join("%4.8f" for _ in timestamped_camera_readings)
    timestamped_camera_readings = np.append(float(timestamp_ms),[Distance_triangle , Distance_square , Distance_pentagone , Distance_hexagone])
    write_fmtt += " %.0f"
    #logging format of the results
    
    
    with open("camera reading {}.txt".format(datetime.now().strftime('%d-%m-%Y-%H-%M')), "ab") as ff:
        np.savetxt(ff, np.expand_dims(timestamped_camera_readings, axis=0),fmt='%f')
        
    key = cv2.waitKey(1)
    if key == 0:
        break
    #exiting operation

cap.release()
cv2.destroyAllWindows()
#stopping capture and relising resources 







