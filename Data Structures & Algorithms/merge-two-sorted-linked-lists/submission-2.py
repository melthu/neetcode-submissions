# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = list1
        p2 = list2

        dummy = ListNode()
        p = dummy

        while p1 and p2:
            if p1.val < p2.val:
                p.next = ListNode(p1.val, None)
                print(p1.val)
                p = p.next
                p1 = p1.next
            else:
                p.next = ListNode(p2.val, None)
                print(p2.val)
                p = p.next
                p2 = p2.next
        
        while p1:
            p.next = ListNode(p1.val, None)
            print(p1.val)
            p = p.next
            p1 = p1.next

        while p2:
            p.next = ListNode(p2.val, None)
            print(p2.val)
            p = p.next
            p2 = p2.next
        
        return dummy.next


        


        