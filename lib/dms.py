def fib(n): # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result
 
def return_double(n):
    return(n * 2)

def factorial(n):
    ans = 1
    while n > 0:
        ans = ans * n
        n = n - 1
    return(ans)

