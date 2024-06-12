"""
Implements Max/Min heap use for implementing priority queue.
"""

import logging
import pytest

from enum import Enum, auto
from lib.test_assertion import assert_equal_list


class Heap:

    LOGGER = logging.getLogger(__name__)

    class HeapType(Enum):
        MIN = auto()
        MAX = auto()

    _capacity: int
    _heap_type: HeapType

    _heap_arr: list[int | None]
    _size: int

    @staticmethod
    def create_min(capacity: int):
        return Heap(capacity, heap_type=Heap.HeapType.MIN)

    @staticmethod
    def create_max(capacity: int):
        return Heap(capacity, heap_type=Heap.HeapType.MAX)

    def __init__(self, capacity: int, heap_type: HeapType | None = HeapType.MIN):
        if capacity <= 0:
            raise RuntimeError(f"Cannot create heap with capacity {capacity}")

        self._capacity = capacity
        self._heap_type = heap_type

        self._heap_arr = [None] * capacity
        self._size = 0

    def insert(self, value: int) -> None:
        if self._size >= self._capacity:
            self.LOGGER.error("Max capacity already reached. Cannot insert new data")
            return

        self._heap_arr[self._size] = value
        self._heapify_up(self._size)
        self._size += 1

    def remove_at(self, ind: int) -> None:
        if self._size <= 0 or len(self._heap_arr) <= 0:
            return

        self._heap_arr[ind] = self._get_data_at(self._size - 1)
        self._heap_arr[self._size - 1] = None
        self._heapify_down(ind)
        self._size -= 1

    def get_top(self) -> int | None:
        if self._size <= 0 or len(self._heap_arr) <= 0:
            return

        return self._heap_arr[0]

    def take_top(self) -> int | None:
        top = self.get_top()
        self.remove_at(0)
        return top

    def get_heap_array(self):
        return self._heap_arr

    def _heapify_up(self, ind: int):
        if (parent_ind := self._get_parent_ind(ind)) < 0:
            return

        print("ind", ind)
        current_val = self._get_data_at(ind)
        parent_val = self._get_data_at(parent_ind)
        print(current_val, parent_val)
        if self._is_swappable(current_val, parent_val):
            self._swap(ind, parent_ind)

        return self._heapify_up(parent_ind)

    def _heapify_down(self, ind: int) -> None:
        if self._get_left_child(ind) is None:
            return

        current_val = self._get_data_at(ind)
        swappable_child_ind = self._get_most_swappable_ind(self._get_left_child_ind(ind), self._get_right_child_ind(ind))
        swappable_child_val = self._get_data_at(swappable_child_ind) if swappable_child_ind is not None else None

        if swappable_child_val is not None and self._is_swappable(swappable_child_val, current_val):
            self._swap(ind, swappable_child_ind)

        return self._heapify_down(swappable_child_ind)

    def _swap(self, ind1, ind2) -> None:
        self._heap_arr[ind1], self._heap_arr[ind2] = self._heap_arr[ind2], self._heap_arr[ind1]

    def _is_swappable(self, from_val, to_val) -> bool:
        if self._heap_type == self.HeapType.MAX:
            return from_val > to_val
        return from_val < to_val

    def _get_most_swappable_ind(self, left_index: int, right_index: int) -> int | None:
        left_val = self._get_data_at(left_index)
        right_val = self._get_data_at(right_index)

        if left_val is None:
            return

        if right_val is None:
            return left_index

        if left_val == right_val:
            return left_index

        if self._heap_type == self.HeapType.MAX:
            return left_index if left_val > right_val else right_index

        return left_index if left_val < right_val else right_index

    def _get_data_at(self, index) -> int | None:
        if index >= self._capacity:
            return

        return self._heap_arr[index]

    def _get_parent_ind(self, index) -> int:
        return (index - 1) // 2

    def _get_left_child_ind(self, index: int) -> int:
        return (index * 2) + 1

    def _get_left_child(self, index: int) -> int | None:
        c_ind = self._get_left_child_ind(index)
        return self._get_data_at(c_ind)

    def _get_right_child_ind(self, index: int) -> int | None:
        return (index * 2) + 2

    def _get_right_child(self, index: int) -> int | None:
        c_ind = self._get_right_child_ind(index)
        return self._get_data_at(c_ind)

