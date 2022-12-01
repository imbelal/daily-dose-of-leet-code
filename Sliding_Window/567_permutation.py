class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        dict = {}
        for ch in s1:
            dict[ch] = 1 + dict.get(ch, 0)

        l = 0
        r = len(s1)
        while r <= len(s2):
            substr = s2[l:r]
            sol = True
            for ch in substr:
                if substr.count(ch) != dict.get(ch):
                    sol = False
                    break
            if sol == True:
                return sol
            l += 1
            r += 1
        return False


S = Solution()
print(S.checkInclusion("abc", "ccccbbbbaaaa"))
