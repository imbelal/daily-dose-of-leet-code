from ast import List
from math import ceil


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        l, r = 1, max(piles)
        res = r
        while l <= r:
            mid = (l + r) // 2
            hourRequired = 0
            for x in piles:
                hourRequired += ceil(x/mid)
            if h < hourRequired:
                l = mid + 1
            else:
                res = min(r, mid)
                r = mid - 1

        return res
