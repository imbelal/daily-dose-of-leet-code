from typing import List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        rotten = deque()
        numberOfFreshOrange = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    rotten.append((r, c))
                elif grid[r][c] == 1:
                    numberOfFreshOrange += 1

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        lst = []
        maxTime = 0

        while rotten:
            r1, c1 = rotten.popleft()
            for dr, dc in directions:
                r2 = r1 + dr
                c2 = c1 + dc
                if r2 in range(rows) and c2 in range(cols) and grid[r2][c2] == 1:
                    lst.append((r2, c2))
                    numberOfFreshOrange -= 1
                    grid[r2][c2] = 2

            if len(rotten) == 0 and len(lst) > 0:
                maxTime += 1
                rotten = deque(lst)
                lst = []

        if numberOfFreshOrange == 0:
            return maxTime
        else:
            return -1


s = Solution()
x = s.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]])
print(x)
