# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        
        if self.isSameTree(root, subRoot):
            return True
        
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            def helper(root):
                ret = []
                s = [root]
                while s:
                    cur = s.pop(0)

                    if cur is None:
                        ret.append(cur)
                        continue

                    ret.append(cur.val)
                    
                    s.append(cur.left)
                    s.append(cur.right)

                return ret
            
            p_list = helper(p)
            q_list = helper(q)

            if p_list != q_list:
                return False

            return True