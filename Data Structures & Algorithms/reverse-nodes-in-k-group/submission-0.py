# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def getlen(node):
            count = 0
            while node and count < k: # stop when run out of node, or when segment long enough
                count += 1
                node = node.next

            return (count, node)  # node=nexthead. 

        def reverse(k, node, prevtail): # recursion. node=start of segment, k=k, prevtail=end of prev segmtnet
            count, nexthead = getlen(node)
            # base case: remaining len < k
            if count < k:
                return

            # non-base case:
            # ? -> 2 -> 3 -> ?  k=2 (exaplme)
            # ? -> 3 -> 2 -> ? (reverse the list) 
            curr = node
            prev = None
            while curr != nexthead:
                # save
                temp = curr.next
                # reverse
                curr.next = prev
                # move train
                prev = curr
                curr = temp

            # connect both ends of segment to rest of list 
            # make tail of revrsed list (node) point to 2.next (save this at beginning (nexthead))
            # # ? -> 3 -> (2 -> ?)
            #              ^node
            #                   ^nexthead
            node.next = nexthead

            # prevtail.next point to end of og non-reversed segment (curr=nexthead atp, so prev=end)
            # # (? -> 3) -> 2 -> ?
            #    ^prevtail
            #    ^cur ^prev
            prevtail.next = prev

            # reverse next segment
            reverse(k, nexthead, node)
        
        # the head will change. keep track of ehead
        dummy = ListNode(0, head)
        reverse(k, dummy.next, dummy) # prevtail of 1st segment is just dumy

        return dummy.next


