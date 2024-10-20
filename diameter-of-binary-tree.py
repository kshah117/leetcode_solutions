# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_d = 0

        def helper(n):
            if not n:
                return 0

            left_h = helper(n.left)
            right_h = helper(n.right)

            self.max_d = max(self.max_d, left_h + right_h)

            return 1 + max(left_h, right_h)

        helper(root)
        return self.max_d
