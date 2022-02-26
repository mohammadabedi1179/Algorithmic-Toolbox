import numpy as np
def get_fibonacci_huge_naive(n, m):
   r=np.zeros([m**2])
   r[0]=0
   r[1]=1
   for i in range(2,m**2):
        r[i]=r[i-2]+r[i-1]
        r[i]=r[i]%m
   for i in range(m**2):
       if r[i]==1 and r[i+1]==0:
           mod=i
           break
   Remain=n%(mod+1)
   return int(r[Remain])

n, m = input().split(" ")
n=int(n)
m=int(m)
print(get_fibonacci_huge_naive(n, m))
