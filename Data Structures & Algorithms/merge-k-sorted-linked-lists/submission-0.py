# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(l1, l2): # merge two list and return the head
            #todo
            dummy = cur = ListNode()

            while l1 and l2: # if l2 is none loop is skipped
                if l1.val < l2.val:
                    cur.next = l1
                    l1 = l1.next
                else:
                    cur.next = l2
                    l2 = l2.next
                cur = cur.next
            
            cur.next = l1 or l2 # append the rest
            
            return dummy.next

        # mergesort but the unit is 1 linked list not 1 node
        # edge case
        if not lists or len(lists) == 0: return None # [] means None apparently???

        while len(lists) > 1: # while there is more than 1 thing to sort
            merged = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                merged.append(merge(l1, l2)) # no extra nodes being created

            lists = merged # make it go through the merged ver. mergesort...

        return lists[0]
            

        
      