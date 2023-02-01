from ast import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        if len(nums) == 1:
            return nums[0]
        while l <= r:
            mid = (l + r) // 2
            if nums[mid + 1] < nums[mid]:
                return nums[mid + 1]
            elif nums[mid - 1] > nums[mid]:
                return nums[mid]
            elif nums[-1] > nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        return nums[0]
