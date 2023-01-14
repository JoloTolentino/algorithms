# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        def emptyList(node,deque):
            while deque:
                val = deque.popleft()
                node.next = ListNode(val)
                node = node.next
            
            return node

        
        greater = deque()
        lesser = deque()

        dummy = ListNode()
        while head:
            if head.val <x:
                lesser.append(head.val)
            else:
                greater.append(head.val)
            head = head.next 
        
        current = dummy
        current = emptyList(current,lesser)
        current = emptyList(current,greater)         


        return dummy.next
        
