
class Solution(object):
    def swapPairs(self, head):
        if not head: return None
        
        dummy = ListNode(next = head)
        prev,fast  = dummy, head
        while fast and fast.next:

            # storing
            nxt =fast.next.next
            adj = fast.next
            
            # rearanging
            prev.next = adj
            adj.next = fast
            fast.next = nxt
            
            # updating
            prev =fast
            fast = nxt


            
        return dummy.next