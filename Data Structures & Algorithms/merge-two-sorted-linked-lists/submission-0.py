# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = tail = ListNode()

        while list1 and list2: # while both list are not empty
            if list1.val < list2.val: # if next node should be from list 1
                tail.next = list1 # make list1 next part of tail
                list1 = list1.next # move list1 pointer
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next #update pointer
        
        # if one list still has stuff remaining
        tail.next = list1 or list2

        return dummy.next # dummy is empty node, empty "head" before the actual head (it has no val)