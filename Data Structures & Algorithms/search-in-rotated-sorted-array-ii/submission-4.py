class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return True
            elif nums[l] < nums[m]: # m is in left segment
                if nums[l] <= target < nums[m]: # if target in left, search left side
                    r = m - 1
                else: 
                    l = m + 1
            elif nums[l] > nums[m]: # m is in right segment
                # if target in right
                if nums[m] < target <= nums[r]:
                    l = m + 1 # search right
                else:
                    r = m - 1
            else:
                l += 1 # can't tell what segment we're in
        
        return False