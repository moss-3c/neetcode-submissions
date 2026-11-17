"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: # empty list
            return None

        # first pass: copies of nodes only
        # !hash map to map old to new copy
        nodes = {None: None}
        newHead = newNode = Node(head.val, None, None) # (head,next,random)
        cur = head
        while cur:
            newNode.val = cur.val
            nodes[cur] = newNode
            if cur.next:
                newNode.next = Node(cur.next.val, None, None)
            cur, newNode = cur.next, newNode.next
        
        # 2nd pass: set random ptrs
        cur = head
        while cur:
            nodes[cur].random = nodes[cur.random] # cur2's random become random2
            cur = cur.next

        return newHead

        