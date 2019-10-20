import os                                                                       
from multiprocessing import Pool                                                
                                                                                
                                                                                
processes = ('Camera.py','IMU.py', 'motor_control.py')                    
                                                                                
def run_process(process):                                                             
    os.system('python3 {}'.format(process))                                       
                                                                                
                                                                                
pool = Pool(processes=3)                                                        
pool.map(run_process, processes)
