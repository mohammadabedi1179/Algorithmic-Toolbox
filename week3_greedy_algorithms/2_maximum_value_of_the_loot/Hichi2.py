n=int(input())
m=[]
for i in range(3):
    k=n%10
    m.append(k)
    n=(n-k)/10
