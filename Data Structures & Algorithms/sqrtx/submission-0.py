class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0: return 0
        if x == 1: return 1

        l = 1
        r = x // 2

        while l <= r:
            m = (l + r) // 2
            sq = m ** 2

            if sq > x:
                r = m - 1
            elif sq < x:
                if (m + 1) ** 2 > x:
                    return m
                else:
                    l = m + 1
            else: # perfect sq
                return m

