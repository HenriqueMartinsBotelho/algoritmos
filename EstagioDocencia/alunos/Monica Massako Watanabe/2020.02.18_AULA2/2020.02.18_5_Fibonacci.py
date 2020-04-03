import math

def fibonacci(i: int)->int:
  r5 = math.sqrt(5)
  t1= math.pow((1+r5)/2, i)
  t2= math.pow((1-r5)/2, i)

  return math.floor ((t1-t2)/r5)

print (fibonacci(20))