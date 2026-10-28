class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        # prefixing (in place)
        res[0] = 1
        prod = res[0]
        for i in range(1, len(res)):
            prod *= nums[i - 1]
            res[i] = prod
        
        # suffixing (in place)
        # last num stays the same
        prod = 1
        for i in range(len(res) - 2, -1, -1):
            prod *= nums[i + 1]
            res[i] *= prod
        
        return res
