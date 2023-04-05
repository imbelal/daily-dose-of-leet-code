from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i: int, currntArr: List[int], sum: int):
            if sum == target:
                res.append(currntArr.copy())
                return
            elif i >= len(candidates) or sum > target:
                return
            currntArr.append(candidates[i])
            dfs(i, currntArr, sum + candidates[i])
            currntArr.pop()
            dfs(i+1, currntArr, sum)
            return res

        dfs(0, [], 0)
        return res


s = Solution()
x = s.combinationSum([2, 3, 5], 8)
print(x)
