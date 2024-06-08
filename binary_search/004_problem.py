"""
There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1


Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104

"""

import pytest

from lib.loop_limiter import LoopLimiter
from typing import Generator


class RotArrSearch:

    def __init__(self, loop_limiter: LoopLimiter) -> None:
        self.loop_limiter = loop_limiter


    def search_in_rotated_arr(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        target_ind = -1

        while (left <= right and not self.loop_limiter.is_at_limit()):
            mid = (left + right) // 2

            mid_num = nums[mid]
            left_num = nums[left]
            right_num = nums[right]

            if target == mid_num:
                target_ind = mid
                break

            if left_num <= mid_num:
                if target > mid_num or target < left_num:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if target < mid_num or target > right_num:
                    right = mid - 1
                else:
                    left = mid + 1

        return target_ind




class TestRotatedArraySearch:

    @pytest.fixture
    def loop_limiter(self):
        yield LoopLimiter(limit=1000)

    @pytest.fixture
    def rot_array_search(self, loop_limiter: LoopLimiter):
        yield RotArrSearch(loop_limiter)

    def test_should_search_rotated_array(self, rot_array_search: RotArrSearch):
        rotated_arr_list = [ [4,5,6,7,0,1,2], [4,5,6,7,8,1,2,3], [1,2,3]]
        generate_test_mapping = lambda rotated_arr: [(i, rotated_arr.index(i)) for i in rotated_arr]
        rotated_arr_list_mapping = [ (r, generate_test_mapping(r)) for r in rotated_arr_list ]
        for rotated_arr, mapping in rotated_arr_list_mapping:
            for target, expected in mapping:
                assert rot_array_search.search_in_rotated_arr(rotated_arr, target) == expected

    def test_should_return_negative_one_when_not_exists(self, rot_array_search: RotArrSearch):
        rotated_arr = [4,5,6,7,0,1,2]
        target = 3
        expected = -1

        assert rot_array_search.search_in_rotated_arr(rotated_arr, target) == expected

    def test_should_search_single_valued_arr(self, rot_array_search: RotArrSearch):
        rotated_arr = [1]
        target = 0
        expected = -1

        assert rot_array_search.search_in_rotated_arr(rotated_arr, target) == expected
