# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        s = [root]
        ret = []
        while s:
            rs = None

            for i in range(len(s)):
                cur = s.pop(0)
                rs = cur.val
                if cur.left:
                    s.append(cur.left)
                if cur.right:
                    s.append(cur.right)

            
            if rs is not None:
                ret.append(rs)
        
        return ret