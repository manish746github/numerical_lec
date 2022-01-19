def f(x):
    return (10-3*x*x)
 
def simp(x0,xn,n):
    h = (xn - x0) / n
    
    integration = f(x0) + f(xn)
    
    for i in range(1,n):
        k = x0 + i*h
        
        if i%2 == 0:
            integration = integration + 2 * f(k)
        else:
            integration = integration + 4 * f(k)
    integration = integration * h/3
    
    return integration

print("we are using lower limit =-1;upper_limit=3;n=4")
lower_limit = -1
upper_limit = 3
sub_interval = 4
result = simp(lower_limit, upper_limit, sub_interval)
print("Integration result by Simpson's method is:", (result) )
print("exact result for same set of values is 12")
