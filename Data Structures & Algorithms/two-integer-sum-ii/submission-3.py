class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # L R = start and end
        # when (L-->) L moves right: the sum INCREASES
        # when (R--<) R moves left: the sum DECREASES
        l, r = 0, len(numbers) - 1
        while True: # always one unique answer --> loop will find it somehow
            k = numbers[l] + numbers[r]
            if k > target: # we want to decrease the sum
                r -= 1
            elif k < target: # increase sum
                l += 1
            else:
                return [l + 1, r + 1] # 1-indexed

