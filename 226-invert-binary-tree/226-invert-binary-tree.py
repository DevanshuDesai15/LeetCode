# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # Depth First Search
        
        if not root:
            return None
        
        # swapping the children
        tmp = root.left
        root.left = root.right
        root.right = tmp
        
        self.invertTree(root.left) # doing recurssion by calling itself
        self.invertTree(root.right)
        return root