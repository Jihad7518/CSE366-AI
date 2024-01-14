# Tic-Tac-Toe Board
class Board:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    def print_board(self):
        for row in self.board:
            print("|".join(row))
            print("-----")

    def is_full(self):
        for row in self.board:
            if ' ' in row:
                return False
        return True

    def is_winner(self, player):
        # Check rows, columns, and diagonals for a winner
        for i in range(3):
            if all(self.board[i][j] == player for j in range(3)) or \
               all(self.board[j][i] == player for j in range(3)):
                return True
        if all(self.board[i][i] == player for i in range(3)) or \
           all(self.board[i][2 - i] == player for i in range(3)):
            return True
        return False

    def make_move(self, row, col, player):
        if self.board[row][col] == ' ':
            self.board[row][col] = player
            return True
        return False

    def undo_move(self, row, col):
        self.board[row][col] = ' '

# Minimax Algorithm with Alpha-Beta Pruning
def minimax_alpha_beta(board, depth, alpha, beta, maximizing_player):
    if board.is_winner('X'):
        return -1
    elif board.is_winner('O'):
        return 1
    elif board.is_full():
        return 0

    if maximizing_player:
        max_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if board.board[i][j] == ' ':
                    board.make_move(i, j, 'O')
                    eval = minimax_alpha_beta(board, depth + 1, alpha, beta, False)
                    board.undo_move(i, j)
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break  # Beta cutoff
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board.board[i][j] == ' ':
                    board.make_move(i, j, 'X')
                    eval = minimax_alpha_beta(board, depth + 1, alpha, beta, True)
                    board.undo_move(i, j)
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break  # Alpha cutoff
        return min_eval

# Find the best move using Minimax with Alpha-Beta Pruning
def find_best_move_alpha_beta(board):
    best_val = float('-inf')
    best_move = (-1, -1)
    alpha = float('-inf')
    beta = float('inf')

    for i in range(3):
        for j in range(3):
            if board.board[i][j] == ' ':
                board.make_move(i, j, 'O')
                move_val = minimax_alpha_beta(board, 0, alpha, beta, False)
                board.undo_move(i, j)

                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val

                alpha = max(alpha, move_val)

    return best_move

# Example: Play Tic-Tac-Toe against the Minimax algorithm with Alpha-Beta Pruning
if __name__ == "__main__":
    game_board = Board()

    while not game_board.is_full() and not game_board.is_winner('X') and not game_board.is_winner('O'):
        # Player's move
        print("Player's turn:")
        game_board.print_board()
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter column (0-2): "))
        if game_board.make_move(row, col, 'X'):
            game_board.print_board()
        else:
            print("Invalid move. Try again.")
            continue

        # Check if the player wins
        if game_board.is_winner('X'):
            print("Player wins!")
            break

        # Minimax's move
        print("Minimax's turn:")
        best_move = find_best_move_alpha_beta(game_board)
        game_board.make_move(best_move[0], best_move[1], 'O')
        game_board.print_board()

        # Check if Minimax wins
        if game_board.is_winner('O'):
            print("Minimax wins!")
            break

    if game_board.is_full() and not game_board.is_winner('X') and not game_board.is_winner('O'):
        print("It's a draw!")

