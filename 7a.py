n = int(input("Enter a number: "))
def fibonacci(n):
    a, b = 0, 1
    count = 0
    print(f"Fibonacci series for {n} numbers:")
    while count < n:
        print(a, end=' ')
        c = a + b
        a = b
        b = c
        count += 1
fibonacci(n)
