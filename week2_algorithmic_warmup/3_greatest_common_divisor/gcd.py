
def gcd_naive(a, b):
    d=1
    while d!=0:
        d=a%b
        a=b
        b=d
    return a
a, b =input().split(" ")
a=int(a)
b=int(b)
print(gcd_naive(a, b))
