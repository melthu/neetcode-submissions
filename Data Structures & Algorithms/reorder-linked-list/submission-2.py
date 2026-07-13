# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        n = 0
        curr = head
        while curr:
            curr = curr.next
            n += 1
        
        curr = head
        for i in range(math.ceil(n / 2) - 1):
            curr = curr.next
        
        nextnode = curr.next
        curr.next = None
        curr = nextnode
        
        prev = None
        while curr:
            nextnode = curr.next
            curr.next = prev
            prev = curr
            curr = nextnode
        
        curr = head
        while curr and prev:
            nextnode = curr.next
            nextprev = prev.next
            curr.next = prev
            prev.next = nextnode
            curr = nextnode
            prev = nextprev
        





        