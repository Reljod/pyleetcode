"""
Disclaimer: This is just a sample problem I personally drafted.
The question might not be as descriptive or complete as what a regular
coding problem would have.


Problem:

Find the index of given number (target) on a sorted num array (sorted_arr)
using binary search algorithm.

target = any num
sorted_arr = sorted non-repeating num array

"""

import sys

from lib.loop_limiter import LoopLimiter


def main(*args):
    sorted_arr = [-1, 0, 3, 5, 9, 11]
    target = 9

    target_ind = find_target_ind(target, sorted_arr)

    print(f"Target {target} is {'Missing' if target_ind == -1 else f'in {target_ind}' }")

def find_target_ind(target: int, arr: list[int]) -> int:
    l_ind = 0
    r_ind = len(arr) - 1

    limiter = LoopLimiter()

    while (l_ind <= r_ind and not limiter.is_at_limit()):
        m_ind = (l_ind + r_ind) // 2

        if arr[m_ind] > target:
            r_ind = m_ind
        elif arr[m_ind] < target:
            l_ind = m_ind + 1
        else:
            # Means arr[m_ind] == target
            return m_ind

    return -1

def test_find_target_ind() -> None:
    sorted_arr = [21, 32, 33, 59, 101, 121, 1903, 45001, 100000]

    input_expected_map = [(x, sorted_arr.index(x)) for x in sorted_arr]

    for (target, expected) in input_expected_map:
        assert find_target_ind(target, sorted_arr) == expected

if __name__ == "__main__":
    main(*sys.argv[1:])
