# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        sz = 0
        temp = head

        while temp:
            sz += 1
            temp = temp.next
        
        temp2 = head
        sz2 = 0

        if sz - n == 0:
            return head.next

        while temp2:
            sz2 += 1
            if sz2 == (sz - n):
                temp2.next = temp2.next.next
                break
            temp2 = temp2.next
        return head