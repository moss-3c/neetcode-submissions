class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:

        n = mountainArr.length()

        # FINDING..THE PEAK
        l, r = 1, n - 2
        peak = 0
        while True:
            mid = l + (r - l) // 2
            m = mountainArr.get(mid)
            ml, mr = mountainArr.get(mid - 1), mountainArr.get(mid + 1)

            if ml < m > mr:
                peak = mid
                break
            elif ml > m: # right slope
                r = mid - 1
            else: # left slope
                l = mid + 1
        
        # search left half
        l, r = 0, peak
        while l <= r:
            mid = l + (r - l) // 2
            m = mountainArr.get(mid)

            if m < target:
                l = mid + 1
            elif m > target:
                r = mid - 1
            else:
                return mid

        # search right half
        l, r = peak + 1, n - 1
        while l <= r:
            mid = l + (r - l) // 2
            m = mountainArr.get(mid)

            if m < target:
                r = mid - 1
            elif m > target:
                l = mid + 1
            else:
                return mid
        
        return -1
