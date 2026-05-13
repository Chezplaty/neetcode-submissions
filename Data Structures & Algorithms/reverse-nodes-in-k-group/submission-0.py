# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        

        i = 0
        curr = head

        while curr and i < k:
            curr = curr.next
            i += 1
        
        if i == k:
            prev_val = self.reverseKGroup(curr, k)
            while i > 0:
                dummy = head
                head = head.next
                dummy.next = prev_val
                prev_val = dummy
                i -= 1
        else:
            return head
        
        return dummy

        