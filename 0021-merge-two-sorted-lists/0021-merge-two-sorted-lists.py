# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        head = dummy
        while list1 and list2: 
            head.next = ListNode(min(list1.val,list2.val))
            if list1.val < list2.val:  
                list1 = list1.next
            else:
                list2 = list2.next
            head = head.next
        if list1:
            while list1:
                head.next = ListNode(list1.val)
                list1 = list1.next
                head = head.next
        if list2:
            while list2:
                head.next = ListNode(list2.val)
                list2 = list2.next
                head = head.next
                
        return dummy.next
        