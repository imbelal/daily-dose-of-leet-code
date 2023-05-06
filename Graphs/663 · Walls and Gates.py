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
        visited = set()
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    gates.append((r, c))

        distance = 0
        lst = []
        while gates:
            r1, c1 = gates.popleft()
            for dr, dc in directions:
                r2, c2 = r1+dr, c1+dc
                if r2 in range(rows) and c2 in range(cols) and (r2, c2) not in visited and rooms[r2][c2] > 0:
                    rooms[r2][c2] = rooms[r1][c1] + 1
                    lst.append((r2, c2))
                    visited.add((r2, c2))

            if len(gates) == 0 and len(lst) > 0:
                gates = deque(lst)
                lst = []
