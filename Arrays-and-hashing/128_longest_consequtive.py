class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        s = sorted(set(nums))
        if len(s) == 1:
            return 1
        maxCon = 0
        crntCon = 1
        for i in range(len(s) - 1):
            if s[i+1] - s[i] == 1:
                crntCon += 1
                # print(crntCon)
                if i == len(s) - 2 and maxCon < crntCon:
                    maxCon = crntCon
            else:
                if maxCon < crntCon:
                    maxCon = crntCon
                crntCon = 1

        return maxCon
