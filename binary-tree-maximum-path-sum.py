# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = root.val

        def helper(x):
            if not x:
                return 0
            
            left_max = helper(x.left)
            right_max = helper(x.right)

            left_max = max(left_max, 0)
            right_max = max(right_max, 0)

            self.res = max(self.res, left_max + right_max + x.val)
            return x.val + max(left_max, right_max)

        helper(root)
        return self.res