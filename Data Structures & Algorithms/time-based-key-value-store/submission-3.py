class TimeMap:

    def __init__(self):
        self.timemap = {}
        # key: alice
        # value: [[time, val], [time, val], ... ]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timemap:
            self.timemap[key] = []
        self.timemap[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        # get the list of time, val
        if key not in self.timemap:
            return ""
        
        data = self.timemap[key] # get the array of pairs
        # do a binary search for the pair <= timestamp
        l, r = 0, len(data) - 1
        # timestamp too small
        if timestamp < data[0][0]:
            return ""

        res = ""   # l and r = we didnt check these nums yet
        while l <= r:
            m = (l + r) // 2
            if data[m][0] <= timestamp: # m < time
                res = data[m][1]
                l = m + 1 # chop off left half
            else: # m > time
                r = m - 1 # chop off the right half
        
        return data[r][1]
        
