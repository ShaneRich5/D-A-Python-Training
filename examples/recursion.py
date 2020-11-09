
def count_down(n):
  '''
  Simple count down example
  '''
  if n < 0:
    return

  print(n)
  count_down(n - 1)

# print('count down ====')
# count_down(10)

def factorial(n):
  '''
  Computing factorials recursively
  '''
  if n == 0:
      return 1
  if n == 1:
      return 1
  if n == -1: 
      return -1
  if n > 1:
      return n * factorial(n-1) 
  if n < -1: 
      return n * factorial(n+1)

# print(factorial(5))
