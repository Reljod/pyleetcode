"""
Get Nth Fibonacci number implemented with dynamic programming.

"""


def find_nth_number(n: int) -> int:
    # This is given that 0 will always be the
    # start of the fibonacci sequence
    #
    # Find sub-problems and sub-structures
    # f(n) = f(n-1) + f(n-2)
    solved_fib = []

    i = 0
    while i <= n:

        if i == 0 or i == 1:
            solved_fib.append(i)
            i += 1
            continue

        solved_fib.append(solved_fib[i - 1] + solved_fib[i - 2])
        i += 1

    return solved_fib[n]


def test_find_nth_number():
    # 0, 1, 1, 2, 3, 5, 8
    assert 0 == find_nth_number(0)
    assert 1 == find_nth_number(1)
    assert 1 == find_nth_number(1)
    assert 8 == find_nth_number(6)
