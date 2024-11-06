# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def helper(level):
            if not level:
                return True

            for i in range(int(len(level) / 2)):
                if not level[i] and not level[-(i + 1)]:
                    continue
                if (
                    (level[i] and not level[-(i + 1)])
                    or (not level[i] and level[-(i + 1)])
                    or (level[i].val != level[-(i + 1)].val)
                ):
                    return False

            next_level = []

            while level:
                cur = level.pop(0)
                if not cur:
                    continue
                next_level.append(cur.left)
                next_level.append(cur.right)

            return helper(next_level)

        return helper([root])
