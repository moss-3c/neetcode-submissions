class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # edge case
        if len(nums) == 1:
            return (1 if nums[0] == target else 0)
        
        l = 0
        res = float("inf")
        total = 0

        for r in range(len(nums)):
            total += nums[r]

            # while total is valid, try making window smaller
            while total >= target:
                res = min(r - l + 1, res)
                # bc window shrinking, remove value
                total -= nums[l]
                # will never increment past r+1 bc total will =0 
                l += 1


        return 0 if res == float("inf") else res
            

