import sys

if len(sys.argv) < 2:
    print("- Parameter(s) expected.")
    sys.exit(1)


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 7:
        print("Usage: python same_tree.py p_val1 p_val2 q_val1 q_val2 q_val3 q_val4")
    else:
        # Construct the trees from command-line arguments
        p_val1, p_val2, q_val1, q_val2, q_val3, q_val4 = map(int, sys.argv[1:])
        p = TreeNode(p_val1)
        p.left = TreeNode(p_val2)
        q = TreeNode(q_val1)
        q.left = TreeNode(q_val2)
        q.right = TreeNode(q_val3)
        q.right.right = TreeNode(q_val4)

        solution = Solution()
        result = solution.isSameTree(p, q)
        print(p)
        print(q)
        if result:
            print("The given trees are identical.")
        else:
            print("The given trees are not identical.")
