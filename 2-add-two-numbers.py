import sys

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            curr.next = ListNode(carry % 10)
            curr = curr.next
            carry //= 10
        return dummy.next

if __name__ == '__main__':
    # Define the linked lists.
    # Example: 342 + 465 = 807.
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))

    # Parse command line arguments.
    if len(sys.argv) > 1:
        values = [int(x) for x in sys.argv[1:]]
        l1_values = values[:len(values)//2]
        l2_values = values[len(values)//2:]
        l1 = ListNode(l1_values[0])
        current_node = l1
        for value in l1_values[1:]:
            current_node.next = ListNode(value)
            current_node = current_node.next
        l2 = ListNode(l2_values[0])
        current_node = l2
        for value in l2_values[1:]:
            current_node.next = ListNode(value)
            current_node = current_node.next

    # Create a solution object and call the method.
    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)

    # Print the result.
    while result:
        print(result.val, end='')
        result = result.next