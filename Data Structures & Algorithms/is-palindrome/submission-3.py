class Solution:
    def isPalindrome(self, s: str) -> bool:
        # strip string
        filtered = [char.lower() for char in s if char.isalnum()]
        return filtered == filtered[::-1]  
        
        # space: O(n)
        # time: O(n)

    