# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True
        def helper(cur, h):
            if not cur:
                return h
            
            left_height = helper(cur.left, h + 1)
            right_height = helper(cur.right, h + 1)


            if abs(left_height - right_height) > 1:
                self.balanced = False
            
            return max(left_height, right_height)


        helper(root, 0)
        return self.balanced