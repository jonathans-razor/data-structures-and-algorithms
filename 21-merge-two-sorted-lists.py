# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        current = head
        while current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next

        return head


def create_linked_list(data):
    if not data:
        return None
    head = ListNode(data[0])
    current = head
    for val in data[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python leetcode83.py [list]")
        sys.exit(1)

    data = [int(val) for val in sys.argv[1:]]
    head = create_linked_list(data)

    solution = Solution()
    new_head = solution.deleteDuplicates(head)

    print("Original Linked List:")
    print_linked_list(head)

    print("\nLinked List after Removing Duplicates:")
    print_linked_list(new_head)
