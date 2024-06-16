"""
This is for practicing binary search in python
"""


def main():
    print("Hello, binary search!")

    nums_list = [0, 5, 6, 8, 11, 12, 19]
    target = 5

    target_index = binary_search(target, nums_list)
    print(f"The index of target: {target} is {target_index}")


def binary_search(target: int, num_list: list[int]) -> int:
    # returns index of the target
    left, right = 0, len(num_list) - 1

    while (left <= right):
        mid = (left + right) // 2
        if target < num_list[mid]:
            right = mid
        elif target > num_list[mid]:
            left = mid + 1
        else:
            return mid

    return -1


def test_should_get_target_index():
    nums_list = [0, 5, 6, 8, 11, 12, 19]

    test_data = [(i, nums_list.index(i)) for i in nums_list]
    for td in test_data:
        assert td[1] == binary_search(td[0], nums_list)


def test_empty_nums_list():
    target = 1
    nums_list = []

    assert -1 == binary_search(target, nums_list)


if __name__ == "__main__":
    main()
