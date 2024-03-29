from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pec = set()
        atl = set()

        def dfs(r, c, visited, prevHeight):
            if (r < 0 or r == rows
                or c < 0 or c == cols
                or (r, c) in visited or
                    heights[r][c] < prevHeight):
                return
            visited.add((r, c))
            dfs(r+1, c, visited, heights[r][c])
            dfs(r-1, c, visited, heights[r][c])
            dfs(r, c+1, visited, heights[r][c])
            dfs(r, c-1, visited, heights[r][c])

        for c in range(cols):
            dfs(0, c, pec, heights[0][c])
            dfs(rows-1, c, atl, heights[rows-1][c])
        for r in range(rows):
            dfs(r, 0, pec, heights[r][0])
            dfs(r, cols - 1, atl, heights[r][cols-1])

        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pec and (r, c) in atl:
                    res.append([r, c])
        return res


s = Solution()
x = s.pacificAtlantic([[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [
                      2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]])
print(x)
