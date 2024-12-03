"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def __init__(self):
        self.visited = {}

    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return

        if node.val in self.visited:
            return self.visited[node.val]

        copy_node = Node(node.val, [])
        self.visited[node.val] = copy_node

        for n in node.neighbors:
            copy_neighbor = self.cloneGraph(n)
            copy_node.neighbors.append(copy_neighbor)

        return copy_node
