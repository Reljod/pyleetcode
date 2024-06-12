"""
Implement Simple Depth-first Search Algorithm with Recursion

"""

from lib.test_assertion import assert_equal_list


class DFS:

    adjacency_list: list[list[int]]

    def __init__(self, adjacency_list: list[list[int]]):
        self.adjacency_list = adjacency_list
        v_count = len(adjacency_list)

        self._visited = [False] * v_count
        self.visits = []

    def traverse(self, start_at: int):
        self.visits.append(start_at)
        self._visited[start_at] = True
        neighbors = self.adjacency_list[start_at]

        for n in neighbors:  # The neighbor priority is based on adjaceny list order
            if self._visited[n]:
                # Do not traverse for already visited vertices
                continue

            self.traverse(n)

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


class TestDFS:

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
        dfs = DFS(self.adjacency_list)
        dfs.traverse(start_at=0)

        assert len(self.adjacency_list) == len(set(dfs.visits))

    def test_should_get_traversal_path_from_search(self):
        dfs = DFS(self.adjacency_list)
        traversal_path = dfs.search(0, 6)

        assert_equal_list(traversal_path, [0, 1, 2, 4, 3, 6])


if __name__ == "__main__":
    TestDFS().test_should_traverse_all_vertices()
    TestDFS().test_should_get_traversal_path_from_search()
