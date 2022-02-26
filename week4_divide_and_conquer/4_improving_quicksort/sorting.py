# Uses python3
"""import sys
import random

def sorting(n,a):
    m1=0
    m2=0
    if n<=1:
        a_sorted=a
    else:
        d1=[]
        d2=[]
        for i in range(1,n):
            if a[i]<=a[0]:
                d1.append(a[i])
                m1=m1+1

            else:
                d2.append(a[i])
                m2=m2+1
        a_sorted=sorting(m1,d1)+[a[0]]+sorting(m2,d2)
    

    return a_sorted

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b=sorting(n,a)
    for x in b:
        print(x, end=' ')"""
# python3
import random
import time
def quicksort3(arr, l, r):
    # print('Splitting:', arr[l:r])
    if l + 1 >= r:
        return

    # Pivot selection; Return a random integer N such that l <= N <= r
    m = random.randint(l, r-1)
    # temp = sorted([(0,arr[0]), ((l+r)//2,arr[(l+r)//2]), (-1,arr[-1])], key = lambda x: x[1])
    # m = temp[1][0]
    arr[l], arr[m] = arr[m], arr[l]

    # partition procedure
    m1, m2 = partition3(arr, l, r)

    quicksort3(arr, l, m1)
    quicksort3(arr, m2+1, r)

def partition3(arr, l, r):
    m2 = l
    for i in range(l+1, r):
        if arr[i] <= arr[l]:
            arr[m2+1], arr[i] = arr[i], arr[m2+1]
            m2 += 1

    arr[l], arr[m2] = arr[m2], arr[l]

    m1 = l
    for i in range(l, m2):
        if arr[i] < arr[m2]:
            arr[i], arr[m1] = arr[m1], arr[i]
            m1 += 1
    return m1, m2

def create_array(size):
    return [random.choice(list(range(10))) for _ in range(size)]

n = int(input())
seq = [int(i) for i in input().split()]
for x in seq:
    print(x, end=' ')

t1 = time.time()
seq = create_array(100000)
quicksort3(seq, 0, 100000)
t2 = time.time()
#print('Time taken:', t2-t1)
