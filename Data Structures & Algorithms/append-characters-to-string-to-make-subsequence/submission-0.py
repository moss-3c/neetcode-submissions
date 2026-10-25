class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        # space: O(1), time: O(n)

        # num chars of t found while scanning s
        sub = 0

        # scan s
        for i in range(len(s)):
            # case 1: letter matches the one in t
            if t[sub] == s[i]:
                sub += 1
            
            if sub == len(t):
                break
        
        return len(t) - sub


        