# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # slow = end of first half
        # beginning of 2nd half
        second = slow.next
        slow.next = None # tail of 2nd half after reversal. tails always point to nothing
        prev = None # the node to point to, during reversal

        while second:
            temp = second.next
            second.next = prev

            #move th train
            prev = second
            second = temp
        
        # merge both halves of list
        second = prev
        first = head

        while second: # second half len will be shorter or equal to first
            t1, t2 = first.next, second.next # temp =saving the next
            first.next = second
            second.next = t1

            # move the train
            first, second = t1, t2
            


        

