# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.ret = []
        
        
        def helper(level):
            next_level = []
            cur_level = []    
            while level:
                cur = level.pop(0)
                cur_level.append(cur.val)
                if cur.left:
                    next_level.append(cur.left)
                if cur.right:
                    next_level.append(cur.right)
                    
            self.ret.append(cur_level)
            if next_level:
                helper(next_level)

        if not root:
            return []
        
        helper([root])
        return self.ret