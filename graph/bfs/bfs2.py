from collections import deque
from dataclasses import dataclass
from typing import Self


@dataclass(frozen=True)
class Item:
    id: int
    is_target: bool

    def __repr__(self) -> str:
        return f"Item({self.id}, {self.is_target})"

class BFS:

    def __init__(self, adjacency_list: dict[Item, list[Item]]) -> None:
        self.adjacency_list = adjacency_list
        self.vertices = adjacency_list.keys()

    def search(self, start_at: Item) -> list[Item]:
        self.visited = {v: False for v in self.vertices}
        traversal: list[Item] = []

        q = deque()
        q.append(start_at)
        self.visited[start_at] = True

        while q:
            v_curr = q.popleft()
            traversal.append(v_curr)

            if v_curr.is_target:
                break

            for neighbor in self.adjacency_list[v_curr]:
                if self.visited[neighbor]:
                    continue

                self.visited[neighbor] = True
                q.append(neighbor)

        return traversal


class BFSBuilder:

    def __init__(self) -> None:
        self.adjacency_list: dict[Item, list[Item]] = {}

    def add_relation(self, u: Item, v: Item) -> Self:
        if u not in self.adjacency_list:
            self.adjacency_list[u] = [v]
        else:
            self.adjacency_list[u].append(v)

        return self

    def add_edge(self, item1: Item, item2: Item) -> Self:
        return self.add_relation(item1, item2).add_relation(item2, item1)

    def build(self) -> BFS:
        return BFS(self.adjacency_list)


def main():
    bfs = BFSBuilder()\
        .add_edge(Item(0, False), Item(1, False))\
        .add_edge(Item(0, False), Item(2, False))\
        .add_edge(Item(0, False), Item(3, False))\
        .add_edge(Item(1, False), Item(3, False))\
        .add_edge(Item(2, False), Item(6, False))\
        .add_edge(Item(2, False), Item(7, False))\
        .add_edge(Item(3, False), Item(5, False))\
        .add_edge(Item(5, False), Item(7, False))\
        .add_edge(Item(6, False), Item(8, True))\
        .build()

    traversal = bfs.search(Item(0, False))
    print(traversal)


if __name__ == "__main__":
    main()
