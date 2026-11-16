class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1
        
        dupes = set()
        l, r = 0, 0

        res = 0

        for r in range(len(s)):
            while s[r] in dupes:
                res = max(res, r - l) # not sure. whats the length??
                dupes.remove(s[l])
                l += 1
            
            dupes.add(s[r])
        
        res = max(res, r - l + 1)
        

        return res

