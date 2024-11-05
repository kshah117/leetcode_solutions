# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        self.str = ""
        def helper(x):
            if not x:
                self.str += ",null"
                return
            
            self.str += f",{x.val}"
            helper(x.left)
            helper(x.right)

        helper(root)
        
        if self.str.startswith(","):
            self.str = self.str[1:]
        return self.str

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = data.split(",")
        self.i = 0
        
        def helper():
            if vals[self.i] == "null":
                self.i += 1
                return None

            cur = TreeNode(int(vals[self.i]))
            self.i += 1
            cur.left = helper()
            cur.right = helper()
            return cur

        return helper()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))