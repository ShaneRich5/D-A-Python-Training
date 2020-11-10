'''
Lab 7.2

1. Make a python script to create a directory in this directory called "data" (use the os module)
2. Copy your least_favorite_movie.txt file into the new data directory (use the shutil module)
3. Copy the entire data directory into a new directory called data2
4. Move the data directory into the data2 directory
5. Remove the data directory

You should find the following documentation helpful:  
**https://docs.python.org/3.4/library/os.html#module-os**  
**https://docs.python.org/3.4/library/shutil.html#shutil.copy**

To run the code below, take the following steps
1. Uncomment 'import lab72' in the 'main.py' file/
2. Uncomment any 'approach' you'd like to test.
3. Click the 'Run' button at the top of the page to try it out.
'''

''' approach #1 '''

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
    


''' approach #2 '''

import os
import shutil

'''
1. Make a python script to create a directory in this directory called "data" (use the os module)
'''

filename = 'last_movie.txt'
directory_path = os.path.join(os.getcwd(), 'data')

if not os.path.isdir(directory_path):
    os.mkdir(directory_path)
else:
    print(directory_path, 'path already exists!')

source_file = os.path.join(os.getcwd(), filename)
destination_file = os.path.join(directory_path, filename)

'''
2. Copy your last_movie.txt file into the new data directory (use the shutil module)
'''

shutil.copy2(source_file, destination_file)

copied_directory_path = os.path.join(os.getcwd(), 'data2')

'''
3. Copy the entire data directory into a new directory called data2
'''

try:
    os.mkdir(copied_directory_path)
except FileExistsError:
    print(f'{copied_directory_path} already exists!')

'''
4. Move the data directory into the data2 directory
'''

try:
    shutil.copytree(directory_path, copied_directory_path + '/data')
except:
    print('\'data\' dir has already been moved!')

'''
5. Remove the data directory
'''
   
shutil.rmtree(directory_path)


''' approach #2 '''