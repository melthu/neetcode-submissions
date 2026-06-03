# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        toReverse = slow.next
        slow.next = None

        prev = None
        curr = toReverse
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        p2 = prev
        p1 = head

        while p1 and p2:
            next1 = p1.next
            p1.next = p2
            next2 = p2.next
            p1 = next1
            p2.next = p1
            p2 = next2


        

        