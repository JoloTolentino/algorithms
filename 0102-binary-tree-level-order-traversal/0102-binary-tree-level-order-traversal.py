# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        mapping = {}
        
        def dfs(node,level = 0):
            if node:
                if level in mapping: mapping[level].append(node.val) 
                else: mapping[level] = [node.val]
                dfs(node.left,level+1)
                dfs(node.right,level+1)
            return 

        dfs(root)

        return [mapping[level] for level in mapping]