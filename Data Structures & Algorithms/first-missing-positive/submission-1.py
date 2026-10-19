class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # go through every value, change to 0 if neg
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
        
        #go through every value
        # "mark" it as existent at the correct index
        # by making the num there neg
        for i in range(len(nums)):
            value = abs(nums[i])
            index = value - 1

            # if index out of bounds
            if index < 0 or index >= len(nums):
                continue

            # avoid marking og neg number as "existent"
            if nums[index] == 0:
                nums[index] = -1 - len(nums)
            else:
                # avoid positiving a neg value
                if nums[index] > 0:
                    # 1 at i=0, etc.
                    nums[index] *= -1
    
        # return index+1 of first pos value
        i = 0
        while i < len(nums):
            if nums[i] >= 0:
                return i + 1
            i += 1
        
        return i + 1