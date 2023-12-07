import sys

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        currentListNode = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                currentListNode.next = list1
                list1, currentListNode = list1.next, list1
            else:
                currentListNode.next = list2
                list2, currentListNode = list2.next, list2
        if list1 or list2:
            currentListNode.next = list1 if list1 else list2
        return dummy.next

if __name__ == "__main__":
    l1 = ListNode(
        int(sys.argv[1]), ListNode(int(sys.argv[2]), ListNode(int(sys.argv[3])))
    )
    l2 = ListNode(
        int(sys.argv[4]), ListNode(int(sys.argv[5]), ListNode(int(sys.argv[6])))
    )
    s = Solution()
    result = s.mergeTwoLists(l1, l2)
    while result:
        print(result.val, end=" ")
        result = result.next
