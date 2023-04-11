import math
import numpy

def f(x):
    return x-0.8-0.2*math.sin(x)

def regufalsi_method(po, p1, TOL, No):    
    while numpy.sign(f(po)*f(p1)) > 0:
        print("Nhap lai")
        po = float(input("Nhap po: "))
        p1 = float(input("Nhap p1: "))
    if numpy.sign(f(po)) > 0:
        i = 2
        qo = f(po)
        q1 = f(p1)
        while i <= No:
            print(p)
            p = p1 - q1*(p1-po)/(q1-qo)
            if abs(p - p1) < TOL:
                print("Result: ",p)
                break
            i = i + 1
            if numpy.sign(f(p)) > 0:
                po = p1
                qo=q1
                p1 = p
                q1 = f(p)
            elif numpy.sign(f(p)) < 0:
                p1 = p
                q1 = f(p)
            else:
                print("ERROR")

    if numpy.sign(f(po)) < 0:
        i = 2
        qo = f(po)
        q1 = f(p1)
        while i <= No:
            p = p1 - q1*(p1-po)/(q1-qo)
            print(p)
            if abs(p - p1) < TOL:
                print("Result: ",p)
                break
            i = i + 1
            if numpy.sign(f(p)) < 0:  
                po = p1           
                qo=q1   
                p1 = p
                q1 = f(p)
            elif numpy.sign(f(p)) > 0:
                p1 = p       
                q1 = f(p)    
            else:
                print("ERROR")

if __name__ == '__main__':
    regufalsi_method(0, math.pi/2,1e-4,50)