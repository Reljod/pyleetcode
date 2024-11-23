from typing import Any, Callable, Self


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

    def insert(self, head: Node | None, node: Node, at: Node) -> None:
        curr = head

        while curr is not None:
            if curr == at:
                temp = curr.next
                node.next = temp
                curr.next = node

            curr = curr.next

    def remove(self, head: Node | None, node: Node) -> None:
        curr = head

        while curr is not None:
            if curr.next == node:
                curr.next = node.next

            curr = curr.next

    def filter(self, head: Node | None, predicate: Callable[[Node], bool]) -> Node | None:
        curr = head
        filtered = None

        while curr is not None:
            if predicate(curr):
                if filtered is None:
                    filtered = curr
                else:
                    filtered.next = curr
                    filtered = filtered.next

            curr = curr.next

        if filtered is not None:
            filtered.next = None

        return filtered

    def build(self):
        return self.head

    def display(self, head: Node | None) -> None:
        curr: Node | None = head

        while curr is not None:
            print(curr.val)
            curr = curr.next


def main():
    a = Node(10)
    b = Node(20)
    c = Node(30)
    d = Node(40)

    sb = SingleLinkedListBuilder()
    head = sb.add(a)\
             .add(b)\
             .add(c)\
             .build()

    print("Display linked list after adding")
    sb.display(head)

    print("Display linked list after insertion")
    sb.insert(head, d, b)
    sb.display(head)

    print("Display linked list after deletion")
    sb.remove(head, d)
    sb.display(head)

    print("Display linked list after filter")
    result = sb.filter(head, lambda x: x.val >= 20)
    sb.display(result)

if __name__ == "__main__":
    main()
