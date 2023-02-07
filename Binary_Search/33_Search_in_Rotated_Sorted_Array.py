class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        pivot = 0
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[-1]:
                l = mid + 1
            else:
                r = mid
        pivot = l

        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            realMid = (mid + pivot) % len(nums)
            if nums[realMid] > target:
                r = mid - 1
            elif nums[realMid] < target:
                l = mid + 1
            else:
                return realMid
        return - 1
