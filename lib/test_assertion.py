def assert_equal_list(list1: list[int], list2: list[int]):
    assert len(list1) == len(list2)

    for i, val in enumerate(list1):
        assert val == list2[i]
