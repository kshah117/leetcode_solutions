# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head:
            return head

        length = 1
        temp = head
        while temp.next:
            length += 1
            temp = temp.next

        k = k % length
        if k == 0:
            return head

        temp2 = head

        i = 0
        while i < length - k - 1:
            i += 1
            temp2 = temp2.next

        ret = temp2.next
        temp2.next = None
        temp.next = head

        return ret
