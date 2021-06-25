# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(val=-1)
        node = head
        while True:
            if l1 is not None and l2 is not None:
                if l1.val < l2.val:
                    node.next = ListNode(l1.val)
                    l1 = l1.next
                else:
                    node.next = ListNode(l2.val)
                    l2 = l2.next
            elif l1 is not None:
                node.next = ListNode(l1.val)
                l1 = l1.next
            elif l2 is not None:
                node.next = ListNode(l2.val)
                l2 = l2.next
            else:
                break
            node = node.next

        return head.next

if __name__ == '__main__':
    a, b = 5, 10
    la = [None for _ in range(a)]
    lb = [None for _ in range(b)]
    for i in range(a):
        la[i] = ListNode(i * 3 + 5)
    for i in range(b):
        lb[i] = ListNode(i * 2 + 7)
    for i in range(a - 1):
        la[i].next = la[i + 1]
    for i in range(b - 1):
        lb[i].next = lb[i + 1]

    a = Solution()
    head = a.mergeTwoLists(la[0], lb[0])
    while head is not None:
        print(head.val)
        head = head.next