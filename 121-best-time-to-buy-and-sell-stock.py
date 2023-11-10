import sys

def maxProfit(prices):
    if not prices or len(prices) < 2:
        return 0

    min_price = prices[0]
    max_profit = 0

    for price in prices[1:]:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)

    return max_profit

if __name__ == "__main__":
    # Check if command line arguments are provided
    if len(sys.argv) < 2:
        print("Usage: python script.py <price1> <price2> ...")
        sys.exit(1)

    # Extract prices from command line arguments
    prices = [int(arg) for arg in sys.argv[1:]]

    # Calculate and print the result
    result = maxProfit(prices)
    print("Maximum profit:", result)
