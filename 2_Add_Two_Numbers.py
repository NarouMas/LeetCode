# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = False
        head = ListNode()
        node = head
        while True:
            val = carry
            if l1 is not None:
                val += l1.val
                l1 = l1.next
            if l2 is not None:
                val += l2.val
                l2 = l2.next
            carry = False if val < 10 else True
            val %= 10
            node.val = val
            if l1 is not None or l2 is not None or carry:
                node.next = ListNode()
                node = node.next
            else:
                break
        return head

if __name__ == '__main__':
    a = Solution()
    print(a.addTwoNumbers([1, 2, 7, 8, 4], 15))