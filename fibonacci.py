from types import *
import math
import string

def print_fibonacci(n):
    """Print a Fibonacci series up to n."""
    a, b = 1, 1
    while a <= n:
        print a;
        a, b = b, a+b

print_fibonacci(2000)

def fibonacci(n):
    """Returns a list of Fibonacci numbers up to n."""
    assert type(n) is IntType, "fibonacci received a non-integer: %s" % `n`
    if n < 1: return []
    f = [1, 1]
    while f[-1] <= n:
        f.append(f[-1] + f[-2])
    return f[0:-1]

fibs = fibonacci(10000)
ratios = [float(fibs[i])/fibs[i-1] for i in range(1, len(fibs))]

print "Fibonacci:", fibs
print "Ratios:    [%s]" % string.join(["%.6g" % r for r in ratios], ", ")

print "Golden ratio: %.10g" % ((math.sqrt(5)+1)/2)

# print "Fibonacci:", fibonacci('10')
# print "Fibonacci:", fibonacci('sd')


