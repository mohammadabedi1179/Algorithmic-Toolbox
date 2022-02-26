import sys
"""def get_majority_element(n,a):
    m=n
    d=[]
    for i in range(n):
        d.append(i)
    b=[]
    while n>0:
        current_element=a[d[0]]
        count=0
        for j in d:

            if current_element==a[j]:
                count=count+1
            else:
                b.append(j)
        if count>m/2:
            return 1
        d=b
        b=[]
        n=n-count

n=int(input())
list1=[]
for i in range(n):
    list1.append(int(input()))
if get_majority_element(n,list1) == 1:
    print(1)
else:
    print(0)
if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(n,a) == 1:
        print(1)
    else:
        print(0)"""
# python3
n = int(input())
seq = [int(i) for i in input().split()]


def divide_func(seq, l, r):
    if l+1==r:
        return seq[l]
    elif l+2==r:
        return seq[l]
    m = (l+r)//2
    left = divide_func(seq, l, m)
    right = divide_func(seq, m, r)

    c1, c2 = 0, 0
    for i in seq[l:r]:
        if i == left:
            c1+=1
        elif i == right:
            c2+=1
    if c1>(r-l)//2 and left != -1:
        return left
    elif c2>(r-l)//2 and right != -1:
        return right
    else: 
        return -1

print(int(divide_func(seq, 0, n) != -1))
