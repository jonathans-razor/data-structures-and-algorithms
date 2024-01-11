import sys
from typing import List, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        """
        Given the root of a binary tree, determine if it is a valid binary search tree (BST).

        A valid BST is defined as follows:

        The left subtree of a node contains only nodes with keys less than the node's key.
        The right subtree of a node contains only nodes with keys greater than the node's key.
        Both the left and right subtrees must also be binary search trees.

        Example 1:

        Input: root = [2,1,3]
        Output: true
        Example 2:

        Input: root = [5,1,4,null,null,3,6]
        Output: false
        Explanation: The root node's value is 5 but its right child's value is 4.

        Constraints:

        The number of nodes in the tree is in the range [1, 104].
        -231 <= Node.val <= 231 - 1

        return value: 
        """

        def helper(node: TreeNode, lower=float("-inf"), upper=float("inf")) -> bool:
            if not node:
                return True
            val = node.val
            if val <= lower or val >= upper:
                return False
            if not helper(node.right, val, upper):
                return False
            if not helper(node.left, lower, val):
                return False
            return True

        return helper(root)


def parse_input(input_str: str) -> TreeNode:
    def build_tree(node_list: List[int], index: int) -> TreeNode:
        if index >= len(node_list) or node_list[index] is None:
            return None
        node = TreeNode(node_list[index])
        node.left = build_tree(node_list, 2 * index + 1)
        node.right = build_tree(node_list, 2 * index + 2)
        return node

    node_list = [
        int(x) if x != "null" else None for x in input_str.strip("[]").split(",")
    ]
    return build_tree(node_list, 0)


def main(args: List[str]) -> None:
    input_str = args[0]
    root = parse_input(input_str)
    soln = Solution()
    print(soln.isValidBST(root))


if __name__ == "__main__":
    main(sys.argv[1:])
