/*
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

 Example 1:

Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.

 * @param {TreeNode} root
 * @param {number} targetSum
 * @return {boolean}

*/

class TreeNode {
    constructor(val) {
        this.val = val;
        this.left = this.right = null;
    }
}

function buildTree(data) {
    if (!data || data.length === 0) {
        return null;
    }

    const values = data.split(',').map(val => (val === 'null' ? null : parseInt(val, 10)));
    const root = new TreeNode(values[0]);
    const queue = [root];
    let index = 1;

    while (index < values.length) {
        const current = queue.shift();

        if (values[index] !== null) {
            current.left = new TreeNode(values[index]);
            queue.push(current.left);
        }
        index++;

        if (index < values.length && values[index] !== null) {
            current.right = new TreeNode(values[index]);
            queue.push(current.right);
        }
        index++;
    }

    return root;
}

function hasPathSum(root, targetSum) {
    if (!root) {
        return false;
    }

    if (root.val === targetSum && !root.left && !root.right) {
        return true;
    }

    return hasPathSum(root.left, targetSum - root.val) || hasPathSum(root.right, targetSum - root.val);
}

// Parse command line arguments
const args = process.argv.slice(2);
if (args.length !== 2) {
    console.error("Usage: node pathSum.js <targetSum> <treeData>");
    process.exit(1);
}
const targetSum = parseInt(args[0], 10);
const treeData = args[1];

const root = buildTree(treeData);
console.log(hasPathSum(root, targetSum)); // Output: true or false
