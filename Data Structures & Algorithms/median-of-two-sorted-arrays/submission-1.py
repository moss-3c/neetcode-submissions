class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(A) > len(B): # make A shorter
            A, B = B, A
        
        # try to find the proper "left" segment of both arr
        # either 0 of A is in left segment, or up to all of A
        # idx: -1 -> -inf, >=len -> +inf
        # l->r: means nothing just break out when you find suitable number (it must exist)

        
        total = len(A) + len(B)
        left = total // 2 # of elements in left (not idx)
        
        l, r = 0, len(A) - 1 # range of "try to include # up to this idx (inclusive) in A"
        while True:
            m1 = l + (r - l) // 2 # m = pretned # up to this idx = in left segment
            m2 = left - m1 - 2 # if m1 = 0, left = 2 --> m2 = 0 .m2(0) = left(2) - m1(0) - 2

            # get the. actual values
            Aleft = A[m1] if m1 >= 0 else float('-infinity')
            Bleft = B[m2] if m2 >= 0 else float('-infinity')
            Aright = A[m1 + 1] if m1 + 1 < len(A) else float('infinity')
            Bright = B[m2 + 1] if m2 + 1 < len(B) else float('infinity')

            if Aleft <= Bright and Bleft <= Aright: #it works
                if total % 2 == 0: # if arr is even, median is avg of max(left) min(right)
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
                # if arr is odd, median is first # in combined right segment
                return min(Aright, Bright)
            elif Aleft > Bright: # too many # from in left half
                r = m1 - 1 # chop off right candidates
            else: # not enough # from A in left half
                l = m1 + 1 # chop off left candidates



        