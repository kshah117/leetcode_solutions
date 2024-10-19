# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def helper(root, size):
            if not root:
                return size
            
            return max(helper(root.left, size + 1), helper(root.right, size + 1))

        return helper(root, 0)

        