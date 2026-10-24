class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # O(n log n)
        people.sort()

        l = 0
        r = len(people) - 1
        boats = 0
        
        #O(n)
        while l < r:
            if people[l] + people[r] <= limit:
                # send them both over
                l += 1
                r -= 1
                # 1 boat used
                boats += 1
            else:
                # if they're too heavy
                # send the heavier one over. heavier person's weight <= limit, guaranteed to work
                r -= 1
                boats += 1
        
        # someone might be left over
        if l == r:
            boats += 1
        
        return boats

            