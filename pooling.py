import os                                                                       
from multiprocessing import Pool                                                
                                                                                
                                                                                
processes = ('a.py','b.py', 'c.py')                    
                                                                                
def run_process(process):                                                             
    os.system('python3 {}'.format(process))                                       
                                                                                
                                                                                
pool = Pool(processes=3)                                                        
pool.map(run_process, processes)