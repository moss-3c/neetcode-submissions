class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # m, n = num elements left to be sorted, in each list
        # m - 1, n - 1 = index

        curr = len(nums1) - 1

        # while there are still elements in both lists to be sorted
        while m > 0 and n > 0:
            # if m is bigger
            if nums1[m - 1] >= nums2[n - 1]:
                nums1[curr] = nums1[m - 1]
                m -= 1
            else:
                nums1[curr] = nums2[n - 1]
                n -= 1

            # if n is bigger
            curr -= 1
        
        while m > 0:
            nums1[curr] = nums1[m - 1]
            curr -= 1
            m -= 1
        
        while n > 0:
            nums1[curr] = nums2[n - 1]
            curr -= 1
            n -= 1
    

        