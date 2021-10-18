__version__ = '0.1.0'

def py_fib(n):
    if n < 2:
        return 1
    return py_fib(n-2) + py_fib(n-1)
