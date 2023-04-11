import math

def f(x):
    return  x - 0.8 - 0.2*math.sin(x)

def df(x):
    return 1 - 0.2*math.cos(x)
    

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
            
Newtonsmethod(0 ,1e-4,20)
