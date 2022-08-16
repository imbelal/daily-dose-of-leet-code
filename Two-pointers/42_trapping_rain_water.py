from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        maxL = height[0]
        maxR = height[-1]
        L = 0
        R = len(height) - 1
        res = 0
        while L <= R:
            if maxL <= maxR:
                if maxL - height[L] >= 0:
                    res += maxL - height[L]
                maxL = max(maxL, height[L])
                L += 1
            else:
                if maxR - height[R] >= 0:
                    res += maxR - height[R]
                maxR = max(maxR, height[R])
                R -= 1
        return res


s = Solution()
res = s.trap([5, 5, 1, 7, 1, 1, 5, 2, 7, 6])
print(res)
