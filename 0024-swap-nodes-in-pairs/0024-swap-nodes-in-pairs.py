
class Solution(object):
    def swapPairs(self, head):
        if not head: return None
        
        dummy = ListNode(next = head)
        prev,current  = dummy, head
        while current and current.next:

            nxt =current.next.next
            second = current.next

            prev.next = second
            current.next = nxt
            second.next = current
            

            prev =current
            current = nxt


            
        return dummy.next