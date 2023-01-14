# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def getLastNode(node):

            while node and node.next and node.next.next: 
                node = node.next
            
            last_node = node.next if node.next else node
            node.next = None 
            return last_node

        def validLength(node):
            count = 0 
            while node: 
                node = node.next
                count+=1
             
            return True if count >1 else False,count 

        validity,total = validLength(head)
        
        if head and validity:
            k-= (k//total)*total
            count = 0   
            prev_head = head  
            while count<k: 
                new_head = getLastNode(head)
                new_head.next = prev_head
                prev_head = new_head
                head = new_head
                count +=1 
            return head
        else:
            return head
