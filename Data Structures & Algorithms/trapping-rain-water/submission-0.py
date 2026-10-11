class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        # prefix max
        prefix = [0] * n
        prefix[0] = height[0]
        for i in range(1, n):
            prefix[i] = max(height[i], prefix[i - 1])

        # prefix suffix
        suffix = [0] * n
        suffix[-1] = height[-1]
        for i in range(n - 2, -1, -1):
            suffix[i] = max(height[i], suffix[i + 1])

        # total area
        water = 0
        for i in range(0, n):
            water += min(prefix[i], suffix[i]) - height[i]
        
        return water