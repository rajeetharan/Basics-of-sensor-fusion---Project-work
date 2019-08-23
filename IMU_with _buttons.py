from altimu10v5.lsm6ds33 import LSM6DS33
from altimu10v5.lis3mdl import LIS3MDL
from altimu10v5.lps25h import LPS25H
from time import sleep
import calendar
import numpy as np
import time




lsm6ds33 = LSM6DS33()
lsm6ds33.enable()
#enabling accelerometer and gyroscope.

lis3mdl = LIS3MDL()
lis3mdl.enable()
#enabling magnetometer 


     
while True:
    
    timestamped_imu_readings = np.ndarray((0,), np.float32)
    #creating and assigning an array to store readings
    timestamp= time.time()*1000
    #millisecond timestamping
    
    timestamped_imu_readings = np.append(timestamped_imu_readings, lsm6ds33.get_accelerometer_g_forces())
    timestamped_imu_readings = np.append(timestamped_imu_readings, lsm6ds33.get_accelerometer_angles())
    timestamped_imu_readings = np.append(timestamped_imu_readings, lsm6ds33.get_gyroscope_raw())
    timestamped_imu_readings = np.append(timestamped_imu_readings, lis3mdl.get_magnetometer_raw())
    #appending IMU readings to the array
    
    write_fmt = " ".join("%4.8f" for _ in timestamped_imu_readings)
    #writing format of reading's decimal points
    timestamped_imu_readings = np.append(float(timestamp),timestamped_imu_readings)
    #adding readings row
    write_fmt += " %.0f"
    #writing format 
    with open("IMU_Readings.txt", "ab") as f:
        np.savetxt(f, np.expand_dims(timestamped_imu_readings, axis=0),  fmt=write_fmt)
        #saving file
        
        

    sleep(0.8)
        

    

    
    
