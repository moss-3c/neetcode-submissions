class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # hash method: O(n) time, O(n) space
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        for k, v in freq.items():
            if v >= len(nums)//2:
                return k