# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = res = ListNode()
        carry = 0

        while l1 or l2 or carry:
            res.next = ListNode()
            res = res.next # make new digit

            # add digit
            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0
            summ = n1 + n2 + carry
            res.val = summ % 10 # 10 -> 0 + carry=1

            # carry?
            carry = summ // 10

            # update l1/l2
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
        
        return dummy.next