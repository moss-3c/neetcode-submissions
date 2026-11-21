class ListNode:
    def __init__(self, key=None, val=None, nex=None, prev=None):
        self.key, self.val, self.nex, self.prev = key, val, nex, prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.nodemap = {} # key=key, val=node
        self.head = ListNode()
        self.tail = ListNode()

        # connect them
        self.head.nex = self.head.prev = self.tail
        self.tail.nex = self.tail.prev = self.head
    
    # remove node
    def remove(self, node):
        p, n = node.prev, node.nex
        p.nex, n.prev = n, p # update neights
        # node ptr doesn't rly matter..
    
    # insert a node (at end honly)
    def insert(self, node):
        p, n = self.tail.prev, self.tail # get neighbors
        p.nex = n.prev = node  # update neighbors
        node.prev, node.nex = p, n # update node

    def get(self, key: int) -> int:
        # key doesn't exist
        if key not in self.nodemap:
            return -1
        
        # update cache # move node to end
        MRUnode = self.nodemap[key]
        self.remove(MRUnode)
        self.insert(MRUnode)

        return self.nodemap[key].val
                

    def put(self, key: int, value: int) -> None:
        # if key exists, update value of key
        if key in self.nodemap:
            self.nodemap[key].val = value # update value
            self.remove(self.nodemap[key])
        else: 
            # add key value to nodemap
            self.nodemap[key] = ListNode(key, value)
        
        # update cache
        self.insert(self.nodemap[key])

        # if capacity exceeded, remove LRU key (ll head)
        if len(self.nodemap) > self.capacity:
            del self.nodemap[self.head.nex.key]
            self.remove(self.head.nex)
