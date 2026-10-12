class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # edge case:
        if len(nums) == 0:
            return 0

        i = 0
        end = len(nums) - 1
        while (i < end):
            # if match, take num at end
            if nums[i] == val:
                nums[i] = nums[end]
                end -= 1
                continue
            i += 1
        
        if nums[i] == val:
            return i
        else:
            return i+1