from collections import deque
from dataclasses import dataclass
from enum import auto, Enum
from typing import Any, Callable, Self


@dataclass
class Node:
    data: Any
    left: Self | None = None
    right: Self | None = None

    def __str__(self) -> str:
        return f"Node({str(self.data)})"


class DfsType(Enum):
    PRE_ORDER = auto()
    IN_ORDER = auto()
    POST_ORDER = auto()


class BinaryTreeTraverser:
    def traverse_dfs(self, current: Node | None, predicate: Callable[[Node], None], dfs_type = DfsType.IN_ORDER) -> None:
        if current is None:
            return

        if dfs_type == DfsType.PRE_ORDER:
            predicate(current)

        self.traverse_in_order_dfs(current.left, predicate)

        if dfs_type == DfsType.IN_ORDER:
            predicate(current)

        self.traverse_in_order_dfs(current.right, predicate)

        if dfs_type == DfsType.POST_ORDER:
            predicate(current)

    def traverse_pre_order_dfs(self, current: Node | None, predicate: Callable[[Node], None]) -> None:
        return self.traverse_dfs(current, predicate, dfs_type=DfsType.PRE_ORDER)

    def traverse_in_order_dfs(self, current: Node | None, predicate: Callable[[Node], None]) -> None:
        return self.traverse_dfs(current, predicate, dfs_type=DfsType.IN_ORDER)

    def traverse_post_order_dfs(self, current: Node | None, predicate: Callable[[Node], None]) -> None:
        return self.traverse_dfs(current, predicate, dfs_type=DfsType.POST_ORDER)

    def traverse_bfs(self, current: Node | None, predicate: Callable[[Node], None]) -> None:
        q = deque([current])

        while q:
            node = q.popleft()

            if node is None:
                return

            predicate(node)

            if node.left is not None:
                q.append(node.left)

            if node.right is not None:
                q.append(node.right)


class BinaryTree:

    def __init__(self, traverser: BinaryTreeTraverser) -> None:
        self.traverser = traverser
        self.storer = []

    def traverse(self, root: Node | None) -> None:
        return self.traverser.traverse_bfs(root, print)


def main():
    nodes = [Node(i+1) for i in range(10)]

    nodes[0].left = nodes[1]
    nodes[0].right = nodes[2]

    nodes[1].left = nodes[3]
    nodes[1].right = nodes[4]

    nodes[2].left = nodes[5]
    nodes[2].right = nodes[6]

    nodes[3].left = nodes[7]
    nodes[3].right = nodes[8]

    nodes[4].left = nodes[9]

    root = nodes[0]

    binary_tree_traverse = BinaryTreeTraverser()
    binary_tree = BinaryTree(binary_tree_traverse)

    binary_tree.traverse(root)

if __name__ == "__main__":
    main()
