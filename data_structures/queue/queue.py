"""
Implement Queue to do enqueue and dequeue using pointer-like implementation in python.
"""


from typing import Self
from dataclasses import dataclass


class Queue:

    @dataclass
    class Node:
        next: Self | None  # Should have been just the reference of the next node
        data: int

    _head: Node | None
    _tail: Node | None

    def __init__(self) -> None:
        self._head = None
        self._tail = None

    def get_front(self) -> int:
        return self._head.data

    def get_back(self) -> int:
        return self._tail.data

    def enqueue(self, data: int) -> None:
        node = self.Node(None, data)

        if self._head is None:
            self._head = node
        else:
            self._tail.next = node

        self._tail = node

    def dequeue(self) -> int | None:
        head_node = self._head
        self._head = self._head.next
        return head_node.data


class TestQueue:

    def test_should_enqueue_data(self):
        queue = Queue()
        queue.enqueue(10)
        queue.enqueue(20)
        queue.enqueue(30)

        assert queue.get_front() == 10
        assert queue.get_back() == 30

    def test_should_dequeue_data(self):
        queue = Queue()
        queue.enqueue(10)
        queue.enqueue(20)
        queue.enqueue(30)

        data = queue.dequeue()

        assert data == 10
        assert queue.get_front() == 20
        assert queue.get_back() == 30


if __name__ == "__main__":
    TestQueue().test_should_enqueue_data()
    TestQueue().test_should_dequeue_data()
