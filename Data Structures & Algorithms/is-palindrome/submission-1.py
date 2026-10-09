class Solution:
    def isPalindrome(self, s: str) -> bool:
        # strip string
        filtered = [char.lower() for char in s if char.isalnum()]

        # edge case: length = 1 
        if len(filtered) <= 1:
            return True

        # initialize pointers
        start = 0
        end = len(filtered) - 1

        # move pointers & compare (loop)
        while (True):
            # if not match -> false
            if filtered[start] != filtered[end]:
                return False
            
            # move pointers
            start += 1
            end -= 1

            # if pointers have crossed/met
            if start >= end:
                break
            

        return True
        
        # space: O(n)
        # time: O(n)

    