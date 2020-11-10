'''
1. Create a file in this directory
2. Call the file last_movie.txt
3. Populate the file with the name of the last movie you watched
'''

import os

print(os.getcwd())

last_movie = "Rat Race"
filepath = ("last_movie_lab7.txt")

with open(filepath, 'wt') as file:
  file.write(last_movie)
