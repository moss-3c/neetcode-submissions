class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
    
        # edge cases: nums len 1, k = 0
        if k == 0:
            # i j can never be distinct --> True not possible
            return False
        
        if len(nums) == 1:
            # you can't really have two distinct indices with one element
            return False

        

        i, j = 0, 1
        n = len(nums)

        # O(2n) time
        # O(1) space
        
        # iterate through nums
        # set should have previous k elements, not including curr element (i)
        for i in range(len(nums)):
            # check for match
            if nums[i] in window:
                return True
            else: # if no match
                # add curr elem to set
                window.add(nums[i])
                if i - k >= 0:
                    window.discard(nums[i - k]) # this elem will be outside window next loop itr
                

        
        return False

