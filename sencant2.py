import math

def f(x):
    return x-0.8-0.2*math.sin(x)

def secantmethod(po,p1,TOL,No):
    
    i=2
    
    qo = f(po)
    q1 = f(p1)
    
    while i <= No:
        p = p1 - q1*(p1-po)/(q1-qo)
        print(p)
        
        if abs(p-p1) < TOL:
            print('Result: ',p)
            break
        else:
            i=i+1
            print(p)
            po=p1
            qo=q1
            p1=p
            q1=f(p)
            
secantmethod(0, math.pi/2,1e-4,50)
    