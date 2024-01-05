#!/usr/bin/python3
import sys


def init_board(n):
    return [[' ' for _ in range(n)] for _ in range(n)]


def board_deepcopy(board):
    return [row[:] for row in board]


def get_solution(board):
    return [[r, c] for r, row in enumerate(board) for c, value in enumerate(row) if value == "Q"]

def xout(board, row, col):
    n = len(board)
    for c in range(col + 1, n):
        board[row][c] = 'x'
    for c in range(col - 1, -1, -1):
        board[row][c] = 'x'
    for r in range(row + 1, n):
        board[r][col] = 'x'
    for r in range(row - 1, -1, -1):
        board[r][col] = 'x'
    for r, c in zip(range(row + 1, n), range(col + 1, n)):
        if c >= n: break
        board[r][c] = 'x'
    for r, c in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if c < 0: break
        board[r][c] = 'x'
    for r, c in zip(range(row - 1, -1, -1), range(col + 1, n)):
        if c >= n: break
        board[r][c] = 'x'
    for r, c in zip(range(row + 1, n), range(col - 1, -1, -1)):
        if c < 0: break
        board[r][c] = 'x'

def recursive_solve(board, row, queens, solutions):
    n = len(board)
    if queens == n:
        solutions.append(get_solution(board))
        return solutions

    for c in range(n):
        if board[row][c] == ' ':
            tmp_board = board_deepcopy(board)
            tmp_board[row][c] = 'Q'
            xout(tmp_board, row, c)
            solutions = recursive_solve(tmp_board, row + 1, queens + 1, solutions)

    return solutions

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit() or int(sys.argv[1]) < 4:
        print("Usage: nqueens N (N must be an integer greater than or equal to 4)")
        sys.exit(1)

    board_size = int(sys.argv[1])
    chessboard = init_board(board_size)
    solutions = recursive_solve(chessboard, 0, 0, [])

    for solution in solutions:
        print(solution)
