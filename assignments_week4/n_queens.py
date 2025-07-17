#Solve N-Queens Problem
def solve_n_queens(n):
    def is_safe(row, col, diagonals, anti_diagonals, cols):
        return col not in cols and (row - col) not in diagonals and (row + col) not in anti_diagonals

    def backtrack(row):
        if row == n:
            result.append(["".join(r) for r in board])
            return
        for col in range(n):
            if is_safe(row, col, diagonals, anti_diagonals, cols):
                board[row][col] = 'Q'
                cols.add(col)
                diagonals.add(row - col)
                anti_diagonals.add(row + col)

                backtrack(row + 1)

                board[row][col] = '.'
                cols.remove(col)
                diagonals.remove(row - col)
                anti_diagonals.remove(row + col)

    result = []
    board = [["."] * n for _ in range(n)]
    cols, diagonals, anti_diagonals = set(), set(), set()
    backtrack(0)
    return result


try:
    n = int(input("Enter the number of queens (N): "))
    if n < 1:
        raise ValueError
    solutions = solve_n_queens(n)
    print(f"\nTotal solutions for {n}-Queens: {len(solutions)}\n")
    for idx, solution in enumerate(solutions, 1):
        print(f"Solution {idx}:")
        for row in solution:
            print(row)
        print()
except ValueError:
    print("Please enter a valid positive integer for N.")
