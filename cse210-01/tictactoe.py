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

def has_winner(board):
    if board[0] == board[1] == board[2] or board[3] == board[4] == board[5] or board[6] == board[7] == board[8] or board[0] == board[3] == board[6] or board[1] == board[4] == board[7] or board[2] == board[5] == board[8] or board[0] == board[4] == board[8] or board[2] == board[4] == board[6]:
        return True

def draw(board):
    for square in range(9):
        if board[square] != "x" and board[square] != "o":
            return False
    return True