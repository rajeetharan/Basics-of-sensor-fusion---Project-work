How to run both programs simultaneously

To run interested python programs simultaneously you should go to the terminal and try the command 
sudo python3 program1.py && sudo python3 program2.py
in our case 
sudo python3 IMU.py && sudo python3 Camera_shape_detection.py




About Python scripts 

a.  IMU.py

Altimu10v5 IMU sensor (https://www.pololu.com/product/2739) is used in this project and it is connected via I2C protocol. 
It is essential to enable i2C ( https://www.raspberrypi-spy.co.uk/2014/11/enabling-the-i2c-interface-on-the-raspberry-pi/ )
and I2C dependencies installed ( if your version is lite )
Following library is used to access the Altimu10v5 IMU sensor https://github.com/SvetoslavKuzmanov/altimu10v5.
It is necessary to install them ( sudo python setup.py make) then ( sudo python setup.py install)
Also to have the dependency files in same directory of the code file.

Following IC are LSM6DS33 3-axis gyroscope , 3-axis accelerometer and LIS3MDL 3-axis magnetometer inside the IMU and utlized in the code.
The timestamp is in millisecond and the fetched readings are exported to a text file named " IMU_Readings.txt "



b. Camera_shape_detection.py

Using Raspberry Pi Camera Module V2 and OPENCV library 
Same edge size shapes ( Triangle , square , pentagon , hexagon ) are deteced and the distance between camera and shape is exported.
The timestamp is in millisecond and the calculated distances are exported to a text file named " camera reading.txt ".
IN this case the calculations are carried out with my own edge length so when ever experiemnting with a different edge length shape it should be replaced in calculation part. 


c.  HSV_filter.py

This program is a sub program in case of using Camera_shape_detection.py in different environments( light intensity level ) or different colors.This programis used to calibrate and find the lower and Upper HSV values to do the thresholding operation of camera and filter our interested colorspace. We can figureout our HSV values and place it in the " Camera_shape_detection.py " low and upper  hsv values.

