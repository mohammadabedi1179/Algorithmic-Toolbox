
def fibonacci_partial_sum_naive(m, n):
    su=1
    suma=1
    a=0
    b=1
    if (n%60)<=1:
        su=(n%60)
    for i in range(1,n%60):
            c=a+b
            a=b
            b=c
            su +=c
    a=0
    b=1
    if (m%60)<=1:
        suma=(m%60)
    for i in range(1,m%60):
            c=a+b
            a=b
            b=c
            suma +=c
    if (m%60)<=1:
        su=su-suma+m%60
    else:
        su=su-suma+c%60
    return su % 10
m, n=input().split(" ")
m=int(m)
n=int(n)
print(fibonacci_partial_sum_naive(m, n))