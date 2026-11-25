class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0: return True # "" is substr of anything
        if len(t) == 0: return False 

        si = 0
        for ti in range(len(t)):
            if si < len(s) and s[si] == t[ti]:
                si += 1

        return si == len(s)
