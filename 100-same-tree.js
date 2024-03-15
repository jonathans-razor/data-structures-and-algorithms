// LeetCode Problem 100: Same Tree
// Given two binary trees, write a function to check if they are the same or not.
// Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

/**
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {boolean}
 */

class TreeNode {
    constructor(val) {
        this.val = val;
        this.left = this.right = null;
    }
}

function isSameTree(p, q) {
    if (!p && !q) {
        return true; // Both trees are empty, so they are the same
    }
    if (!p || !q || p.val !== q.val) {
        return false; // One of the trees is empty or their values are different
    }
    return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
}

// Read input from command line arguments
const tree1 = parseTreeFromCommandLine(process.argv[2]);
const tree2 = parseTreeFromCommandLine(process.argv[3]);

function parseTreeFromCommandLine(input) {
    // Parse input and construct the tree (you can customize this part)
    // For example, input format: "1,2,null,null,3,null,null"
    const values = input.split(',').map(val => (val === 'null' ? null : parseInt(val)));
    return buildTree(values, 0);
}

function buildTree(values, index) {
    if (index >= values.length || values[index] === null) {
        return null;
    }
    const node = new TreeNode(values[index]);
    node.left = buildTree(values, 2 * index + 1);
    node.right = buildTree(values, 2 * index + 2);
    return node;
}

console.log(isSameTree(tree1, tree2)); // Output: true or false