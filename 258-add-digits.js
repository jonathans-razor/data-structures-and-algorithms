/*
258. Add Digits
Easy
Topics
Companies
Hint
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

 

Example 1:

Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.
Example 2:

Input: num = 0
Output: 0
 

Constraints:

0 <= num <= 231 - 1

*/
const sumDigits = (num) => {
  const digits = num.toString().split("");
  const sum = digits.reduce((acc, digit) => acc + parseInt(digit), 0);
  return sum > 9 ? sumDigits(sum) : sum;
};

if (process.argv.length !== 3) {
  console.error("Usage: node addDigits.js <number>");
  process.exit(1);
}

const inputNumber = parseInt(process.argv[2]);
const result = sumDigits(inputNumber);
console.log(`Result for ${inputNumber}: ${result}`);
