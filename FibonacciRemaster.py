def re_fib(n, result):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return re_fib(n-1, result) + re_fib(n-2, result)