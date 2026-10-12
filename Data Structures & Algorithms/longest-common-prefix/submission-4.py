class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
            
        if len(strs) == 1:
            return strs[0]

        prefix = strs[0]
        for str in strs:
            for i in range(len(prefix)):
                if i == len(str) or str[i] != prefix[i]:
                    prefix = str[:i]
                    break
        
        return prefix