def fibonacci_sum_squares_naive(n):
    a = 0
    b = 1
    c=1
    for i in range(n % 60):
        c = a + b
        a = b
        b = c
    m=(c%10)*(a%10)
    return m % 10

n = int(input())
print(fibonacci_sum_squares_naive(n))
