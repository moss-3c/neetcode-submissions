class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1copy = nums1[0:m]
        
        i = j = k = 0

        while (i < m and j < n):
            if nums2[j] < nums1copy[i]:
                nums1[k] = nums2[j]
                j += 1
            else:
                nums1[k] = nums1copy[i]
                i += 1
            k += 1
        
        while i < m:
            nums1[k] = nums1copy[i]
            k += 1
            i += 1
        
        while j < n:
            nums1[k] = nums2[j]
            k += 1
            j += 1
                

        