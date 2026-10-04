class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # key = the number, value = the number's index in nums array
        # no dupe keys bc only 1 solution
        seen = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            lookup = seen.get(diff)
            # if we've seen the number before
            if lookup != None:
                return [lookup, i]  
                # lookup = smaller index bc check arr in ascedning order
            else:
                seen.update({nums[i]: i})
                


