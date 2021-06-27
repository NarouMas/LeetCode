# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        cur = head
        for i in range(k):
            if cur is None:
                return head
            cur = cur.next
        newHead = self.reverse(head, cur)
        head.next = self.reverseKGroup(cur, k)
        return newHead

    def reverse(self, head, tail):
        pre = tail
        while head != tail:
            t = head.next
            head.next = pre
            pre = head
            head = t
        return pre



if __name__ == '__main__':
    def main():
        si = 10
        n = [None for _ in range(si)]
        for i in range(si):
            n[i] = ListNode(i)
        for i in range(si - 1):
            n[i].next = n[i + 1]

        a = Solution()
        head = a.reverseKGroup(n[0], 3)
        while head is not None:
            print(head.val)
            head = head.next
    main()
