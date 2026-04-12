class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        head = ListNode()
        tail = head
        carry = 0

        while l1 or l2 or carry != 0:
            curr1 = l1.val if l1 else 0
            curr2 = l2.val if l2 else 0

            total = curr1 + curr2 + carry
            carry = total // 10
            digit = total % 10

            tail.next = ListNode(digit)
            tail = tail.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return head.next


def main():
    li = ListNode(2)
    li.next = ListNode(4)
    li.next.next = ListNode(3)

    li1 = ListNode(5)
    li1.next = ListNode(6)
    li1.next.next = ListNode(4)

    sol = Solution()
    print(sol.addTwoNumbers(li, li1))


main()
