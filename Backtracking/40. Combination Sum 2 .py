class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i: int, curr: List[int], sum: int):
            if sum == target:
                res.append(curr.copy())
                return
            elif sum > target or i >= len(candidates):
                return
            curr.append(candidates[i])
            dfs(i+1, curr, sum + candidates[i])
            curr.pop()
            while (i+1) < len(candidates) and candidates[i+1] == candidates[i]:
                i += 1
            dfs(i+1, curr, sum)
        dfs(0, [], 0)
        return res
