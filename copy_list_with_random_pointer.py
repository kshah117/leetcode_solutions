"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

from typing import Optional


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mappings = {None:None}

        temp1 = head

        while temp1:
            mappings[temp1] = Node(x=temp1.val)
            temp1 = temp1.next

        temp2 = head
        while temp2:
            copy_node = mappings[temp2]
            copy_node.next = mappings[temp2.next]
            copy_node.random = mappings[temp2.random]
            temp2 = temp2.next
        
        return mappings[head]
        