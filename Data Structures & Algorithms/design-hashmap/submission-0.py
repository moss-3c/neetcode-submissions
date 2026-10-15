class ListNode:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:
    def __init__(self):
        self.set = [ListNode(0, 0) for _ in range(10**4)]

    def put(self, key: int, value: int) -> None:
        cur = self.set[key % len(self.set)]
        while cur.next:
            cur = cur.next # go to end of list
            # if key already exists, update corresponding value
            if cur.key == key: 
                cur.value = value
                return
        
        # insert key
        cur.next = ListNode(key, value)

    def get(self, key: int) -> int:
        cur = self.set[key % len(self.set)]
        while cur.next:
            cur = cur.next
            # if key exists, return its value
            if cur.key == key: 
                return cur.value
        
        # key does not exist
        return -1

    def remove(self, key: int) -> None:
        cur = self.set[key % len(self.set)]
        while cur.next:
            # if key exists, remove key and corresponding value
            if cur.next.key == key: 
                cur.next = cur.next.next
            else:
                cur = cur.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)