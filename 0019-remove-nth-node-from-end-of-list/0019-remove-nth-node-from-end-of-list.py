class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy_head = ListNode(0,head)
        first = dummy_head.next
        
        for _ in range(n):
            first =first.next
        
        second = dummy_head
        
        while first:
            first,second = first.next,second.next
        
        second.next = second.next.next
        return dummy_head.next