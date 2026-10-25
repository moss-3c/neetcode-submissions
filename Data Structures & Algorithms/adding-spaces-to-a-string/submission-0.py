class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        j = 0 # ptr to spaces
        res = []

        for i in range(len(s)):
            if j < len(spaces) and i == spaces[j]:
                res.append(' ')
                j += 1
            res.append(s[i])
        
        return ''.join(res)
