class Solution:
    def good(self, k, piles) -> int:
        time = 0
        for p in piles:
            time += math.ceil(float(p) / k)
        return time
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2
            time = self.good(k, piles)

            if time <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res