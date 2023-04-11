
import math

def G_p(x):
    return math.cos(x)

def Fixed_Point(P0,TOL,N0):
    i=1
    
    while i<=N0:
        p=G_p(P0)
        
        if abs(p-P0)<TOL:
            print(p)
            break
        else:
            i=i+1
            print(p)
            P0=p

Fixed_Point(0,1e-5,50)
 
    