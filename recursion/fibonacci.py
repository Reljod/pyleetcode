import sys

class Fibonacci:

    def __init__(self, start_at = (0, 1)) -> None:
        self.start_at = start_at

    def get_nth_fib(self, n):
        if n <= 1:
            return self.start_at[n]

        return self.get_nth_fib(n - 1) + self.get_nth_fib(n - 2)


def main(*args):

    input = int(args[0]) if len(args) >= 1 else 5

    f = Fibonacci(start_at=(1, 1))
    output = f.get_nth_fib(input)

    print(f"{input} Nth fibonacci is {output}")


if __name__ == "__main__":
    main(*sys.argv[1:])
