# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev, curr = None, head
        while curr:
            temp = curr.next # keep track of next
            curr.next = prev # flip ptr

            # move train
            prev = curr
            curr = temp

        return prev
