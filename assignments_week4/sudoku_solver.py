#Implement Sudoku Solver
def solve_sudoku(board):
    def is_valid(r, c, k):
        for i in range(9):
            if board[i][c] == k or board[r][i] == k or board[r//3*3+i//3][c//3*3+i%3] == k:
                return False
        return True

    def backtrack():
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for k in map(str, range(1, 10)):
                        if is_valid(i, j, k):
                            board[i][j] = k
                            if backtrack():
                                return True
                            board[i][j] = '.'
                    return False
        return True

    backtrack()


print("Enter the Sudoku puzzle row by row (use '.' for empty cells):")
sudoku_board = []
for i in range(9):
    while True:
        row = input(f"Row {i+1}: ").strip()
        if len(row) == 9 and all(ch in "123456789." for ch in row):
            sudoku_board.append(list(row))
            break
        else:
            print("Invalid input. Enter exactly 9 characters (digits or '.')")


solve_sudoku(sudoku_board)
print("\nSolved Sudoku:")
for row in sudoku_board:
    print(" ".join(row))
