def gcd_naive(a, b):
    d=1
    while d!=0:
        d=a%b
        a=b
        b=d
    return a
def lcm_naive(a, b):
    gcd=gcd_naive(a,b)
    l=a*b/gcd
    return l

a,b=input().split(" ")
a=int(a)
b=int(b)
print(int(lcm_naive(a,b)))
