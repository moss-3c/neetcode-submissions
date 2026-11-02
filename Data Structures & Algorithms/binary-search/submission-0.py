class Solution:
    def bsh(self, l, h, nums, target) -> int:
            m = (l + h) // 2

            # check mid?
            if target == nums[m]:
                return m

            # base case: window size 1 and mid not found
            if l == h:
                return -1
            
            # window size >1 and mid not found
            if target < nums[m]:
                # search lower half
                return self.bsh(l, m, nums, target)
            else:
                # search upper half
                return self.bsh(m + 1, h, nums, target)
            
    def search(self, nums: List[int], target: int) -> int:
        return self.bsh(0, len(nums) - 1, nums, target)
    
    

        
        
        