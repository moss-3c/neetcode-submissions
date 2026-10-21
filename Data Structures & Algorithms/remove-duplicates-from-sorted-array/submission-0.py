class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # edge case
        if (len(nums) == 1):
            return 1

        k = 0
        next = 1

        while next < len(nums):
            if nums[next] != nums[k]:
                nums[k + 1] = nums[next]
                k += 1
            
            next += 1

        return k + 1