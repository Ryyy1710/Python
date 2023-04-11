import math

def f(x):
    return (x*x*x + 4*x*x -10)

def Bisection(a,b,TOL,No):
    i=1
    FA = f(a)
    
    while i<= No:
        p=(a+b)/2
        FP=f(p)
        
        if FP==0 or (b-a)/2 < TOL:
            print(p)
            break
        else:
            i=i+1
            print(p)

        if FA*FP > 0:
            a = p
            FA = FP
        else:
            b = p
            print(p)
            
Bisection(1,2,1e-4,50)
            
            
            
        
            
            
        
        
        