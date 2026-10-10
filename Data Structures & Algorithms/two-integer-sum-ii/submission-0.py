class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # initialize 2 pointers
        start = 0
        end = len(numbers) - 1
        testSum = numbers[start] + numbers[end]

        while (testSum != target):
            # slide ptrs
            if testSum > target:
                end -= 1
            if testSum < target:
                start += 1
            # update testSum of new pointers
            testSum = numbers[start] + numbers[end]

            # a unique answer is guaranteed, no handling of ptrs crossing

        return [start + 1, end + 1]