class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i, x in enumerate(nums):
            dict = {}
            for i, x in enumerate(nums):
                r = target - x
                if dict.get(r) != None:
                    return [dict.get(r), i]
                else:
                    dict[x] = i
            return []
