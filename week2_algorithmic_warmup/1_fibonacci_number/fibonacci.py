import numpy as np
n=int(input())
fib=np.zeros([1,n+2])
fib[0,0]=0
fib[0,1]=1
for i in range(n):
    fib[0,i+2]=fib[0,i+1]+fib[0,i]
print(int(fib[0,n]))