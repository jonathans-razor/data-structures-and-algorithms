import sys

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def merge_lists(head1, head2):
    # Create a dummy node to simplify merging logic
    dummy = ListNode()
    current = dummy

    while head1 and head2:
        if head1.value < head2.value:
            current.next = head1
            head1 = head1.next
        else:
            current.next = head2
            head2 = head2.next
        current = current.next

    # Append any remaining nodes from either list
    if head1:
        current.next = head1
    else:
        current.next = head2

    return dummy.next

def create_linked_list(data):
    # Create a linked list from input data
    head = ListNode()
    current = head
    for val in data:
        current.next = ListNode(val)
        current = current.next
    return head.next

if __name__ == "__main__":
    # Parse input data for list1 and list2 (assuming integer values)
    try:
        data_list1 = list(map(int, sys.argv[1].split()))
        data_list2 = list(map(int, sys.argv[2].split()))
    except IndexError:
        print("Usage: python merge_linked_lists.py <list1> <list2>")
        sys.exit(1)

# Create linked lists from input data
list1_head = create_linked_list(data_list1)
list2_head = create_linked_list(data_list2)

# Merge the lists and print the result
merged_head = merge_lists(list1_head, list2_head)
while merged_head:
    print(merged_head.value, end=" -> ")
    merged_head = merged_head.next