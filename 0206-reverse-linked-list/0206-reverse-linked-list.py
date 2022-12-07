# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        ##previous node
        
        '''
        1. Initialize the last value of the linked list node  
        2. remember to analyze ahead (head.next)
        3. now we need to reverse the list by reasignning the head.next to the reversed list (prev node)
        4. 
        '''
        
        reversedList =None #1
        while head:
            temp  =head.next #2
            head.next = reversedList #3
            reversedList = head #4
            head = temp 
        
        return reversedList
            
            
            