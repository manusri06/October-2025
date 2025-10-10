# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        
        col_t = defaultdict(list)
        q = deque([(root,0,0)])

        while q:
            node, row, col = q.popleft()
            col_t[col].append((row,node.val))

            if node.left:
                q.append((node.left,row+1,col-1))

            if node.right:
                q.append((node.right,row+1,col+1))

        res = []
        for c in sorted(col_t.keys()):
            colnodes = sorted(col_t[c], key=lambda x:(x[0],x[1]))
            res.append([val for row,val in colnodes])
        return res



