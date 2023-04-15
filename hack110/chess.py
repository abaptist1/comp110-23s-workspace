"""Sample Verion of Chess"""

import pygame
import sys

# Constants for window size and colors
WIDTH = 800
HEIGHT = 800
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Initialize Pygame
pygame.init()

# Set up the window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess")

# Load chess pieces images
chess_pieces = {
    "wp": pygame.image.load("hack110/assets/white_pawn.png"),
    "wr": pygame.image.load("hack110/assets/white_rook.png"),
    "wb": pygame.image.load("hack110/assets/white_bishop.png"),
    "wn": pygame.image.load("hack110/assets/white_knight.png"),
    "wq": pygame.image.load("hack110/assets/white_queen.png"),
    "wk": pygame.image.load("hack110/assets/white_king.png"),
    "bp": pygame.image.load("hack110/assets/black_pawn.png"),
    "br": pygame.image.load("hack110/assets/black_rook.png"),
    "bb": pygame.image.load("hack110/assets/black_bishop.png"),
    "bn": pygame.image.load("hack110/assets/black_knight.png"),
    "bq": pygame.image.load("hack110/assets/black_queen.png"),
    "bk": pygame.image.load("hack110/assets/black_king.png")
}

# Define the initial chess board state
board = [
    ["br", "bn", "bb", "bq", "bk", "bb", "bn", "br"],
    ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
    ["wr", "wn", "wb", "wq", "wk", "wb", "wn", "wr"]
]

# Track selected piece position
selected_piece = None

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            col = pos[0] // 100
            row = pos[1] // 100
            if selected_piece:
                # Move the selected piece to the clicked position if it's a valid move
                if (row, col) in selected_piece.get_valid_moves(board):
                    board[row][col] = selected_piece.piece_type
                    board[selected_piece.row][selected_piece.col] = ""
                    selected_piece.move(row, col)
                    selected_piece = None
                else:
                    # Deselect the piece if the move is not valid
                    selected_piece = None
            else:
                # Select a piece if there is one at the clicked position
                piece_type = board[row][col]
                if piece_type:
                    selected_piece = ChessPiece(piece_type, row, col)

    # Draw the chess board
    window.fill(WHITE)
    for row in range(8):
        for col in range(8):
            pygame.draw.rect(window, BLACK if (row + col) % 2 == 0 else WHITE,
                             pygame.Rect(col * 100, row * 100, 100, 100))
            piece = board[row][col]
            if piece:
                image = chess_pieces[piece]
                window
