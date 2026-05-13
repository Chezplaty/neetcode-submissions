# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = ListNode()
        start = head

        while list1 and list2:

            if list1.val <= list2.val:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next
            
            head = head.next
        
        #if there are still more elements in list1 or list2, point to them
        if list1:
            head.next = list1
        elif list2:
            head.next = list2

        return start.next

        
            
            