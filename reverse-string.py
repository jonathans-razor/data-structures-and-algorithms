import sys

if len(sys.argv) < 2:
    print("- Parameter(s) expected.")
    sys.exit(1)

string = sys.argv[1]
reversed_string = string[::-1]

print(reversed_string)
