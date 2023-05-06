from typing import List
from collections import deque


class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """

    def walls_and_gates(self, rooms: List[List[int]]):
        rows, cols = len(rooms), len(rooms[0])
        gates = deque()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    gates.append((r, c))

        while gates:
            r1, c1 = gates.popleft()
            for dr, dc in directions:
                r2, c2 = r1+dr, c1+dc
                if r2 in range(rows) and c2 in range(cols) and rooms[r2][c2] == 2147483647:
                    rooms[r2][c2] = rooms[r1][c1] + 1
                    gates.append((r2, c2))
