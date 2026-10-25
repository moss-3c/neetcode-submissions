class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # max element initially last index
        n = len(arr)
        maxnum = arr[n - 1]

        for i in range(n - 2, -1, -1):
            temp = arr[i]
            arr[i] = maxnum
            maxnum = max(temp, maxnum)
        
        arr[n - 1] = -1

        return arr
            