class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        sqrtlist = []
        for x in points:
            value = sqrt((((x[0] - 0) ** 2) + ((x[1] - 0) ** 2)))
            sqrtlist.append((value, x))
        srt = sorted(sqrtlist, key=lambda tup: tup[0])
        res = []

        for i in range(0, k):
            res.append(srt[i][1])

        return res
