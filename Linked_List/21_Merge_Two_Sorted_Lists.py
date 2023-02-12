from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        merged_head = dummy
        l1 = head1
        l2 = head2

        while l1 and l2:
            if l1.val <= l2.val:
                merged_head.next = l1
                l1 = l1.next
            else:
                merged_head.next = l2
                l2 = l2.next

            merged_head = merged_head.next

        if l1:
            merged_head.next = l1
        elif l2:
            merged_head.next = l2

        return dummy.next


head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(3)

head2 = ListNode(2)
head2.next = ListNode(3)
head2.next.next = ListNode(4)

s = Solution()
s.mergeTwoLists(head1, head2)
