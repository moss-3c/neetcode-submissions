class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # upper bound = max weight
        l, r = max(weights), sum(weights)
        res = r

        def canShip(m):
            # test if the weight "works"
            ships = 1 # loop won't count last ship
            currW = 0
            for pkg in weights:
                if currW + pkg > m: # if next pkg exceeds capacity
                    ships += 1 # send a ship
                    # prune
                    if ships > days:
                        return False
                    currW = 0 # reset
            
                currW += pkg
            return True

        while l <= r:
            m = (l + r) // 2 
            if canShip(m):
                res = min(m, res)
                r = m - 1
            else:
                l = m + 1
        
        return res