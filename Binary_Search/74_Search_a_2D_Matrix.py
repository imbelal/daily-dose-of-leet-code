from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def search(nums: List[int], target: int) -> int:
            l = 0
            r = len(nums) - 1
            while l <= r:
                mid = l + ((r - l) // 2)
                if nums[mid] > target:
                    r = mid-1
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    return mid
            return - 1

        l = 0
        r = len(matrix) - 1
        res = -1

        while l <= r:
            mid = (l + r) // 2
            if matrix[mid][0] < target:
                res = search(matrix[mid], target)
                if l == r or res != - 1:
                    break
                l = mid + 1
            elif matrix[mid][0] > target:
                if l == r:
                    res = search(matrix[mid], target)
                    break
                r = mid - 1
            elif matrix[mid][0] == target:
                return True
        if res == -1:
            return False
        else:
            return True
