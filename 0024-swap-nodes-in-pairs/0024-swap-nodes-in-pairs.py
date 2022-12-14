
class Solution(object):
    def swapPairs(self, head):
        if not head: return None
        
        dummy = ListNode(next = head)
        prev,fast  = dummy, head
        while fast and fast.next:

            nxt =fast.next.next
            adj = fast.next

            prev.next = adj
            fast.next = nxt
            adj.next = fast
            

            prev =fast
            fast = nxt


            
        return dummy.next