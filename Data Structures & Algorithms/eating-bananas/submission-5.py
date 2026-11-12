class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # k upper bound = max(piles)
        # k lower bound = 1 (or else you will never eat any)

        l, r = 1, max(piles) # O(n)
        # hours taken = ceil(b / k) for each pile
        # k = b/hr
        # eachpile = b
        # want: hr

        # l->r tested #'s 

        res = r
        while l <= r: # l = r means u only have 1 answer left TO  be tested
            # l <= r bc if l=r you still have to test that answer (run loop)
            k = l + (r - l) // 2
            hours = 0
            for b in piles:
                hours += math.ceil(b / k)
            
            if hours <= h: # finish in time -> try slow down (lower k)
                 res = k # but save answer beforehand
                 r = k - 1
            else: # taking too many hours -> speed up (increase k)
                l = k + 1
        
        return res
