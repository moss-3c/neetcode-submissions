class Solution:
    def compress(self, chars: List[str]) -> int:
        read, write = 0, 0
        
        while read < len(chars):
            chars[write] = chars[read]
            write += 1
            next_read = read + 1

            while next_read < len(chars) and chars[next_read] == chars[read]:
                next_read += 1
            
            if next_read - read > 1:
                for c in str(next_read - read):
                    chars[write] = c
                    write += 1
            
            read = next_read
        
        return write

