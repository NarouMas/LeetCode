# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None:
            return None
        if k == 0:
            return head
        cur = head
        dummy = ListNode(-1, head)
        k -= 1
        n = 0
        while cur.next is not None:
            if k == 0:
                dummy = dummy.next
            else:
                k -= 1
            cur = cur.next
            n += 1
        n += 1
        if dummy.val == -1:
            k = k % n
            if k == 0:
                return head
            k -= 1
            cur = head
            while cur.next is not None:
                if k == 0:
                    dummy = dummy.next
                else:
                    k -= 1
                cur = cur.next
                n += 1
        cur.next = head
        head = dummy.next
        dummy.next = None

        return head


def main():
    node = [ListNode(i, None) for i in range(3)]
    for i in range(2):
        node[i].next = node[i + 1]
    cur = node[0]

    a = Solution()
    res = a.rotateRight(None, 4)
    while res is not None:
        print(res.val)
        res = res.next


if __name__ == '__main__':
    main()
