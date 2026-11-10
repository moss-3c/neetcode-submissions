# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        while head:
            # if node has been visited
            if head.val == float("infinity"):
                return True
            head.val = float("infinity")
            head = head.next
        
        return False