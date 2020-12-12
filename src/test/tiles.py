from test.gamestate import *
from test.dudes import *

gd = GameData()
gc = GameContoller(gd)
drawables_list = gd.get_all_drawables()

# Define tiles
class Tile(object):
    def __init__(self, x, y, full, object_filling, filling_type):
        self.X = x
        self.Y = y
        self.full = full
        self.object_filling = object_filling
        self.filling_type = filling_type

    # def __str__(self):
    #     return str(self.X) + ", " + str(self.Y) + ", " + str(self.full) + ", " + str(self.object_filling)

    def interact(self):
        return self.object_filling

    def get_object_filling(self, source):
        for tile in tiles_list:
            for drawable in source:
                if drawable.x == tile.X and drawable.y == tile.Y:
                    tile.full = True
                    tile.object_filling = drawable.name
                    tile.filling_type = drawable.classification

    def reset_object_filling(self):
        for tile in tiles_list:
            tile.full = False
            tile.object_filling = "none"
            tile.filling_type = "none"

    def get_fill(self):
        print(self.full, self.object_filling)


# def update_tiles():
#     for name, o in gd.characters.items():
#         tiles_list_2d[int(o.x)][int(o.y)].full = o.name
#     for name, o in gd.prop.items():
#         tiles_list_2d[int(o.x)][int(o.y)].full = "full"


A1 = Tile(0, 0, False, "none", "none")
A2 = Tile(0, 1, False, "none", "none")
A3 = Tile(0, 2, False, "none", "none")
A4 = Tile(0, 3, False, "none", "none")
A5 = Tile(0, 4, False, "none", "none")
A6 = Tile(0, 5, False, "none", "none")
A7 = Tile(0, 6, False, "none", "none")
A8 = Tile(0, 7, False, "none", "none")

B1 = Tile(1, 0, False, "none", "none")
B2 = Tile(1, 1, False, "none", "none")
B3 = Tile(1, 2, False, "none", "none")
B4 = Tile(1, 3, False, "none", "none")
B5 = Tile(1, 4, False, "none", "none")
B6 = Tile(1, 5, False, "none", "none")
B7 = Tile(1, 6, False, "none", "none")
B8 = Tile(1, 7, False, "none", "none")

C1 = Tile(2, 0, False, "none", "none")
C2 = Tile(2, 1, False, "none", "none")
C3 = Tile(2, 2, False, "none", "none")
C4 = Tile(2, 3, False, "none", "none")
C5 = Tile(2, 4, False, "none", "none")
C6 = Tile(2, 5, False, "none", "none")
C7 = Tile(2, 6, False, "none", "none")
C8 = Tile(2, 7, False, "none", "none")

D1 = Tile(3, 0, False, "none", "none")
D2 = Tile(3, 1, False, "none", "none")
D3 = Tile(3, 2, False, "none", "none")
D4 = Tile(3, 3, False, "none", "none")
D5 = Tile(3, 4, False, "none", "none")
D6 = Tile(3, 5, False, "none", "none")
D7 = Tile(3, 6, False, "none", "none")
D8 = Tile(3, 7, False, "none", "none")

E1 = Tile(4, 0, False, "none", "none")
E2 = Tile(4, 1, False, "none", "none")
E3 = Tile(4, 2, False, "none", "none")
E4 = Tile(4, 3, False, "none", "none")
E5 = Tile(4, 4, False, "none", "none")
E6 = Tile(4, 5, False, "none", "none")
E7 = Tile(4, 6, False, "none", "none")
E8 = Tile(4, 7, False, "none", "none")

F1 = Tile(5, 0, False, "none", "none")
F2 = Tile(5, 1, False, "none", "none")
F3 = Tile(5, 2, False, "none", "none")
F4 = Tile(5, 3, False, "none", "none")
F5 = Tile(5, 4, False, "none", "none")
F6 = Tile(5, 5, False, "none", "none")
F7 = Tile(5, 6, False, "none", "none")
F8 = Tile(5, 7, False, "none", "none")

G1 = Tile(6, 0, False, "none", "none")
G2 = Tile(6, 1, False, "none", "none")
G3 = Tile(6, 2, False, "none", "none")
G4 = Tile(6, 3, False, "none", "none")
G5 = Tile(6, 4, False, "none", "none")
G6 = Tile(6, 5, False, "none", "none")
G7 = Tile(6, 6, False, "none", "none")
G8 = Tile(6, 7, False, "none", "none")

H1 = Tile(7, 0, False, "none", "none")
H2 = Tile(7, 1, False, "none", "none")
H3 = Tile(7, 2, False, "none", "none")
H4 = Tile(7, 3, False, "none", "none")
H5 = Tile(7, 4, False, "none", "none")
H6 = Tile(7, 5, False, "none", "none")
H7 = Tile(7, 6, False, "none", "none")
H8 = Tile(7, 7, False, "none", "none")

tiles_list = [A1, A2, A3, A4, A5, A6, A7, A8, B1, B2, B3, B4, B5, B6, B7, B8, C1, C2, C3, C4, C5, C6, C7, C8, D1, D2,
              D3, D4, D5, D6, D7, D8, E1, E2, E3, E4, E5, E6, E7, E8, F1, F2, F3, F4, F5, F6, F7, F8, G1, G2, G3, G4,
              G5, G6, G7, G8, H1, H2, H3, H4, H5, H6, H7, H8]

tiles_list_2d = [[A1, A2, A3, A4, A5, A6, A7, A8],
                 [B1, B2, B3, B4, B5, B6, B7, B8],
                 [C1, C2, C3, C4, C5, C6, C7, C8],
                 [D1, D2, D3, D4, D5, D6, D7, D8],
                 [E1, E2, E3, E4, E5, E6, E7, E8],
                 [F1, F2, F3, F4, F5, F6, F7, F8],
                 [G1, G2, G3, G4, G5, G6, G7, G8],
                 [H1, H2, H3, H4, H5, H6, H7, H8]]

