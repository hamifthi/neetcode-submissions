# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        current = dummy
        carry_digit = 0
        while l1 or l2:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            sum_of_vals = l1_val+l2_val+carry_digit
            carry_digit = 0
            if sum_of_vals >= 10:
                remainder = sum_of_vals - 10
                new_node = ListNode(val=remainder)
                carry_digit = 1
            else:
                new_node = ListNode(val=sum_of_vals)
            l1 = l1.next if l1 and l1.next else None
            l2 = l2.next if l2 and l2.next else None
            current.next = new_node
            current = current.next
        if carry_digit:
            new_node = ListNode(val=carry_digit)
            current.next = new_node
        return dummy.next