class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # upper bound = max weight
        l, r = max(weights), sum(weights)
        res = r

        while l <= r:
            m = (l + r) // 2

            # test if the weight "works"
            total = 1
            w = 0
            i = 0
            while i < len(weights):
                if w + weights[i] <= m:
                    w += weights[i]
                    i += 1
                else:
                    total += 1
                    w = 0
                    
            if total > days:
                # if it takes too many days
                # the ship needs to be bigger
                l = m + 1
            else:
                # if total is short enough
                # maybe the ship can be smaller?
                # try shrinking it: (save result too)
                res = m
                r = m - 1
        
        return res