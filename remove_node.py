class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNthFromEnd(self, head: ListNode, n):
        dummy = ListNode(0, head)
        start = dummy
        end = dummy
        for _ in range(n+1):
            end = end.next
        while end:
            end = end.next
            start = start.next
        start.next = start.next.next

        return dummy.next


sol = Solution()
head = ListNode(1)
# head.next = ListNode(2)
# head.next.next = ListNode(3)
# head.next.next.next = ListNode(4)
# head.next.next.next.next = ListNode(5)
print(sol.removeNthFromEnd(head, 1))
