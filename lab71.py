''' approach #1 '''

filepath = 'last_movie.txt'       

with open(filepath, 'w') as file:
  print(file.write('first line'))    

with open(filepath, 'r') as file:
  print(file.readline())                                                        
with open(filepath, 'a') as file:
  file.write('\n'+'Song')

with open(filepath, 'r') as file:
    print('The last movie I watched is: ' + file.readline())
    print('The last song I listened to is: ' + file.readline())


''' approach #2 '''

import os
cwd = os.getcwd()

last_movie = 'Notting Hill'
last_song  = 'Woodkid - Iron'

filepath = (f'{cwd}\last_movie.txt')

with open(filepath, 'wt') as f:
    f.write(''.join([last_movie,'\n']))
    f.write(last_song)

with open(filepath, 'r') as f:
    lines  = f.readlines()
    movie  = lines[0].strip()
    song   = lines[1]

print(f'The last movie I watched is: {movie}')
print(f'The last song I listened to is: {song}')
