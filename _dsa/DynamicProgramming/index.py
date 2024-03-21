memo = [None] * 100


def fib(n):
    if memo(n) is not None:
        return memo[n]
    if n == 0 or n == 1:
        return n
    memo[n] = fib(n - 1) + fib(n - 2)

    return memo[n]


def fib_bt(n):
    fib_list = [0, 1]
    for index in range(2, n + 1):
        next_fib = fib_list[index - 1] + fib_list[index - 2]
        fib_list.append(next_fib)
    return fib_list(n)
