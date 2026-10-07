class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        product = 1
        prefix.append(1)
        for i in range(1, len(nums)):
            product *= (nums[i-1])
            prefix.append(product)
        
        suffix = [0] * len(nums)
        suffix[len(nums) - 1] = 1
        product = 1
        for i in range(len(nums)-1, 0, -1):
            product *= nums[i]
            suffix[i - 1] = product

        res = []
        for i in range(len(nums)):
            res.append(prefix[i] * suffix[i])
        
        return res