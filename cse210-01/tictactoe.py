#Assignment Week 1 Prove: Developer - Solo Code Submission
# This program runs a tictactoe game
#Author: Val Lorence Labisa

def main():
    player = next_player("")
    board = create_board()

    while not (has_winner(board) or draw(board)):
        print_board(board)
        move(player, board)
        player = next_player(player)
    
    print_board(board) 
    if has_winner(board) == True:
        if player == 'x':
            print("Player o wins!")
        elif player == 'o':
            print("Player x wins!")

    elif has_winner(board) == False:
        print("It's a draw.")
    print("\nThank you for playing.")

def print_board(board):
    print()
    print(f'{board[0]}|{board[1]}|{board[2]}')
    print('-+-+-')
    print(f'{board[3]}|{board[4]}|{board[5]}')
    print('-+-+-')
    print(f'{board[6]}|{board[7]}|{board[8]}')
    print()

def create_board():
    board = []
    square = 0
    for square in range(9):
        board.append(square+1)
    return board

def has_winner(board):
    if board[0] == board[1] == board[2] or board[3] == board[4] == board[5] or board[6] == board[7] == board[8] or board[0] == board[3] == board[6] or board[1] == board[4] == board[7] or board[2] == board[5] == board[8] or board[0] == board[4] == board[8] or board[2] == board[4] == board[6]:
        return True

def draw(board):
    for square in range(9):
        if board[square] != "x" and board[square] != "o":
            return False
    return True

def next_player(current):
    if current == "" or current == "o":
        return "x"
    elif current == "x":
        return "o"

def move(player, board):
    square = int(input(f"{player}'s turn to choose a square (1-9): "))
    board[square - 1] = player


if __name__ == "__main__":
    main()