"""
Disclaimer: This is just a sample problem I personally drafted.
The question might not be as descriptive or complete as what a regular
coding problem would have.


Problem:

This is similar problem to 001 but instead we ask a different question.
This is for establishing our knowledge in Binary Search.

Question:
1.a. In what index should we insert a number in a sorted array num to
still maintain it being sorted. When a number already exists, put the number
to the left of the first instance of the number.

1.b. What index when we put the number on the right side of the existing number instead.

target = any num
sorted_arr = sorted non-repeating num array

"""

from lib.loop_limiter import LoopLimiter


def main():
    sorted_arr = [ -3, 0, 1, 1, 5, 5, 7, 7, 13, 20 ]
    target = 7

    bisect_at = bisect_left(target, sorted_arr)

    print(f"{target} can be insert in {sorted_arr} at {bisect_at}")

def bisect_left(num: int, arr: list[int]) -> int:
    low = 0
    high = len(arr)

    limiter = LoopLimiter()

    while (low < high and not limiter.is_at_limit()):
        mid = low + (high - low) // 2
        if arr[mid] < num:
            low = mid + 1
        else:
            high = mid

    return low

def test_bisect_left() -> None:
    sorted_arr = [ -3, 0, 1, 1, 5, 5, 7, 7, 13, 20 ]

    assert bisect_left(5, sorted_arr) == 4
    assert bisect_left(7, sorted_arr) == 6

def test_bisect_left_not_exists() -> None:
    sorted_arr = [ -3, 0, 1, 1, 5, 5, 7, 7, 13, 20 ]

    assert bisect_left(0, sorted_arr) == 1

def test_bisect_left_empty_arr() -> None:
    sorted_arr = []

    assert bisect_left(10, sorted_arr) == 0


if __name__ == "__main__":
    main()
