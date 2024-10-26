# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.good_nodes = 0

        def helper(x, path):
            if not path or x.val >= max(path):
                self.good_nodes += 1
            
            if x.left:
                helper(x.left, path + [x.val])
            if x.right:
                helper(x.right, path + [x.val])

        helper(root, [])
        return self.good_nodes