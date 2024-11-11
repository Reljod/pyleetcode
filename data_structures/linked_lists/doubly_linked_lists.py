from typing import Any, Self


class Node:
    def __init__(self, val: Any):
        self.val = val
        self.next: Self | None = None
        self.prev: Self | None = None

    def __str__(self) -> str:
        return f"Node({self.val})"


class DoublyLinkedList:

    def __init__(self) -> None:
        self.head: Node | None = None
        self.end: Node | None = None

    def add(self, node: Node) -> Self:
        if self.head is None:
            self.head = node
            self.end = self.head
            return self

        if self.end is not None:
            prev = self.end

            self.end.next = node

            self.end = node
            self.end.prev = prev

        return self

    def traverse_forward(self, head: Node | None) -> None:
        curr: Node | None = head

        while curr is not None:
            print(curr.val)
            curr = curr.next

    def traverse_backward(self, end: Node | None) -> None:
        curr: Node | None = end

        while curr is not None:
            print(curr.val)
            curr = curr.prev


def main():
    a = Node(10)
    b = Node(20)
    c = Node(30)
    d = Node(40)

    dll = DoublyLinkedList()

    dll.add(a)\
        .add(b)\
        .add(c)\
        .add(d)

    head = dll.head
    end = dll.end

    print("Traverse forward from head:", head)
    dll.traverse_forward(head)

    print("Traverse forward from end:", end)
    dll.traverse_backward(end)


if __name__ == "__main__":
    main()
