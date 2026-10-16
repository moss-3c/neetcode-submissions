class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def mergeSort(arr: List[int], l: int, r: int):
            # base case: subarray size 1 (already sorted)
            if l >= r:
                return
            
            m = (l + r) // 2
            mergeSort(arr, l, m)
            mergeSort(arr, m + 1, r)
            merge(arr, l, m + 1, r) # M (m + 1) = start of right arr
        
        def merge(arr: List[int], L: int, M: int, R: int):
            # make copies of left and right
            left, right = arr[L : M], arr[M : R+1] # M = start of right arr
            # create i (index of where to overwrite main arr)
            i = L
            # create pointers in left and right
            j, k = 0, 0

            # while both pointer haven't reached end of their own arr
            while j < len(left) and k < len(right):
                # compare value at j and k, add smaller one to pos i in main arr
                # if they're equal just default to j
                if left[j] <= right[k]:
                    arr[i] = left[j]
                    j += 1 # after putting value at j in main arr, j++
                else:
                    arr[i] = right[k]
                    k += 1
                # pointer i in main arr incremented regardless
                i += 1
            
            # after prev loop, only 1 arr has leftover nums
            # so only one of the following loop will run
            # each loop adds their subarray's leftover nums into main
            while j < len(left):
                arr[i] = left[j]
                i += 1
                j += 1
            
            while k < len(right):
                arr[i] = right[k]
                i += 1
                k += 1
            

        mergeSort(nums, 0, len(nums) - 1)

        return nums
