import argparse
from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        """
        Given the head of a linked list, rotate the list to the right by k places.

        Example 1:

        Input: head = [1,2,3,4,5], k = 2
        Output: [4,5,1,2,3]
        Example 2:

        Input: head = [0,1,2], k = 4
        Output: [2,0,1]

        Constraints:
        The number of nodes in the list is in the range [0, 500].
        -100 <= Node.val <= 100
        0 <= k <= 2 * 109
        """
        if not head:
            return None
        if not head.next:
            return head
        node = 1
        currentNode = head
        while currentNode.next:
            currentNode = currentNode.next
            node += 1
        currentNode.next = head
        currentNode = head
        for i in range(node - k % node - 1):
            currentNode = currentNode.next
        newHead = currentNode.next
        currentNode.next = None
        return newHead

def parse_args() -> List[int]:
    parser = argparse.ArgumentParser(description="Rotate List")
    parser.add_argument("--list", type=int, nargs="+", help="List of integers")
    parser.add_argument("--k", type=int, help="Number of places to rotate")
    args = parser.parse_args()
    return args.list, args.k

if __name__ == "__main__":
    l, k = parse_args()
    head = ListNode(l[0])
    currentNode = head
    for i in range(1, len(l)):
        currentNode.next = ListNode(l[i])
        currentNode = currentNode.next
    solution = Solution()
    result = solution.rotateRight(head, k)
    while result:
        print(result.val, end=" ")
        result = result.next