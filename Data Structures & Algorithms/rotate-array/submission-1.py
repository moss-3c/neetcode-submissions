class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        start = -1
        moved = 0

        while (moved < n):
            # if moved < len(nums)
            start += 1
            i = start
            prev = nums[start]

            # move element forward the correct amount
            while (True):
                # move i forward
                i = (i + k) % n
                # move prev element to i
                nums[i], prev = prev, nums[i]
                # after moving an element
                moved += 1

                if (i == start):
                    break
            
            
            
            

            


        