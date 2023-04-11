import numpy as np

def gaussian_elimination(A, b):

    n = len(A)

    A = np.concatenate((A, b.reshape(n, 1)), axis=1)
    #Step 1
    for i in range(n):
        #Step 2
        p = i
        while p <= n and A[p-1, i-1] == 0:
            p += 1

        if p > n:
            print("no unique solution exists")
            break
        #Step 3
        if p != i:
            A[[i, p]] = A[[p, i]]
        #Step 4
        for j in range(i+1, n):
            #Step 6
            A[j] = A[j] - A[i] * (A[j, i]/A[i, i])
    #Step 7
    if A[n-1, n-1] == 0:
        print("no unique solution exists")
        
    #Step 8    
    x = A[n-1, n] / A[n-1, n-1]
    x = np.zeros(n)
    
    #Step 9
    for i in range(n-1, -1, -1):
        x[i] = A[i, -1] - sum([A[i, j] * x[j] for j in range(n) if j != i])
        x[i] = x[i] / A[i, i]
    return x

A = np.array([[0.003000, 59.14], 
              [5.291, -6.130] ], dtype=float)
b = np.array([59.17, 46.78], dtype=float)

x = gaussian_elimination(A, b)
print(x)