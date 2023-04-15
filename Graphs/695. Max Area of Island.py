from typing import List
from queue import deque


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        visited = set()
        rows, cols = len(grid), len(grid[0])
        maxArea = 0

        def bfs(r, c, m):
            q = deque()
            q.append((r, c))
            visited.add((r, c))
            m += 1
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    if r in range(rows) and c in range(cols) and grid[r][c] == 1 and (r, c) not in visited:
                        q.append((r, c))
                        visited.add((r, c))
                        m += 1
            return m

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and grid[r][c] not in visited:
                    maxArea = max(maxArea, bfs(r, c, 0))
        return maxArea


s = Solution()
x = s.maxAreaOfIsland([[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0], [
                      0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]])

print(x)
