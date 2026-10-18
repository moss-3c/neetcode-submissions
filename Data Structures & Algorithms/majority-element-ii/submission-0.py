class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}
        res = []
        for num in nums:
            count[num] = 1 + count.get(num, 0)
            if count[num] > len(nums) // 3 and num not in res:
                res.append(num)
                if len(res) == 2:
                    return res
        
        return res