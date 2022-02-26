import sys
def largest_number(a):
    n = len(a)/3
    for i in range(n):
        while a[3*i]!=0:

    return
n = int(input(""))
numbers = []
for i in range(n):
    numbers.append(int(input()))
m = []
for i in range(n):
    for j in range(3):
        k = numbers[i] % 10
        m.insert(0, k)
        numbers[i] = int((numbers[i]-k)/10)
print(largest_number(m))