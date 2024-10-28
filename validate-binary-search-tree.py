# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def helper(x, lb, rb):
            if not x:
                return True
            
            if x.val >= rb or x.val <= lb:
                return False

            return (helper(x.left, lb, x.val) and helper(x.right, x.val, rb))

        return helper(root, float("-inf"), float("inf"))