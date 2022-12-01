from copy import copy


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) == len(t) and s == t:
            return s
        hashT = {}
        need = len(t)
        for x in t:
            hashT[x] = 1 + hashT.get(x, 0)
        print(hashT)
        l, r = 0, 0
        res = ""
        minLength = len(s) + 1
        for i in range(len(s)):
            dct = copy(hashT)
            have = 0
            # print(s[i])
            if s[i] in t:
                l = i
                dct[s[i]] -= 1
                have += 1
                j = i + 1
                while (have < need and j < len(s)):
                    if s[j] in t and dct[s[j]] > 0:
                        dct[s[j]] -= 1
                        have += 1
                    j += 1

                if have == need:
                    sbstr = s[l:j]
                    if minLength > len(sbstr):
                        minLength = len(sbstr)
                        res = sbstr
            else:
                continue
        return res


s = Solution()
res = s.minWindow("aaaaaaaaaaaabbbbbcdd",
                  "abcdd"
                  )
print(res)
