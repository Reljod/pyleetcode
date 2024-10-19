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
    v0 = Item(0, False)
    v1 = Item(1, False)
    v2 = Item(2, False)
    v3 = Item(3, False)
    v5 = Item(5, False)
    v6 = Item(6, False)
    v7 = Item(7, False)
    v8 = Item(8, True)

    bfs = BFSBuilder()\
        .add_edge(v0, v1)\
        .add_edge(v0, v2)\
        .add_edge(v0, v3)\
        .add_edge(v1, v3)\
        .add_edge(v2, v6)\
        .add_edge(v2, v7)\
        .add_edge(v3, v5)\
        .add_edge(v5, v7)\
        .add_edge(v6, v8)\
        .build()

    traversal = bfs.search(v5)
    print(traversal)


if __name__ == "__main__":
    main()
