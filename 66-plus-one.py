class Solution:
    def plusOne(self, digits):
        # Convert the list elements into an integer
        num = int(''.join(map(str, digits)))
        
        # Increment the integer by 1
        num += 1
        
        # Convert the updated integer back to a list of digits
        result = [int(d) for d in str(num)]
        
        return result

if __name__ == "__main__":
    # Example usage: python plus_one.py 1 2 3
    import sys
    input_digits = [int(arg) for arg in sys.argv[1:]]
    solution = Solution()
    output = solution.plusOne(input_digits)
    print("Result:", output)
