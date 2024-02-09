/**
 * @param {number[]} prices
 * @return {number}
 * 
 * 
 * 123. Best Time to Buy and Sell Stock III

You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete at most two transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Example 1:

Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
 
Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 105

 */
var maxProfit = function (prices) {
  const n = prices.length;
  if (n === 0) return 0;

  // Initialize arrays to store maximum profit for one and two transactions.
  const dp1 = new Array(n).fill(0);
  const dp2 = new Array(n).fill(0);

  // Calculate maximum profit for one transaction.
  let minPrice = prices[0];
  for (let i = 1; i < n; i++) {
    dp1[i] = Math.max(dp1[i - 1], prices[i] - minPrice);
    minPrice = Math.min(minPrice, prices[i]);
  }

  // Calculate maximum profit for two transactions.
  let maxPrice = prices[n - 1];
  for (let i = n - 2; i >= 0; i--) {
    dp2[i] = Math.max(dp2[i + 1], maxPrice - prices[i]);
    maxPrice = Math.max(maxPrice, prices[i]);
  }

  // Combine the results from one and two transactions.
  let maxProfit = 0;
  for (let i = 0; i < n; i++) {
    maxProfit = Math.max(maxProfit, dp1[i] + dp2[i]);
  }

  return maxProfit;
};

// Example usage:
const inputPrices = process.argv.slice(2).map(Number);
const result = maxProfit(inputPrices);
console.log(`Maximum profit: ${result}`);