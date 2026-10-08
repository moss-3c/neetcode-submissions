class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        max_count = 0

        for num in hashset:
            # if num start of a sequence
            if num - 1 not in hashset:
                count = 1
                next_num = num + 1
                # count the sequence size
                while (next_num in hashset):
                    count += 1
                    next_num += 1
                
                # if seq size is larger, update max
                if count >= max_count:
                    max_count = count
                
        return max_count
