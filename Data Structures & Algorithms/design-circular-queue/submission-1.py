class ListNode:
    def __init__(self, val=0, prev=None, nex=None):
        self.val, self.prev, self.nex = val, prev, nex

class MyCircularQueue:

    def __init__(self, k: int):
        self.space = k # remember the node limit
        self.count = 0
        # make dummy nodes
        self.left = ListNode()
        self.right = ListNode()
        # point dummies to each other
        self.left.prev, self.left.nex = self.right, self.right
        self.right.prev, self.right.nex = self.left, self.left


    def enQueue(self, value: int) -> bool:
        # if full, return false
        if self.isFull(): return False

        # add node
        newNode = ListNode(value, self.right.prev, self.right)
        # update niehgobrs
        self.right.prev = newNode
        newNode.prev.nex = newNode
        # update count
        self.count += 1

        # return True
        return True

    def deQueue(self) -> bool:
        # if self is empty, return false
        if self.isEmpty(): return False

        # remove first element
        self.left.nex = self.left.nex.nex
        self.left.nex.prev = self.left

        # update count
        self.count -= 1
        
        return True

    def Front(self) -> int:
        # if empty return -1
        if self.isEmpty(): return -1

        # first elem
        return self.left.nex.val

    def Rear(self) -> int:
        if self.isEmpty(): return -1
        return self.right.prev.val

    def isEmpty(self) -> bool:
        return self.left.nex == self.right

    def isFull(self) -> bool:
        return self.space == self.count
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()