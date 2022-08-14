from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l = 0
        r = len(height) - 1
        while(l < r):
            res = max(min(height[l], height[r]) * (r - l), res)
            if(height[l] <= height[r]):
                l += 1
            else:
                r -= 1
        return res


s = Solution()
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
res = s.maxArea(height)
print(res)
