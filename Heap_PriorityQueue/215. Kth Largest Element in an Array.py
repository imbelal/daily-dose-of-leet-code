from ast import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        arr = [-x for x in nums]
        heapq.heapify(arr)
        res = 0
        while k > 0:
            res = heapq.heappop(arr)
            k -= 1
        return (-1) * res


s = Solution()
s.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)
