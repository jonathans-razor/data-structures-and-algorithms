import sys

if len(sys.argv) < 2:
    print("- Parameter(s) expected.")
    sys.exit(1)

def generate_pascals_triangle(numRows):
    triangle = []
    for i in range(numRows):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle

if __name__ == "__main__":
    numRows = int(sys.argv[1])
    print(generate_pascals_triangle(numRows))
