class Solution:
    def calPoints(self, operations: Lisc[str]) -> int:
        sc = []
        for op in operations:
            if op == "+": # sum of prev 2
                sc.append(sc[-1] + sc[-2])
            elif op == "D": # double prev
                sc.append(sc[-1] * 2)
            elif op == "C": # clear prev
                sc.pop()
            else: # integer
                sc.append(int(op))  # needs cast bc ur given arr of strings
        
        return sum(sc)

            