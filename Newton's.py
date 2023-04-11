import math

def f(x):
    return x*x*x + 3*x*x - 1

def df(x):
    return 3*x*x + 6*x
    

def Newtonsmethod( po, TOL,No):
    
    i=1
    while i<=No:
        p=po-(f(po)/df(po))
        print(p)
        
        if abs(p-po) < TOL:
            print('Result: ',p)
            break
        else:
            i=i+1
            print(p)
            po=p
            
Newtonsmethod(-2.5,1e-4,50)
