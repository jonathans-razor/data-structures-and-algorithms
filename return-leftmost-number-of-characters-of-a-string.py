import sys

if len(sys.argv) < 2:
    print("- Parameter(s) expected.")
    sys.exit(1)

"""

Return Value: string
"""
def return_leftmost_number_of_characters_of_a_string(s: str, i: int) -> str:
    return s[:i]

print(return_leftmost_number_of_characters_of_a_string(sys.argv[1], int(sys.argv[2])))