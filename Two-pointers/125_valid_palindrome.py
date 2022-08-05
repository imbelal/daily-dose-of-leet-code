class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum, s)).lower()
        if len(s) <= 1:
            return True
        length = len(s)
        p1 = 0
        p2 = length - 1
        n = length / 2
        while n > 0:
            if s[p1] != s[p2]:
                return False
            p1 += 1
            p2 -= 1
            n -= 1
        return True
