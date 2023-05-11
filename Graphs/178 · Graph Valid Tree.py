from typing import (
    List,
)


class Solution:

    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) == 0:
            return True

        visited = set()
        neighbours = {i: [] for i in range(n)}

        def dfs(n, prev):
            if n in visited:
                return False
            visited.add(n)
            for x in neighbours[n]:
                if prev == x:
                    continue
                if not dfs(x, n):
                    return False
            return True

        for r, c in edges:
            neighbours[r].append(c)
            neighbours[c].append(r)

        return dfs(0, -1) and len(visited) == n


s = Solution()
x = s.valid_tree(5, [[0, 1], [0, 2], [0, 3], [1, 4]])
print(x)
