import sys

if __name__ == "__main__":
  if len(sys.argv) < 2:
    print("\n- Parameter(s) expected.")
    exit(1)
  print(sys.argv[1:])
