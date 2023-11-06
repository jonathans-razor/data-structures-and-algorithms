import sys

def addBinary(a: str, b: str) -> str:
    # 1. convert to int
    # 2. add
    # 3. convert to binary
    return bin(int(a, 2) + int(b, 2))[2:]
    
if len(sys.argv) < 2:
    print("- Parameter(s) expected.")
    sys.exit(1)

print(addBinary(sys.argv[1], sys.argv[2]))