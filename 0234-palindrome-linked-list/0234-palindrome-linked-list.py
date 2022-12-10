# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        def reverseList(node):
            slow,fast = None, node
            while fast: 
                temp = fast.next 
                fast.next = slow
                slow = fast 
                fast = temp
            return slow 
        
        second = first = head

        while first and first.next:
            first = first.next.next 
            second = second.next
        

        second = reverseList(second)
        
        while second:
            if head.val!= second.val:
                return False
            second,head = second.next,head.next
        return True