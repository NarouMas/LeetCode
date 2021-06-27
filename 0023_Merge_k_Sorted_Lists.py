# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def mergeKLists(self, lists: [ListNode]) -> ListNode:
        from queue import PriorityQueue
        h = PriorityQueue()
        head = ListNode()
        node = head
        for l in lists:
            if l is not None:
                h.put((l.val, id(l), l))
                # heapq.heappush(h, (lists[i].val, lists[i]))
        while not h.empty():
            _, __, temp = h.get()
            node.next = ListNode(val=temp.val)
            node = node.next
            temp = temp.next
            if temp is not None:
                h.put((temp.val, id(temp), temp))
                # heapq.heappush(h, (temp, temp.val))
        return head.next



