class Solution:
    def countCommas(self, n: int) -> int:
        curr  = 1000
        res = 0
        while (curr<=n):
            res += n-curr+1
            curr*= 1000
        return res