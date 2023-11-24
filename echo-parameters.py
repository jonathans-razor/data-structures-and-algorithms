import sys

if len(sys.argv) < 2:
    print("- Parameter(s) expected.")
    sys.exit(1)

"""
Echo parameters to the console using a function.
Return Value: the parameter(s) echoed
"""
def echoParameters(s: str):
    return s

print(echoParameters(sys.argv[1:]))