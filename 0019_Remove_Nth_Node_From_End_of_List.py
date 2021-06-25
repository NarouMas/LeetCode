# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        size = 32
        sizeOfList = 0
        window = [None for _ in range(size)]
        index = 0
        node = head
        while node is not None:
            window[index] = node
            node = node.next
            index = (index + 1) % size
            sizeOfList += 1
        node = (index - n - 1) % size

        if n == sizeOfList:
            head = head.next
        elif n == 1:
            window[node].next = None
        else:
            window[node].next = window[(node + 2) % size]
        return head


if __name__ == '__main__':
    si = 2
    n = [None for _ in range(si)]
    for i in range(si):
        n[i] = ListNode(i)
    for i in range(si - 1):
        n[i].next = n[i + 1]

    a = Solution()
    head = a.removeNthFromEnd(n[0], 2)
    while head is not None:
        print(head.val)
        head = head.next
