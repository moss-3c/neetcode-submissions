class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nummies = set(nums)
        maxseq = 1

        # edge case
        if len(nums) == 0:
            return 0

        for num in nummies: #O(n)
            # if its the start of a sequence, 
            if num - 1 not in nummies:
                seq = 1
                curr = num
                # start counting
                while curr + 1 in nummies: 
                    #O(n) but will only count nums not selected by outer loop 
                    # no number will be selected twice bc it can't be part of 2 separate sequences
                    # in total the whole thing is still O(2n). each num iterated over twice max
                    # ig you could make each num iterated over once only. but would need another
                    # hash set as reference bc you can't edit the hash set while looping over it
                    seq += 1
                    curr += 1
                # update max if found
                maxseq = max(seq, maxseq)


        return maxseq

