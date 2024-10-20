from dataclasses import dataclass
from typing import Self


@dataclass(frozen=True)
class Item:
    id: int

    def __repr__(self) -> str:
        return f"Item({self.id})"


class DFS:

    def __init__(self, adjacency_list: dict[Item, list[Item]]) -> None:
        self.adjacency_list = adjacency_list
        self.vertices = adjacency_list.keys()
        self.visited = { v: False for v in self.vertices }

    def search_item(self, start_at: Item, search_item: Item) -> list[Item]:
        traversals: list[Item] = []

        self.visited[start_at] = True
        traversals.append(start_at)

        for neighbor in self.adjacency_list[start_at]:
            if neighbor == search_item:
                traversals.append(neighbor)
                break

            # Only continue searching if search_item is not traversed yet
            if not self.visited[neighbor] and search_item not in traversals:
                traversals.extend(self.search_item(neighbor, search_item))

        return traversals


class DFSBuilder:

    def __init__(self) -> None:
        self.adjacency_list: dict[Item, list[Item]] = {}

    def add_relation(self, u: Item, v: Item) -> Self:
        if u not in self.adjacency_list:
            self.adjacency_list[u] = [v]
        else:
            self.adjacency_list[u].append(v)

        return self

    def add_edge(self, u: Item, v: Item) -> Self:
        return self.add_relation(u, v).add_relation(v, u)

    def build(self) -> DFS:
        return DFS(self.adjacency_list)

def main():
    v = [Item(i) for i in range(8)]
    dfs = DFSBuilder()\
            .add_edge(v[0], v[1])\
            .add_edge(v[0], v[2])\
            .add_edge(v[0], v[3])\
            .add_edge(v[1], v[2])\
            .add_edge(v[2], v[4])\
            .add_edge(v[3], v[6])\
            .add_edge(v[3], v[5])\
            .add_edge(v[4], v[6])\
            .add_edge(v[5], v[7])\
            .build()

    traversals = dfs.search_item(v[7], v[4])
    print("Traversals:", traversals)


if __name__ == "__main__":
    main()
