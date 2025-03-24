# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left = right = root
        left_h = right_h = 0

        while left:
            left_h += 1
            left = left.left
        while right:
            right_h += 1
            right = right.right
        
        if left_h == right_h:
            return pow(2, left_h) - 1
        
        return self.countNodes(root.left) + self.countNodes(root.right) + 1
