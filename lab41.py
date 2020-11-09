def reccursiondef(n):
  if n <= 1:
    return n
  else:
    return(reccursiondef(n-1) + reccursiondef(n-2))


# print(reccursiondef(5))

# Fibonacci sequence - 1, 1, 2, 3, 5, 8
# indexes.           - 0, 1, 2, 3, 4, 5

def fib_with_loops(n):
  '''
  This examples 
  '''
  previous = 1
  current = 1

  if n <= 1:
    return 1

  for i in range(n - 1):
    tmp = current
    current = current + previous
    previous = tmp

  return current

# i = 5
# print (f'value at index [{i}] is {fib_with_loops(i)}')

