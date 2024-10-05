# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        digit_node = ListNode()
        ret = digit_node
        carry = 0

        while l1 or l2 or carry:
            digit_sum = 0
            if l1:
                digit_sum += l1.val
                l1 = l1.next
            if l2:
                digit_sum += l2.val
                l2 = l2.next

            if carry:
                digit_sum += carry

            digit_value = digit_sum % 10 
            carry = digit_sum // 10
            digit_node.next = ListNode(digit_value)
            digit_node = digit_node.next

        return ret.next