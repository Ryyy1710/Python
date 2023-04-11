def f(x):
    return x*x*x + 3*x*x - 1

def secantmethod(po,p1,TOL,No):
    i=2
    qo = f(po)
    q1 = f(p1)
    
    while i <= No:
        p = p1 - q1*(p1-po)/(q1-qo)
        print(p)
        
        if abs(p-p1) < TOL:
            print('result: ',p)
            break
        i=i+1
        po=p1
        qo=q1
        p1=p
        q1=f(p)
            
secantmethod(-3, -2,1e-4,50)
    