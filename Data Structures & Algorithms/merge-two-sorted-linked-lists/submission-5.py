# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        c1 = list1
        c2 = list2
        while c1 and c2:
            if c1.val < c2.val:
                curr.next = c1
                curr = c1
                c1 = c1.next
            else: 
                curr.next = c2
                curr = c2
                c2 = c2.next

        if not c1:
            curr.next = c2
        
        if not c2:
            curr.next = c1

        return dummy.next
            

