import sys

class Factorial:

    def __init__(self):
        pass

    def get_factorial(self, val: int):

        if val <= -1:
            return "invalid"

        if val <= 1:
            return 1

        return val * self.get_factorial(val - 1)


def main(*arg):
    f = Factorial()

    input = int(arg[1])
    print(f"Factorial of {input} is {f.get_factorial(input)}")

if __name__ == "__main__":
    main(*sys.argv)
