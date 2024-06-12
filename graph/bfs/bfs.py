"""
Implement Simple Breadth-first Search Algorithm with queue

"""

from data_structures.queue.queue import Queue
from lib.test_assertion import assert_equal_list


class BFS:

    def __init__(self, adjacency_list: list[list[int]]):
        self.adjacency_list = adjacency_list
        v_count = len(adjacency_list)

        self._visited = [False] * v_count

        self.v_queue = Queue()
        self.visits = []


    def traverse(self, start_at: int) -> None:
        self.v_queue.enqueue(start_at)

        while (not self.v_queue.is_empty()):
            v_curr = self.v_queue.dequeue()
            self.visits.append(v_curr)
            self._visited[v_curr] = True
            neighbors = self.adjacency_list[v_curr]

            for n in neighbors:
                if self._visited[n]:
                    continue

                self.v_queue.enqueue(n)

    def search(self, start_at: int, end_at: int) -> list[int]:
        self.traverse(start_at)

        traversal = []
        found = False
        for i in range(len(self.visits)):
            visit = self.visits[i]
            if visit == start_at:
                found = True

            if found:
                traversal.append(visit)

            if visit == end_at:
                break

        return traversal

class TestBFS:

    adjacency_list = [
        # (0..n]
        [1, 2],  # 0 -> [1, 2]
        [0, 1],
        [0, 4, 5],
        [4],
        [2, 3, 6],
        [2],
        [4]
    ]

    def test_should_traverse_all_vertices(self):
        bfs = BFS(self.adjacency_list)
        bfs.traverse(start_at=0)

        assert len(self.adjacency_list) == len(set(bfs.visits))

    def test_should_get_traversal_path_from_search(self):
        bfs = BFS(self.adjacency_list)
        traversal_path = bfs.search(0, 6)

        assert_equal_list(traversal_path, [0, 1, 2, 4, 5, 3, 6])


if __name__ == "__main__":
    TestBFS().test_should_traverse_all_vertices()
