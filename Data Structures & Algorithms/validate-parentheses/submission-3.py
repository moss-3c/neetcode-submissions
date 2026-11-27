class Solution:
    def isValid(self, s: str) -> bool:
        bracket = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        openbr = ("(", "{", "[")
        stack = []
        for c in s:
            if c in openbr: # open -> add to stack
                stack.append(c)
            elif c in bracket: # close br -> stack.pop must match
                if not stack or bracket[c] != stack.pop():
                    return False
        
        return not stack
        