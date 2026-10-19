class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre = {0 : 1}
        sum = 0
        res = 0

        # key = sum
        # value = num times sum has appeared
        for num in nums:
            sum += num
            res += pre.get(sum - k, 0)
            pre[sum] = 1 + pre.get(sum, 0)
        
        return res

