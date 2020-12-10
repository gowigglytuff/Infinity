from test.gamestate import *
from test.dudes import *

gd = GameData

# Define tiles
class Tile(object):
    def __init__(self, x, y, full):
        self.X = x
        self.Y = y
        self.full = full

    def __str__(self):
        return str(self.X) + ", " + str(self.Y) + ", " + str(self.full)

    def interact(self):
        return self.full



# def update_tiles():
#     for name, o in gd.characters.items():
#         tiles_list_2d[int(o.x)][int(o.y)].full = o.name
#     for name, o in gd.prop.items():
#         tiles_list_2d[int(o.x)][int(o.y)].full = "full"


A1 = Tile(1, 1, "none")
A2 = Tile(1, 2, "none")
A3 = Tile(1, 3, "none")
A4 = Tile(1, 4, "none")
A5 = Tile(1, 5, "none")
A6 = Tile(1, 6, "none")
A7 = Tile(1, 7, "none")
A8 = Tile(1, 8, "none")

B1 = Tile(2, 1, "none")
B2 = Tile(2, 2, "none")
B3 = Tile(2, 3, "none")
B4 = Tile(2, 4, "none")
B5 = Tile(2, 5, "none")
B6 = Tile(2, 6, "none")
B7 = Tile(2, 7, "none")
B8 = Tile(2, 8, "none")

C1 = Tile(3, 1, "none")
C2 = Tile(3, 2, "none")
C3 = Tile(3, 3, "none")
C4 = Tile(3, 4, "none")
C5 = Tile(3, 5, "none")
C6 = Tile(3, 6, "none")
C7 = Tile(3, 7, "none")
C8 = Tile(3, 8, "none")

D1 = Tile(4, 1, "none")
D2 = Tile(4, 2, "none")
D3 = Tile(4, 3, "none")
D4 = Tile(4, 4, "none")
D5 = Tile(4, 5, "none")
D6 = Tile(4, 6, "none")
D7 = Tile(4, 7, "none")
D8 = Tile(4, 8, "none")

E1 = Tile(5, 1, "none")
E2 = Tile(5, 2, "none")
E3 = Tile(5, 3, "none")
E4 = Tile(5, 4, "none")
E5 = Tile(5, 5, "none")
E6 = Tile(5, 6, "none")
E7 = Tile(5, 7, "none")
E8 = Tile(5, 8, "none")

F1 = Tile(6, 1, "none")
F2 = Tile(6, 2, "none")
F3 = Tile(6, 3, "none")
F4 = Tile(6, 4, "none")
F5 = Tile(6, 5, "none")
F6 = Tile(6, 6, "none")
F7 = Tile(6, 7, "none")
F8 = Tile(6, 8, "none")

G1 = Tile(7, 1, "none")
G2 = Tile(7, 2, "none")
G3 = Tile(7, 3, "none")
G4 = Tile(7, 4, "none")
G5 = Tile(7, 5, "none")
G6 = Tile(7, 6, "none")
G7 = Tile(7, 7, "none")
G8 = Tile(7, 8, "none")

H1 = Tile(8, 1, "none")
H2 = Tile(8, 2, "none")
H3 = Tile(8, 3, "none")
H4 = Tile(8, 4, "none")
H5 = Tile(8, 5, "none")
H6 = Tile(8, 6, "none")
H7 = Tile(8, 7, "none")
H8 = Tile(8, 8, "none")

tiles_list = [A1, A2, A3, A4, A5, A6, A7, A8, B1, B2, B3, B4, B5, B6, B7, B8, C1, C2, C3, C4, C5, C6, C7, C8, D1, D2,
         D3, D4, D5, D6, D7, D8, E1, E2, E3, E4, E5, E6, E7, E8, F1, F2, F3, F4, F5, F6, F7, F8, G1, G2, G3, G4, G5,
        G6, G7, G8, H1, H2, H3, H4, H5, H6, H7, H8]

tiles_list_2d = [[A1, A2, A3, A4, A5, A6, A7, A8],
                 [B1, B2, B3, B4, B5, B6, B7, B8],
                 [C1, C2, C3, C4, C5, C6, C7, C8],
                 [D1, D2, D3, D4, D5, D6, D7, D8],
                 [E1, E2, E3, E4, E5, E6, E7, E8],
                 [F1, F2, F3, F4, F5, F6, F7, F8],
                 [G1, G2, G3, G4, G5, G6, G7, G8],
                 [H1, H2, H3, H4, H5, H6, H7, H8]]

