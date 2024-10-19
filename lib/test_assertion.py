def assert_equal_unordered_list(list1: list[int], list2: list[int]):
    assert len(list1) == len(list2)

    for i, val in enumerate(list1):
        assert val == list2[i]


def assert_equal_unsorted_list(list1: list[int], list2: list[int]):
    assert len(list1) == len(list2)
    list1_sorted = sorted(list1)
    list2_sorted = sorted(list2)

    for i, val in enumerate(list1_sorted):
        assert val == list2_sorted[i]
