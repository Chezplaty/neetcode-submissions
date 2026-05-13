# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1, num2 = 0, 0

        multiplier = 1
        while l1:
            num1 += (l1.val * multiplier)
            multiplier *= 10

            l1 = l1.next
        
        multiplier = 1
        while l2:
            num2 += (l2.val * multiplier)
            multiplier *= 10

            l2 = l2.next

        total = num1 + num2
        newNode = ListNode(total%10)
        head = newNode
        total //= 10
    
        while total > 0:
            value = total%10
            newNode.next = ListNode(value)
            total //= 10

            newNode = newNode.next
        
        return head

