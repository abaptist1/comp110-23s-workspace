""" Generates Piece Sprite Groups"""

from chess_sprites import *
from chess_constants import *
from hack110_a.main_game.chess.chess_sprites import Pawn, Bishop, King, Queen, Rook, Knight

w_pawns: list[tuple] = [A2, B2, C2, D2, E2, F2, G2, H2]
new_w_pawns: list[Pawn] = []
for pawn in w_pawns:
    new_w_pawns.append(Pawn(False, pawn))

b_pawns: list[tuple] = [A7, B7, C7, D7, E7, F7, G7, H7]
new_b_pawns: list[Pawn] = []
for pawn in b_pawns:
    new_b_pawns.append(Pawn(True, pawn))


# Individual chess pieces
b_bishop1 = Bishop(True, True)
b_bishop2 = Bishop(True, False)
w_bishop1 = Bishop(False, True)
w_bishop2 = Bishop(False, False)

b_king = King(True)
w_king = King(False)

b_queen = Queen(True)
w_queen = Queen(False)

b_knight1 = Knight(True, True)
b_knight2 = Knight(True, False)
w_knight1 = Knight (False, True)
w_knight2 = Knight(False, False)

b_rook1 = Rook (True, True)
b_rook2 = Rook (True, False)
w_rook1 = Rook (False, True)
w_rook2 = Rook (False, False)



# Group Holding all sprites
all_sprites = pygame.sprite.Group()

all_sprites.add(b_bishop1)
all_sprites.add(b_bishop2)
all_sprites.add(w_bishop1)
all_sprites.add(w_bishop2)

all_sprites.add(b_king)
all_sprites.add(w_king)

all_sprites.add(b_queen)
all_sprites.add(w_queen)

all_sprites.add(b_knight1)
all_sprites.add(b_knight2)
all_sprites.add(w_knight1)
all_sprites.add(w_knight2)

for pawn in new_b_pawns:
    all_sprites.add(pawn)

for pawn in new_w_pawns:
    all_sprites.add(pawn)


all_sprites.add(b_rook1)
all_sprites.add(b_rook2)
all_sprites.add(w_rook1)
all_sprites.add(w_rook2)