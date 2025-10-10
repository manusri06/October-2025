# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def helper(node):
            if not node:
                return True
            
            lefth = helper(node.left)
            righth = helper(node.right)

            if lefth == -1 or righth == -1:
                return -1

            if abs(lefth-righth) > 1:
                return -1
            
            return 1+max(lefth,righth)
        return helper(root) != -1