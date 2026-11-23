# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # fast and slow ptr: find halfway pt of list
        fast = slow = head
        while fast and fast.next:
            if not fast.next.next:
                break # edge case: list w/even number of elements
            slow = slow.next
            fast = fast.next.next

        # chop it in half (slow points to null)
        # save first node f 2n
        l2 = slow.next
        slow.next = None # slow=last node of first list, fast=at end of 2nd list

        # reverse second half
        prev = None
        while l2:
            temp = l2.next 
            l2.next = prev # revrse ptr

            # move train
            prev = l2
            l2 = temp
            

        # join alternately
        # l2 = null
        l1 = head
        l2 = prev
        while l1 and l2:
            # l1, l2, l1, l2.....
            l1n, l2n = l1.next, l2.next
            l1.next = l2
            l2.next = l1n

            l1, l2 = l1n, l2n
        
        
            