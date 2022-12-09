# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        # dummyHead = ListNode()
        dummy = ListNode(next =head)
        slow = fast =  dummy
        for _ in range(left):
            slow = fast
            fast = fast.next
            
            
        tail = cur = fast
        for _ in range(left,right+1) :
            temp = cur.next
            cur.next = slow.next
            slow.next = cur
            cur = temp
        tail.next = cur
        
        return dummy.next






        
