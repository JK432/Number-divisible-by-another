# Write a Python function to find whether a number is completely divisible by another number
def div(a,b):
  if(a%b==0):
    print("%d is completely divisible by %d"%(a,b))
  else:
    print("%d is not completely divisible by %d"%(a,b))

x=int(input())
y=int(input())
div(x,y)