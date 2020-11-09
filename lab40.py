# Lab. 4.0

# Question 1

def basketballPoints(three, two, one):
  score = 3*three + 2*two + one
  print('Total Score = '+ str(score))
  return 3*three + 2*two + one

basketballPoints(6, 5, 5)
basketballPoints(0, 2, 2)
basketballPoints(6, 5, 5)

# Question 2

def staircase(n):
    if n == 0:
        print('')
    else:
        for num in range(1,n+1):
            print(str('*') * num)

staircase(0)
staircase(1)
staircase(8)