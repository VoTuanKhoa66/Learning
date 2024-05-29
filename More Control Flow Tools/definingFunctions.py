def fib(n):
    """Print a Fibonacci series up to n."""
    a,b = 0,1
    while a < n:
        print(a, end=" ")
        a, b = b, a+b


def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a,b = b, a+b
    return result

f1 = fib2(100)
print(f1)