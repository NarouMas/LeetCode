# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        # length is the length of front half list
        if length % 2 == 0:
            length = length >> 1
        else:
            length = (length >> 1) + 1
        cur = head
        count = 1
        while count != length:
            cur = cur.next
            count += 1
        next = cur.next
        cur.next = None
        cur = next
        # cur is the first node of back half list
        prev = None
        while cur is not None:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        # prev is the head the back half reorder list
        cur = head
        while cur is not None and prev is not None:
            next = cur.next
            cur.next = prev
            b_next = prev.next
            prev.next = next
            cur = next
            prev = b_next


if __name__ == '__main__':
    a = Solution()
    node7 = ListNode(7, None)
    node6 = ListNode(6, None)
    node5 = ListNode(5, node6)
    node4 = ListNode(4, node5)
    node3 = ListNode(3, node4)
    node2 = ListNode(2, node3)
    node1 = ListNode(1, node2)
    a.reorderList(node1)
    cur = node1
    while cur is not None:
        print(cur.val)
        cur = cur.next
