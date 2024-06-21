from lib.test_assertion import assert_equal_list


def get_two_sums(nums: list[int], target: int) -> list[int]:

    known_pairs = {}

    for i, num in enumerate(nums):
        other = target - num
        other_ind = known_pairs.get(other)

        print(known_pairs, other, other_ind)

        if other_ind is not None:
            return [other_ind, i]

        known_pairs[num] = i

    return []


def test_get_two_sums():
    nums = [2, 7, 11, 15]
    target = 9

    assert_equal_list(sorted([0, 1]), sorted(get_two_sums(nums, target)))


def test_empty_nums():
    nums = []
    target = 9

    assert_equal_list([], get_two_sums(nums, target))


def test_one_num_only():
    nums = [1]
    target = 1

    assert_equal_list([], get_two_sums(nums, target))