class TestHeap:

    @pytest.fixture
    def sample_heap(self) -> Heap:
        heap = Heap(3)
        insert_val = [1, 2, 3]
        for v in insert_val:
            heap.insert(v)

        return heap

    def test_should_init_heap_with_none(self):
        min_heap = Heap(10)

        assert min_heap.get_top() is None

    def test_should_throw_runtime_error_on_zero_or_less_capacity(self):
        with pytest.raises(RuntimeError):
            Heap(0)

    def test_should_not_insert_data_at_full_capacity(self, sample_heap: Heap):
        sample_heap.insert(4)
        assert_equal_list(sample_heap.get_heap_array(), [1, 2, 3])


class TestMinHeap:

    @pytest.fixture
    def sample_min_heap(self) -> Heap:
        min_heap = Heap.create_min(10)
        insert_val = [20, 22, 7, 19, 5, 10, 30]
        for v in insert_val:
            min_heap.insert(v)

        # updated array underthehood: [5,7,10,20,19,13,11]
        return min_heap

    def test_should_have_min_on_top_upon_insert(self):
        insert_top_maps = [
            { "insert": [10, 5, 3], "at_top": 3 },
            { "insert": [20, 13, 7, 19, 5], "at_top": 5 }
        ]

        for m in insert_top_maps:
            min_heap = Heap.create_min(10)

            for i in m.get("insert"):
                min_heap.insert(i)

            assert min_heap.get_top() == m.get("at_top")

    def test_should_retain_min_top_upon_taking_top(self, sample_min_heap: Heap):
        init_top = sample_min_heap.get_top()
        top = sample_min_heap.take_top()

        assert top == init_top
        assert sample_min_heap.get_top() == 7

    def test_should_retain_min_heap_upon_removal(self, sample_min_heap: Heap):
        sample_min_heap.remove_at(1)

        assert_equal_list(sample_min_heap.get_heap_array(), [5, 19, 10, 22, 30, 20, None, None, None, None])


class TestMaxHeap:

    @pytest.fixture
    def sample_max_heap(self) -> Heap:
        max_heap = Heap.create_max(10)
        insert_val = [20, 22, 7, 19, 5, 10, 30]
        for v in insert_val:
            max_heap.insert(v)

        # updated array underthehood: [30,20,22,19,5,7,10]
        return max_heap

    def test_should_have_max_on_top_upon_insert(self):
        insert_top_maps = [
            { "insert": [3, 10, 5], "at_top": 10 },
            { "insert": [13, 20, 7, 19, 5], "at_top": 20 }
        ]

        for m in insert_top_maps:
            max_heap = Heap.create_max(10)

            for i in m.get("insert"):
                max_heap.insert(i)

            assert max_heap.get_top() == m.get("at_top")

    def test_should_retain_max_heap_upon_insertion(self, sample_max_heap: Heap):
        sample_max_heap.insert(25)
        assert_equal_list(sample_max_heap.get_heap_array(), [30, 25, 22, 20, 5, 7, 10, 19, None, None])

    def test_should_retain_max_top_upon_taking_top(self, sample_max_heap: Heap):
        init_top = sample_max_heap.get_top()
        top = sample_max_heap.take_top()

        assert top == init_top
        assert sample_max_heap.get_top() == 22

    def test_should_retain_max_heap_upon_removal(self, sample_max_heap: Heap):
        sample_max_heap.remove_at(1)

        assert_equal_list(sample_max_heap.get_heap_array(), [30, 19, 22, 10, 5, 7, None, None, None, None])
