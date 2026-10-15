class MyHashSet:

    def __init__(self):
        # array with linked list
        self.TABLE_SIZE = 10000
        self.table = [[] for _ in range(self.TABLE_SIZE)]


    def add(self, key: int) -> None:
        i = key % self.TABLE_SIZE
        if key not in self.table[i]: # disallow dupes
            self.table[i].append(key)

    def remove(self, key: int) -> None:
        i = key % self.TABLE_SIZE
        if key in self.table[i]: # prevent throw error
            self.table[i].remove(key)
        

    def contains(self, key: int) -> bool:
        return (key in self.table[key % self.TABLE_SIZE])
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)