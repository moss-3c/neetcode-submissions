class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # O(N) space, O(n) time
        has = set()
        for n in nums:
            has.add(n)
        
        i = 1
        while(True):
            if i not in has:
                return i
            i += 1