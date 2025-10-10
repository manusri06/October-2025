# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        n = len(nums)-1
        l,r = 0,n

        def help(l,r):

            if l > r:
                return None
            
            mid = (l+r)//2
            root = TreeNode(nums[mid])

            root.left = help(l,mid-1)
            root.right = help(mid+1,r)
            return root

        return help(l,r)
