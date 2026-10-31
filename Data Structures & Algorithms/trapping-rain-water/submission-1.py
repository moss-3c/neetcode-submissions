class Solution:
    def trap(self, height: List[int]) -> int:
        # edge case
        # need at least 3 indicies to trap water
        if len(height) < 2:
            return 0

        n = len(height)
        leftmax = [0] * n
        rightmax = [0] * n

        leftmax[0] = height[0]
        for i in range(1, n):
            leftmax[i] = max(leftmax[i - 1], height[i])
        
        
        rightmax[n - 1] = height[n - 1]
        for j in range(n - 2, -1, -1):
            rightmax[j] = max(rightmax[j + 1], height[j])
        
        vol = 0
        for k in range(n):
            # water trapped at each index
            # min(leftmax, rightmax) - height[i] <- cannot be <0
            vol += max(0, min(leftmax[k], rightmax[k]) - height[k])
        
        return vol
        
