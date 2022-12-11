# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack = [None] # prev
        def dfs(node):
            if node:
                dfs(node.right) # extend the right most node to create space for the left
                dfs(node.left) # thats why we process the left later
                # we don't check the right subtree for simplicity sake
                node.right = stack[0] # None , 4, 3 , 2 ,1
                node.left = None # none, none , none
                stack[0] = node  # 4 , 3, 2, 1
            return None
        dfs(root)

       






