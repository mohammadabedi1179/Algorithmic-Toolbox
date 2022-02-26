def get_change(m):
    n10=m//10
    m=m%10
    n5=m//5
    n1=m%5
    n=n10+n5+n1
    return n
m=int(input())
print(get_change(m))