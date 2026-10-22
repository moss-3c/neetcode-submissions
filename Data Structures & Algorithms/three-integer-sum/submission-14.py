class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # O(n log n)
        res = []

        for i, val in enumerate(nums):
            l = i + 1
            r = len(nums) - 1

            # check if prev val is the same
            if i > 0 and val == nums[i-1]:
                continue
            
            

            # find triplets
            while l < r:
                tsum = nums[l] + nums[r] + val
                if tsum < 0:
                    # make sum bigger
                    l += 1
                elif tsum > 0:
                    # make sum smaller
                    r -= 1
                else:
                    res.append([nums[l], nums[r], val])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return res
                

            
            



        