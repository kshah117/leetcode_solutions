# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:
    def helper(self, n, x, m):            
        if not n:
            return
        
        n.val = x * 2 + m
        self.vals.add(n.val)

        if n.left:
            self.helper(n.left, n.val, 1)
        if n.right:
            self.helper(n.right, n.val, 2)
        

    def __init__(self, root: Optional[TreeNode]):
        root.val = 0
        self.vals = set()
        self.root = root
        self.helper(root, root.val, 0)
        
    def helper(self, n, x, m):            
        if not n:
            return    
        n.val = x * 2 + m
        self.vals.add(n.val)

        if n.left:
            self.helper(n.left, n.val, 1)
        if n.right:
            self.helper(n.right, n.val, 2)

    def find(self, target: int) -> bool:
        return target in self.vals

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)