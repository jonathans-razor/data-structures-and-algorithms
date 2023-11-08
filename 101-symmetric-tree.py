import sys

if len(sys.argv) < 2:
    print("- Parameter(s) expected.")
    sys.exit(1)

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSymmetric(root):
    def isMirror(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return (
            (left.val == right.val)
            and isMirror(left.left, right.right)
            and isMirror(left.right, right.left)
        )

    if not root:
        return True
    return isMirror(root.left, root.right)


def buildTree(nodes):
    if not nodes:
        return None

    root = TreeNode(int(nodes[0]))
    queue = deque([root])
    i = 1

    while queue and i < len(nodes):
        node = queue.popleft()
        if nodes[i] is not None:
            node.left = TreeNode(int(nodes[i]))
            queue.append(node.left)
        i += 1
        if i < len(nodes) and nodes[i] is not None:
            node.right = TreeNode(int(nodes[i]))
            queue.append(node.right)
        i += 1

    return root


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python symmetric_tree.py <list of numbers>")
        sys.exit(1)

    input_nodes = [int(val) if val != "null" else None for val in sys.argv[1:]]
    root = buildTree(input_nodes)
    result = isSymmetric(root)
    print("Is the tree symmetric?", result)
