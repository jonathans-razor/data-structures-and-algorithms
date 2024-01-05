class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head: ListNode) -> ListNode:
    """
    Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

    Example 1:

    Input: head = [1,1,2]
    Output: [1,2]
    Example 2:

    Input: head = [1,1,2,3,3]
    Output: [1,2,3]

    Constraints:

    The number of nodes in the list is in the range [0, 300].
    -100 <= Node.val <= 100
    The list is guaranteed to be sorted in ascending order.
    
    return value: ListNode
    """
    if not head:
        return head
    curr = head
    while curr.next:
        if curr.val == curr.next.val:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Remove duplicates from a sorted linked list"
    )
    parser.add_argument(
        "list",
        metavar="N",
        type=int,
        nargs="+",
        help="a list of integers representing the sorted linked list",
    )
    args = parser.parse_args()
    head = ListNode(args.list[0])
    curr = head
    for i in range(1, len(args.list)):
        curr.next = ListNode(args.list[i])
        curr = curr.next
    head = deleteDuplicates(head)
    while head:
        print(head.val, end=" ")
        head = head.next
    print("\n\n")