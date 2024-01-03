import numpy as np
import random as r


def print_board(board):
    for row in board:
        print(row)


def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


def user(board):
    while True:
        try:
            row = int(input("Enter row(0, 1, or 2): "))
            col = int(input("Enter column(0, 1, or 2): "))
            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == '':
                return row, col
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def computer(board):
    empty_positions = [(i, j) for i in range(3) for j in range(3) if board[i][j] == '']
    return r.choice(empty_positions)


def is_board_full(board):
    return all(board[i][j] != '' for i in range(3) for j in range(3))


def play_tic_tac_toe():
    # Initialize the Tic-Tac-Toe board
    # creating an empty 3x3 matrix box
    board = np.empty((3, 3), dtype=str)

    # Choose between X and O
    uin = input("Enter which character to use (X or O): ")
    # print the board to show the board of tic tac toe
    while True:
        print_board(board)

        # User's move
        row, col = user(board)
        board[row][col] = uin

        # check the winner
        if check_winner(board, uin):
            print_board(board)
            print("Congratulations! You win!")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        # Computer's move
        print("Computer's move:")
        comp_row, comp_col = computer(board)
        cin = 'O' if uin == 'X' else 'X'
        board[comp_row][comp_col] = cin

        # Check if the computer has won
        if check_winner(board, cin):
            print_board(board)
            print("Sorry, you lose. Better luck next time!")
            break

        # Check if the board is full (a tie)
        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break


if __name__ == "__main__":
    play_tic_tac_toe()
