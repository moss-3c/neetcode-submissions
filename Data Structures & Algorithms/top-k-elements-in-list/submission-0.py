class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # freq dict
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1; #-1 cuz bucket index

        # make bucket
        buckets = [[] for _ in range(len(nums) + 1)] # cannot do [[]] * len(nums)

        # dict -> buckets
        for key, value in freq.items():
            buckets[value].append(key)

        topK = []
        topindex = len(buckets) - 1
        # return topk
        while (k > 0):
            if len(buckets[topindex]) != 0: # if bucket not empty
                topK.append(buckets[topindex].pop(0))
                k -= 1
            if len(buckets[topindex]) == 0:
                topindex -= 1

        return topK