# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        s = head
        f = head.next

        #when loop starts, s is about halfway through list
        while f and f.next:
            s = s.next
            f = f.next.next
        
        second = s.next
        prev_val = s.next = None

        while second:
            holder = second.next
            second.next = prev_val
            prev_val = second
            second = holder
        
        first, second = head, prev_val

        while second:
            tmp1, tmp2 = first.next, second.next

            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2     