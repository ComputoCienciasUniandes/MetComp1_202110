import numpy as np 

def thefun(x):
    return x**3 - 4*x**2 - 4*x + 16

def bisection(f,a,b): #(a,b)
    c=(a+b)/2.
    prod=f(a)*f(c) # 
    if  prod < 0: # sign(f(a)) != sign(f(m))
        b=c #(a,c)
    elif prod > 0: # sign(f(a)) == sign(f(m))
        a=c #(c,b)
    else:
        a=c
        b=c
    return (a,b) 

def nbisection(f,a,b,numiter):
    for i in range(numiter):
        a,b=bisection(f,a,b)
    return a

roots = np.zeros(3)
roots = nbisection(thefun,-3,-1,100), nbisection(thefun, 1, 3,100), nbisection(thefun,3.5, 5,100)

print(roots)