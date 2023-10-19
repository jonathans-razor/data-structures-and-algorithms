import sys

def is_valid_sudoku(board):
  """
  Determine whether the given Sudoku board is valid.

  Args:
    board: A 9x9 list of lists of integers, where 0 represents an empty square.

  Returns:
    True if the board is valid, False otherwise.
  """

  # Check for rows that contain duplicate numbers.
  for row in board:
    if len(set(row)) != 9:
      return False

  # Check for columns that contain duplicate numbers.
  for col in range(9):
    column = [row[col] for row in board]
    if len(set(column)) != 9:
      return False

  # Check for 3x3 subgrids that contain duplicate numbers.
  for i in range(0, 9, 3):
    for j in range(0, 9, 3):
      subgrid = [row[i:i + 3] for row in board[j:j + 3]]
      subgrid = [item for sublist in subgrid for item in sublist]
      if len(set(subgrid)) != 9:
        return False

  return True


if __name__ == '__main__':
  # Read the Sudoku board from the file.
  with open(sys.argv[1], 'r') as f:
    board = [list(map(int, line.strip().split(','))) for line in f]

  # Check the validity of the Sudoku board.
  if is_valid_sudoku(board):
    print('True')
  else:
    print('False')