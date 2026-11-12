# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = p1 = p2 = ListNode(0, head) # dummy

        for i in range(n):
            p1 = p1.next

        while p1.next:
            p1 = p1.next
            p2 = p2.next
        
        p2.next = p2.next.next

        return dummy.next


