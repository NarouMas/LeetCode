#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: [ListNode]) -> [ListNode]:
        dummy = ListNode(-2147483648, head)
        curr = head
        priv = dummy
        while curr is not None and curr.next is not None:
            if curr.val != curr.next.val:
                curr = curr.next
                priv = priv.next
            else:
                node = curr
                while node.next is not None and node.val == node.next.val:
                    node = node.next
                priv.next = node.next
                curr = node.next
        
        return dummy.next

if __name__ == '__main__':
    a = Solution()
    n1 = ListNode(6, None)
    n2 = ListNode(6, n1)
    n3 = ListNode(4, n2)
    n4 = ListNode(3, n3)
    n5 = ListNode(3, n4)
    n6 = ListNode(2, n5)
    n7 = ListNode(1, n6)
    ans = a.deleteDuplicates(n7)
    while ans is not None:
        print(ans.val)
        ans = ans.next

