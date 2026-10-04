class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_dict = {}
        t_dict = {}

        # .get returns default value (0) if key not found
        for char in s:
            s_dict[char] = s_dict.get(char, 0) + 1

        for char in t:
            t_dict[char] = t_dict.get(char, 0) + 1
        
        if s_dict == t_dict:
            return True
        else:
            return False
            