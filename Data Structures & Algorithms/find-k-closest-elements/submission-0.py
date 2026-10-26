class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # l = left bound of m
        # r = right bound of m
        # m = potential start of window
        l, r = 0, len(arr) - k

        
        while l < r:
            m = (l + r) // 2

            # works whether x is inside or outside window
            # compare m with value just outside window arr[m + k]
            if x - arr[m] > arr[m + k] - x:
                # if value just outside right of window is c;pser (window starts at m)
                # shift window to the right (l is the mininmum possible m)
                l = m + 1
            else:
                # else don't go further right (r is the max possible value of m)
                r = m # not mid - 1. correct window might still start at m
            
            # loop ends when l == r (min possilbe val of m = right possible val)
        
        return arr[l:l+k]