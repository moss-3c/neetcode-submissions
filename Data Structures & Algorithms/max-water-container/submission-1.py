class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxvol = 0

        while l < r:
            maxvol = max(maxvol, (r - l) * min(heights[l], heights[r]))
            # get rid of the shorter wall
            if heights[r] < heights[l]:
                r -= 1
            else:
                l += 1
        
        return maxvol
