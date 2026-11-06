class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # edge case
        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        def findPivot():
            # if not rptated
            if nums[0] < nums[-1]:
                return 0
            
            # now
            l, r = 0, len(nums) - 1
            while l + 1 < r:
                m = (l + r) // 2
                if nums[m] > nums[l]: # m in left side
                    l = m
                else:
                    r = m
            
            return r
        
        pivot = findPivot()
        if pivot == 0:
            l, r = 0, len(nums) - 1 # edge case not rotated
        elif target >= nums[0]:
            l, r = 0, pivot - 1
        else:
            l, r = pivot, len(nums) - 1
        
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1

        return -1