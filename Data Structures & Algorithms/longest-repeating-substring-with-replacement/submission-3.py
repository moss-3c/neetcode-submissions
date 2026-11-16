class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0) # update freq dict
            maxf = max(maxf, count[s[r]]) # update true max frequency (ever)

            # WHILE WINDOW IS VALID
            # don't care what the actually most freq char is. 
            # ^^^^^^IMPORTANT
            # eg window size 5 but its all AAAAA -> r-l+1-maxf will be 0 < k
            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1 # similar to prev problem. take this OUT of the dict
                l += 1 # shrink window
            res = max(res, r - l + 1) # not in the while loop cuz when the while loop is running window not valid
            # it worked in the prev problem cuz when you run into "bad" letter, 
            # the window before (r - l + 1 - 1) still valid
        
        return res