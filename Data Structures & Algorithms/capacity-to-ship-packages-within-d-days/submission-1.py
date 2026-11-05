class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # upper bound = max weight
        l, r = max(weights), sum(weights)
        res = r

        def canShip(m):
            # test if the weight "works"
            total = 1 # loop won't count last ship
            w = 0
            i = 0
            while i < len(weights):
                if w + weights[i] <= m:
                    w += weights[i]
                    i += 1
                else:
                    total += 1
                    if total > days:
                        return False
                    w = 0
            
            return True

        while l <= r:
            m = (l + r) // 2 
            if canShip(m):
                res = m
                r = m - 1
            else:
                l = m + 1
        
        return res