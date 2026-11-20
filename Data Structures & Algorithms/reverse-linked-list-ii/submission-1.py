# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = l1 = ListNode()
        dummy.next = head
        # r1 may be None
        # l1 wn't be None bc dummy node
        # l1 = node before l, r1 = node after l

        # find l and l1
        for i in range(1, left):
            l1 = l1.next
        
        l = l1.next

        # reversal
        r = l
        r1 = r.next
        curr = l # bc still need l for end of reverse train point to l
        for j in range(left, right):
            # shift train
            curr = r 
            r = r1
            r1 = r1.next if r1 else None

            r.next = curr # reverse ptr
            
            
            
        # l1 -> r -> (reversed) -> l -> r1
        l1.next = r
        l.next = r1

        return dummy.next