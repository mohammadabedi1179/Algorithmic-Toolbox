
n=int(input())
a=0
b=1
for i in range((n-1)%60):
    c=a+b
    a=b
    b=c
print(c%10)
