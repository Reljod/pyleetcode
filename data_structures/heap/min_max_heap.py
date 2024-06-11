"""
Implements Max/Min heap use for implementing priority queue.
"""

from enum import Enum, auto


class Heap:

    class HeapType(Enum):
        MIN = auto()
        MAX = auto()

    _heap_arr: list[int | None]
    _size: int
    _heap_type: HeapType

    @staticmethod
    def create_min(capacity: int):
        return Heap(capacity, heap_type=Heap.HeapType.MIN)

    @staticmethod
    def create_max(capacity: int):
        return Heap(capacity, heap_type=Heap.HeapType.MAX)

    def __init__(self, capacity: int, heap_type: HeapType | None = HeapType.MIN):
        if capacity <= 0:
            raise RuntimeError(f"Cannot create heap with capacity {capacity}")

        self._heap_type = heap_type

        self._heap_arr = [None] * capacity
        self._size = 0

    def insert(self, value: int) -> None:

        current_ind = self._size

        self._heap_arr[current_ind] = value
        self._size += 1

        self._heapify_up(current_ind)

    def get_top(self) -> int | None:
        return self._heap_arr[0]

    def _heapify_up(self, ind: int):
        if ((parent_ind := self._get_parent(ind)) is None):
            return

        current_val = self._heap_arr[ind]
        parent_val = self._heap_arr[parent_ind]
        if self._heapify_up_cmp(current_val, parent_val):
            self._swap(ind, parent_ind)

        return self._heapify_up(parent_ind)

    def _get_parent(self, index) -> int | None:
        if index <= 0:
            return None

        return (index - 1) // 2

    def _heapify_up_cmp(self, from_val, to_val) -> bool:
        if self._heap_type == self.HeapType.MAX:
            return from_val > to_val
        return from_val < to_val

    def _swap(self, ind1, ind2) -> None:
        self._heap_arr[ind1], self._heap_arr[ind2] = self._heap_arr[ind2], self._heap_arr[ind1]


class TestMinHeap:

    def test_should_init_heap_with_none(self):
        min_heap = Heap.create_min(10)

        assert min_heap.get_top() is None

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


class TestMaxHeap:

    def test_should_init_heap_with_none(self):
        max_heap = Heap.create_max(10)

        assert max_heap.get_top() is None

    def test_should_have_min_on_top_upon_insert(self):
        insert_top_maps = [
            { "insert": [3, 10, 5], "at_top": 10 },
            { "insert": [13, 20, 7, 19, 5], "at_top": 20 }
        ]

        for m in insert_top_maps:
            max_heap = Heap.create_max(10)

            for i in m.get("insert"):
                max_heap.insert(i)

            assert max_heap.get_top() == m.get("at_top")
