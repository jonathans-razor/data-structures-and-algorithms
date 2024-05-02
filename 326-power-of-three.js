/*
Code
Testcase
Test Result
Test Result
326. Power of Three
Easy
Topics
Companies
Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3x.

 

Example 1:

Input: n = 27
Output: true
Explanation: 27 = 33
Example 2:

Input: n = 0
Output: false
Explanation: There is no x where 3x = 0.
Example 3:

Input: n = -1
Output: false
Explanation: There is no x where 3x = (-1).
 

Constraints:

-231 <= n <= 231 - 1
*/

// Approach 1: Logarithmic Approach
function isPowerOfThree(n) {
    const res = Math.log10(n) / Math.log10(3);
    return Number.isInteger(res);
}

// Approach 2: Mathematical Approach
function isPowerOfThreeMath(n) {
    return n > 0 && Math.pow(3, 19) % n === 0;
}

// Command-line input handling
if (process.argv.length !== 3) {
    console.error("Usage: node powerOfThree.js <integer>");
    process.exit(1);
}

const inputNumber = parseInt(process.argv[2]);
if (isNaN(inputNumber)) {
    console.error("Invalid input. Please provide a valid integer.");
    process.exit(1);
}

console.log(`Is ${inputNumber} a power of three?`);
console.log(`Approach 1: ${isPowerOfThree(inputNumber)}`);
console.log(`Approach 2: ${isPowerOfThreeMath(inputNumber)}`);
