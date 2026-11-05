class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        # edge case: "no" rotation
        if nums[l] < nums[r]:
            return nums[l]

        while l + 1 < r:
            m = (l + r) // 2

            if nums[m] < nums[l]: # m in right segment
                r = m # shrink right side
            else: # m in left segment
                l = m # shrink left side

        return nums[r]
            