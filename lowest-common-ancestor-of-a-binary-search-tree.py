# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        small = min(p.val, q.val)
        big = max(p.val, q.val)
        s = [root]
        while s:
            cur = s.pop(0)
            if small <= cur.val <= big:
                return cur
            
            if cur.left:
                s.append(cur.left)
            if cur.right:
                s.append(cur.right)