class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": 
            return ""

        countT, window = {}, {}

        # make countT map
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        
        have = 0
        need = len(countT)

        res = [-1, -1] # l and r ptr
        resLen = float("infinity") # any val is less than inf

        l = 0
        for r in range(len(s)):
            char = s[r]
            window[char] = 1 + window.get(char, 0)

            # check if curr char satisfies
            if char in countT and window[char] == countT[char]:
                have += 1
            
            # shrink window from left try tofind min len
            while have == need:
                # update result (potentially)
                # if window size < result len
                if r - l + 1 < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                
                # shrink left side of window
                window[s[l]] -= 1 # pop char
                if s[l] in countT and window[s[l]] < countT[s[l]]: #works even if dupes
                    have -= 1
                l += 1 # shrink winddow
        
        l, r = res
        # r + 1 bc splicing is not inclusive
        return s[l:r+1] if resLen != float("infinity") else ""



