#Assignment Week 1 Prove: Developer 
#This program runs a tictactoe game
#Author: Val Lorence Labisa

def main():
    player = next_player("")
    board = create_board()
    has_winner(board) == False
    draw(board) == False


def create_board():
    board = []
    square = 0
    for square in range(9):
        board.append(square+1)
    return board


def print_board(board):
    print()
    print(f'{board[0]}|{board[1]}|{board[2]}')
    print('-+-+-')
    print(f'{board[3]}|{board[4]}|{board[5]}')
    print('-+-+-')
    print(f'{board[6]}|{board[7]}|{board[8]}')
    print()