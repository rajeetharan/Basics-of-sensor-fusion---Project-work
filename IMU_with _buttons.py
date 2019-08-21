from altimu10v5.lsm6ds33 import LSM6DS33
from altimu10v5.lis3mdl import LIS3MDL
from altimu10v5.lps25h import LPS25H
import calendar
import numpy as np
import time
import os
from gpiozero import Button
import RPi.GPIO as GPIO
from signal import pause



    
button_start = Button (26)
button_end = Button (13)


lsm6ds33 = LSM6DS33()
lsm6ds33.enable()

lis3mdl = LIS3MDL()
lis3mdl.enable()

lps25h = LPS25H
lis3mdl.enable()


if os.path.exists("IMU_Sensor_Readings.txt"):
  os.remove("IMU_Sensor_Readings.txt")
else:
  pass



     
def do_imu():
    timestamped_sensor_readings = np.ndarray((0,), np.float32)
    timestamp = calendar.timegm(time.gmtime())
    timestamped_sensor_readings = np.append(timestamped_sensor_readings, lsm6ds33.get_accelerometer_g_forces())
    timestamped_sensor_readings = np.append(timestamped_sensor_readings, lsm6ds33.get_accelerometer_angles())
    timestamped_sensor_readings = np.append(timestamped_sensor_readings, lsm6ds33.get_gyroscope_raw())
    write_fmt = " ".join("%4.2f" for _ in timestamped_sensor_readings)
    timestamped_sensor_readings = np.append(float(timestamp),timestamped_sensor_readings)
    write_fmt += " %.0f"
    with open("IMU_Sensor_Readings.txt", "ab") as f:
        np.savetxt(f, np.expand_dims(timestamped_sensor_readings, axis=0),  fmt=write_fmt)

    sleep(0.2)




try:
    while True:
        if button_start.is_pressed :
            print("Button_start pressed ")
            do_imu()
        else:
            print("Start not pressed ")
            
        if button_end.is_pressed :
            print("closing program")
            exit()
        
        else:
            pass
        

finally:                     
    GPIO.cleanup() 

pause()     

    
    
