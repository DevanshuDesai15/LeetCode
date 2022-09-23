# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

## Time Complexity of this problem is O(n) best and worst both.
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        ## Recursive ##
        res=[]
        
        def inorder(root):
            if not root:
                return
            inorder(root.left) # search the left sub tree
            res.append(root.val) # add the value of the root node to result
            inorder(root.right) # search on right sub tree
        inorder(root)
        return res
        
        