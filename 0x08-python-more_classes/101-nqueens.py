#!/usr/bin/python3
import sys

def nqueens(board_size):
    def is_valid(row, col):
        for i in range(row):
            if board[i][col] == 1:
                return False
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        for i, j in zip(range(row, -1, -1), range(col, board_size)):
            if board[i][j] == 1:
                return False
        return True

    def solve(row):
        if row == board_size:
            return True
        for col in range(board_size):
            if is_valid(row, col):
                board[row][col] = 1
                if solve(row + 1):
                    return True
                board[row][col] = 0
        return False

    board = [[0 for _ in range(board_size)] for _ in range(board_size)]
    if not solve(0):
        print("No solution found.")
        return
    for row in board:
        print(row)


def main():
    args = sys.argv[1:]
    if len(args) != 1:
        print("Usage: python nqueens.py N")
        return
    board_size = int(args[0])
    nqueens(board_size)


if __name__ == "__main__":
    main()
