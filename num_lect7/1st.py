import numpy as np
def f(x):
    return x*x - 10
def g(x):
    return 2*x
a = float(input("input any no."))
b=int(input("enter iteration"))
c=1
while(c<=b):
    r=a-f(a)/g(a)
    c=c+1
    a=r

print("the root is",a)
