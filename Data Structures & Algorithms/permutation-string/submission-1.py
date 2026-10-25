class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # edge case
        if len(s2) < len(s1):
            return False

        s1freq = [0] * 26 # char freq of substr (substr = last len(s1) chars)
        s2freq = [0] * 26 # fixed, won't change
        k = len(s1) - 1 # k = window size. l - r ptr

        # build the freq of s1 (this won't change)
        for c in s1:
            s1freq[ord(c) - ord('a')] += 1

        # add the first len(s1) - 1 letters of s2 into freq
        # kth letter will be added by comparison loop
        for i in range(k):
            char_idx = ord(s2[i]) - ord('a')
            s2freq[char_idx] += 1

        # move the sliding window along s1 and compare freq's repeatedly
        # i = left most element in curr window
        for i in range(len(s2) - k):
            # add new elem that came into window
            s2freq[ord(s2[i + k]) - ord('a')] += 1
            # compare
            if s1freq == s2freq:
                return True
            else:
                # remove leftmost element in window
                s2freq[ord(s2[i]) - ord('a')] -= 1
        
        return False
        