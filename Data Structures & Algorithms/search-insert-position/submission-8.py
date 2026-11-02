class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if target == nums[m]:
                return m
            elif target < nums[m]:
                r = m - 1 # shrink range to lower half
            else:
                l = m + 1 # shrink range to upper half
        

        return l