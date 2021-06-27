# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        node = head
        if head is not None and head.next is not None:
            head = head.next

        before = ListNode()
        while node is not None:
            next_node = node.next
            if next_node is not None:
                node.next = next_node.next
                next_node.next = node
                before.next = next_node
                before = node
            node = node.next
        return head


if __name__ == '__main__':
    si = 4
    n = [None for _ in range(si)]
    for i in range(si):
        n[i] = ListNode(i)
    for i in range(si - 1):
        n[i].next = n[i + 1]

    a = Solution()
    head = a.swapPairs(n[0])
    while head is not None:
        print(head.val)
        head = head.next
