class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        h = []
        res = []

        for i in range(k):
            heapq.heappush(h, (-nums[i], i))
        
        for l in range(len(nums) - k + 1):
            while h[0][1] < l:
                heapq.heappop(h)

            # append to result
            res.append(-h[0][0])

            # add next num to heap
            if l + k < len(nums):
                heapq.heappush(h, (-nums[l + k], l + k))
        
        return res
        
