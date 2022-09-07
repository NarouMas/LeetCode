# Definition for singly-linked list.
from multiprocessing import dummy


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: [ListNode]) -> [ListNode]:
        dummy = ListNode(0, head)
        head = dummy
        while head.next:
            head = head.next
            while head.next and head.val == head.next.val:
                head.next = head.next.next
        return dummy.next


if __name__ == '__main__':
    a = Solution()
    n1 = ListNode(6, None)
    n2 = ListNode(6, n1)
    n3 = ListNode(4, n2)
    n4 = ListNode(3, n3)
    n5 = ListNode(3, n4)
    n6 = ListNode(1, n5)
    n7 = ListNode(1, n6)
    ans = a.deleteDuplicates(n7)
    while ans is not None:
        print(ans.val)
        ans = ans.next

