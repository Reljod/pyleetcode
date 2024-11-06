from typing import Any, Self


class Node:

    def __init__(self, val: Any, next: Self | None = None):
        self.val = val
        self.next = next


class SingleLinkedListBuilder:

    def __init__(self) -> None:
        self.head: Node | None = None
        self.end: Node | None = None

    def add(self, node: Node) -> Self:

        if self.head is None:
            self.head = node
            self.end = self.head
            return self

        if self.end is not None:
            self.end.next = node

        self.end = node

        return self

    def build(self):
        return self.head

    def display(self, head: Node | None) -> None:
        while head is not None:
            print(head.val)
            head = head.next


def main():
    a = Node(10)
    b = Node(20)
    c = Node(30)

    sb = SingleLinkedListBuilder()
    head = sb.add(a)\
             .add(b)\
             .add(c)\
             .build()

    sb.display(head)


if __name__ == "__main__":
    main()
