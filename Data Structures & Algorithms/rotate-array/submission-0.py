class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        res = [0] * n

        for i in range(n):
            new_i = (i + k) % n
            res[new_i] = nums[i]
        
        nums[:] = res
        