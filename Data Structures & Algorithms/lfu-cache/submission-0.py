class ListNode():
    def __init__(self, val=None, prev=None, nex=None):
        # val is actually key...the way it's used
        self.val, self.prev, self.nex = val, prev, nex

class LinkedList():
    def __init__(self):
        # map + a list
        self.left = ListNode(0)
        self.right = ListNode(0)

        self.left.nex = self.right
        self.right.prev = self.left
        self.map = {}
    
    def length(self):
        return len(self.map)
    
    def pushRight(self, val): # inserts new node at right of LL
        node = ListNode(val, self.right.prev, self.right) # insert + set node's ptr
        # put it in map
        self.map[val] = node
        nx, pv = node.nex, node.prev
        pv.nex = node # set neighbors ptrs
        nx.prev = node
        

    def pop(self, val): # pop value if it exists
        if val in self.map: # it has to exist..
            node = self.map[val]
            nx, pv = node.nex, node.prev
            pv.nex = nx
            nx.prev = pv
            self.map.pop(val, None) # oh

    
    def popLeft(self): # pop LRU. node to be kicked
        res = self.left.nex.val
        self.pop(self.left.nex.val)
        return res # need res to remove it from key->val map


class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.lfuCnt = 0
        # map key -> val (can be changed to node value / refactor)
        self.valMap = {} 
        # map key -> count (# of times it's been getted())
        self.countMap = collections.defaultdict(int) 

        # map keycount -> linkedlist
        # return empty ll if key doesn't exist
        self.listMap = collections.defaultdict(LinkedList) 
    
    def counter(self, key): # increments number of times key has een used   
        count = self.countMap[key] # get count of key
        self.countMap[key] += 1 # inc
        # remove from prev linked list (ll is based on count)
        self.listMap[count].pop(key) 
        # add to new linkedlist
        self.listMap[count + 1].pushRight(key)

        # if the og min count with nodes is not valid anymore
        if count == self.lfuCnt and self.listMap[count].length() == 0:
            self.lfuCnt += 1

    def get(self, key: int) -> int:
        if key not in self.valMap: # key doesn't exist
            return -1
        
        # inc # times key has been used
        self.counter(key)

        # return key
        return self.valMap[key]
        

    def put(self, key: int, value: int) -> None:
        # edge case
        if self.cap == 0:
            return
        
        # if kicking a node is necessary
        # 1. key has to not exist and 2. currcap = max
        if key not in self.valMap and len(self.valMap) == self.cap:
            deleteme = self.listMap[self.lfuCnt].popLeft() # get ll w/node to be kicked
            # remove from key->val map and key->count map
            self.valMap.pop(deleteme)
            self.countMap.pop(deleteme)
        
        self.valMap[key] = value # key ->val
        self.counter(key)
        # if count of (new? may not be new lol) key is smaller than curr lfucount
        self.lfuCnt = min(self.lfuCnt, self.countMap[key])
        
#Listnode: val, prev, next
#LL: length, pushRight, pop, popLeft, update

#LFU: 
# cap, lfucount, kv (key to val)

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)