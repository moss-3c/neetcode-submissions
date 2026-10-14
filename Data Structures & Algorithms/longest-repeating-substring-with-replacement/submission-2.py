class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        left = 0
        freq = {}

        for i in range(len(s)):
            freq[s[i]] = freq.get(s[i], 0) + 1

            # while window is invalid
            # invalid = window size - most freq of window > k
            while (i - left + 1) - max(freq.values()) > k:
                freq[s[left]] -= 1
                left += 1
            
            res = max(i - left + 1, res)
        
        return res