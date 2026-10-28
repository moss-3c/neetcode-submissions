class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # get the frequencies
        count = {}
        maxcount = 0 # used to make the bucket array
        for n in nums:
            count[n] = 1 + count.get(n, 0)
            maxcount = max(maxcount, count[n])

        # put them into frequency buckets
        # index 1 = appears 1 time, 2 = 2x...etc
        count_arr = [[] for _ in range(maxcount + 1)]
        for key, val in count.items():
            count_arr[val].append(key)

        # extra top k elements from nested arr
        res = []
        curr = len(count_arr) - 1
        for i in range(k):
            # if arry is empty
            while not count_arr[curr]:
                curr -= 1

            res.append(count_arr[curr].pop(-1))

        
        # return top k (rightmost) elements of arr
        return res

        # technique: make array index mean something