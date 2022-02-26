def fibonacci_sum_naive(n):
    su=1
    a=0
    b=1
    if (n%60)<=1:
        su=(n%60)
    for i in range(1,n%60):
            c=a+b
            a=b
            b=c
            su +=c

    return su % 10
n = int(input())
print(fibonacci_sum_naive(n))
