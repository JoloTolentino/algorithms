# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def sortedListToBST(self, head):
        
        if head:    
            slow = fast = head 
            prev = None 
            while fast and fast.next:
                fast = fast.next.next 
                prev = slow
                slow = slow.next 
            
            root = TreeNode(slow.val) 
            
            if prev:
                prev.next = None  # detach left side
            else:
                head = None # if prev is none set head to none to avoid cycle

            root.left = self.sortedListToBST(head) # run using the original head again to until all nodes are converted
            root.right = self.sortedListToBST(slow.next) # right hand side 
            return root 


        return None
            

        