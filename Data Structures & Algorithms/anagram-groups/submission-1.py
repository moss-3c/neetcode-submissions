class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_maps = {} #key: freq map of a word, value: its index in the output array
        nth_anagram = 0 # the nth anagram encountered
        output = []

        for str in strs:
            # make the freq map for word (array)
            word_map = [0] * 26
            for char in str:
                word_map[ord(char) - ord('a')] += 1
            
            # convert to tuple (unmutable) 
            # so it can be used as dict key
            freq_key = tuple(word_map)

            # where in output list word should go
            output_index = freq_maps.get(freq_key)

            # if that anagram doesn't exist
            if output_index == None:
                # put in freq_maps
                freq_maps[freq_key] = nth_anagram
                nth_anagram += 1
                output.append( [str] )
            else:
                output[output_index].append(str) # add word
            
        return output