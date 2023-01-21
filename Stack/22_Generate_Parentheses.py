class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
        def rcrson(lst: List[str], txt: str, n: int):
            if txt.count('(') == n and txt.count(')') == n:
                lst.append(txt)
                return lst
            elif txt.count(')') > txt.count('('):
                return
            else:
                if txt.count('(') < n:
                    rcrson(lst, txt+'(', n)
                if txt.count(')') < n:
                    rcrson(lst, txt+')', n)
            return lst
        return rcrson([], "(", n)
