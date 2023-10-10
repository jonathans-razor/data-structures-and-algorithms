import sys

if len(sys.argv) != 2:
    print("Usage: python reverse_string.py <string>")
    sys.exit(1)

string = sys.argv[1]
reversed_string = string[::-1]

print(reversed_string)