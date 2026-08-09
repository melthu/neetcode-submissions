# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        heap = []

        # add first element of each of the k lists to the heap (val, index, pointer)
        for i in range(len(lists)):
            node = lists[i]
            if node:
                heap.append((lists[i].val, i, node))
        
        # initalize min heap
        heapq.heapify(heap)
        
        # while heap: pop min, append to sol, shift pointer, add next element to heap
        while heap:
            _, i, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
        
        return dummy.next
            



        
        
        