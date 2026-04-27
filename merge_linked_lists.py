# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):

        dummy = ListNode(0)
        head = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                dummy.next = list1
                list1 = list1.next
            else:
                dummy.next = list2
                list2 = list2.next

            dummy = dummy.next
        if list1:
            dummy.next = list1
        if list2:
            dummy.next = list2
        return head.next


list1 = ListNode(1, ListNode(2, ListNode(4)))

list2 = ListNode(1, ListNode(3, ListNode(4)))

sol = Solution()
print(sol.mergeTwoLists(list1, list2))
