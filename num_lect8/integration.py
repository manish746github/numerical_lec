def f(x):
   return (10 - x**2)
A = -2
B = 2
N = int(input())
H = (B-A)/N
sum = 0.5*( f(A) + f(B) )
for i in range (1,N-1):
    x=A+i*H
    sum = sum + f(x)
sum = H*sum
print("value of integral =",sum)

