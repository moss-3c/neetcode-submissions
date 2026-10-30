class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # edge case
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1

        seen = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            res = max(len(seen), res)
        
        return res
            

