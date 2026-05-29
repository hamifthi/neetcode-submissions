# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 1
        current = head
        while current.next:
            current = current.next
            length += 1
        
        index_delete = length - n
        current = head
        if index_delete == 0:
            if length == 1:
                return
            else:
                return head.next
        
        prev = None
        next_ = None
        index = 0
        current = head
        while index != index_delete:
            prev = current
            next_ = current.next.next
            current = current.next
            index += 1
        
        prev.next = next_
        return head


