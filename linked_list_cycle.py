# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from typing import Optional


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s = head
        f = head
        if not head:
            return False 
        while f.next:
            s = s.next
            f = f.next.next
            if not f:
                return False
            if s == f:
                return True
                
        return False