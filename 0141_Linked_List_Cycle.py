# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head) -> bool:
        if not head:
            return False
        hare = tortoise = head
        if hare.next is None or hare.next.next is None:
            return False
        hare = hare.next.next
        tortoise = tortoise.next
        while True:
            if hare == tortoise:
                return True
            if hare.next is None or hare.next.next is None:
                return False
            hare = hare.next.next
            tortoise = tortoise.next
