import string


class Solution(object):
    def isAnagram(self, s, t):
        res = True
        for item in string.ascii_lowercase:
            if s.count(item) != t.count(item):
                res = False
                break
        return res
