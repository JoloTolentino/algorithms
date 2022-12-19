# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        if preorder:
            root_val = preorder.pop(0)
            root = TreeNode(val = root_val)
            
            LHS = inorder[:inorder.index(root_val)]
            RHS = inorder[inorder.index(root_val)+1:]
            
            if LHS:
                root.left = self.buildTree(preorder,LHS)
            if RHS: 
                root.right = self.buildTree(preorder,RHS)
            
            
        
        return root
        




        






    
















