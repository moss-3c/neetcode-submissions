class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set(nums)
        return not len(seen) == len(nums)