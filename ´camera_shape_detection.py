import cv2
import numpy as np
import time
import calendar
import datetime



cap = cv2.VideoCapture(0)

font = cv2.FONT_HERSHEY_SIMPLEX

while True:
    
    _, frame = cap.read()
    #assigning frames of video capture
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #converting captured frame from BGR to HSV
    timestamp_millisecond= time.time()*1000
    
    
    low_H = 0
    low_S = 0
    low_V = 42
    high_H = 180
    high_S = 255
    high_V = 255

    lower_red = np.array([low_H, low_S, low_V])
    upper_red = np.array([high_H, high_S, high_V])
    #defining lower and upper limits of thresholding
    # we achieved above values by manual tuning
    # opencv ranges of HSV  are  H= 0 - 179 , S= 0 - 255 , V= 0 - 255

    mask = cv2.inRange(hsv, lower_red, upper_red)
    #thresholding operation
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
        #It approximates a contour shape to another shape
        x = approx.ravel()[0] 
        # detected shape type text placement 
        y = approx.ravel()[1] 
        #  detected shape type text placement 
        perimeter = cv2.arcLength(cnt,True) # find perimeter
        

        if area > 200:  
        # we consider contour if it has area above 200 pixel*pixel to eliminate small detections
            cv2.drawContours(frame, [approx], 0, (0, 0, 0), 5)

            if len(approx) == 3:  
            #when approx contour's length is 3 we decide it's triangle
                cv2.putText(frame, "triangle " , (x, y), font, 1, (0, 0, 0))
                distance_triangle=(((154*58)/(perimeter/3))*0.2645)
                print("Traingle is detected and distance is = ",distance_triangle , "mm")
                # Above numbers were calculated with focal length , pixel length and real dimention  of shape
                
                
            elif len(approx) == 4:
                cv2.putText(frame, "square", (x, y), font, 1, (0, 0, 0))
                distance_square=(((154*58)/(perimeter/4))*0.2645)
                print("Square is detected and distance is = ",distance_square , "mm")
                
                
            elif len(approx) == 5:
                cv2.putText(frame, "Pentogon", (x, y), font, 1, (0, 0, 0))
                distance_pentogone=(((154*58)/(perimeter/5))*0.2645)
                print("Pentogon is detected and distance is = ",((151*58)/(perimeter/5))*0.2645 , "mm")
                
                
            elif len(approx) == 6:
                cv2.putText(frame, "6angle", (x, y), font, 1, (0, 0, 0))
                distance_hexogone = (((154*58)/(perimeter/6))*0.2645)
                print("Pentogon is detected and distance is = ",distance_pentogone , "mm")
                
                
                
            elif 7 < len(approx) < 100:
                cv2.putText(frame, "Circle", (x, y), font, 1, (0, 0, 0))
                print("Other than our desired shape is detected")
            

    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)
    #displaying monitor and frame
    

    key = cv2.waitKey(1)
    if key == True:  # stopping the capturing operation 
        break

cap.release()
cv2.destroyAllWindows()





