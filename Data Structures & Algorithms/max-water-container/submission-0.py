class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # edge case
        if len(heights) <= 1:
            return 0

        # two pointer
        left = 0
        right = len(heights) - 1
        max = 0

        # "discard" the smaller pointer
        while (left < right): # before ptrs cross
            # calc area
            area = (right - left) * min(heights[right], heights[left])
            # update max
            if area > max:
                max = area

            # shift ptrs
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        
        return max

            
