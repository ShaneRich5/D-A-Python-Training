# import lab72

import os
import shutil

cwd = os.getcwd()

#1
if os.path.exists(f'{cwd}\data') == False:
    os.mkdir(f'{cwd}\data')
  
#2    
if os.path.isfile(f'{cwd}\data\last_movie.txt') == False: 
    shutil.copy2(f'{cwd}\last_movie.txt'
                     , f'{cwd}\data\last_movie.txt')

#3    
if os.path.exists(f'{cwd}\data2') == False:
    os.mkdir(f'{cwd}\data2')    

#4  
if os.path.exists(f'{cwd}\data2\data') == False:
    shutil.copytree(f'{cwd}\data'
                        , f'{cwd}\data2\data')
  
#5
if os.path.exists(f'{cwd}\data') == True:
    shutil.rmtree(f'{cwd}\data')
    
