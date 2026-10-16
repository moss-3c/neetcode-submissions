class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # l is the index where next 0 should be place
       l, i = 0, 0
       r = len(nums) - 1

       while i <= r:
            if nums[i] == 0: 
                # swap 0 to 0's area
                nums[l], nums[i] = nums[i], nums[l]
                l += 1
                i += 1

            # if nums[i] == 1: skip
            elif nums[i] == 1:
                i += 1
            
            else: # nums[i] == 2
                # put 2 in the 2's area
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
                # i not incremented, this index in arr must be re-evaluated
    