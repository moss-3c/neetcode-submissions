class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # LOWER BOUND: max(nums)
        # UPper bound: sum(nums
        # can u split input array in <= k groups where maxsum = mid? greedy

        def canFind(largest):
            subarrs = 0
            currSum = 0
            for n in nums:
                currSum += n
                if currSum > largest:
                    subarrs += 1
                    currSum = n

            # count last subarr
            subarrs += 1

            return subarrs <= k

        l, r = max(nums), sum(nums)
        res = r
        while l <= r: # standard binary search
            m = l + (r - l) // 2
            if canFind(m):
                res = m
                r = m - 1
            else:
                l = m + 1
        
        return res