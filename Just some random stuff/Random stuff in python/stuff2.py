import chess

# Initialize the chessboard
board = chess.Board()

# Function to print the chessboard
def print_board(board):
    print(board)

# Function to check for checkmate
def check_for_checkmate(board):
    if board.is_checkmate():
        if board.turn:
            print("Checkmate! Black wins.")
        else:
            print("Checkmate! White wins.")
        return True
    return False

# Main game loop
while True:
    print_board(board)
    
    if check_for_checkmate(board):
        break
    
    move_uci = input("Enter your move (UCI format) or 'q' to quit: ")
    
    if move_uci == 'q':
        break
    
    try:
        move = chess.Move.from_uci(move_uci)
        if move in board.legal_moves:
            board.push(move)
        else:
            print("Invalid move. Try again.")
    except ValueError:
        print("Invalid move format. Use UCI format (e.g., 'e2e4').")

print("Game over.")
