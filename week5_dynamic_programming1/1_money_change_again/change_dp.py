import sys
def get_change(m):
    n=m//4
    if n>0:
        if (m-4*n)==2:
            n=n-1
    o=(m-4*n)//3
    p=m-4*n-3*o
    return o+n+p 
"""m=int(input())
print(get_change(m))"""

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
