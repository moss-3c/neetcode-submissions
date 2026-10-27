class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1 # place to copy next unique element

        for r in range(1, len(nums)):
            # if a unique element is found
            if nums[r] != nums[r - 1]:
                 # copy unique element to l
                 nums[l] = nums[r]
                 l += 1
        
        # final index of l = # unique elments - 1
        return l
