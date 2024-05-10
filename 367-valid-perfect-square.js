/* 

Given a positive integer num, return true if num is a perfect square or false otherwise.

A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.

You must not use any built-in library function, such as sqrt.

 

Example 1:

Input: num = 16
Output: true
Explanation: We return true because 4 * 4 = 16 and 4 is an integer.
Example 2:

Input: num = 14
Output: false
Explanation: We return false because 3.742 * 3.742 = 14 and 3.742 is not an integer.
 

Constraints:

1 <= num <= 231 - 1 

*/

// LeetCode Problem 367: Valid Perfect Square
var isPerfectSquare = function(num) {
    let left = 1;
    let right = 10 ** 18; // Set an upper bound for the search range

    while (left < right) {
        const mid = left + Math.floor((right - left) / 2);
        if (mid * mid >= num) {
            right = mid;
        } else {
            left = mid + 1;
        }
    }

    return left * left === num;
};

// Example usage:
const inputNumber = parseInt(process.argv[2]); // Read input from command line
const result = isPerfectSquare(inputNumber);
console.log(`Is ${inputNumber} a perfect square? ${result}`);