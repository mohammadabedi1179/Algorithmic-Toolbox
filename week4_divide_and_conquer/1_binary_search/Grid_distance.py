import numpy as np
def grid(n,m):
    b=np.ones((n,m),dtype=int)
    for i in range(1,n):
        for j in range(1,m):
            b[i,j]=b[i-1,j]+b[i,j-1]
    number_of_ways=b[n-1,m-1]
    return b
print(grid(4,3))