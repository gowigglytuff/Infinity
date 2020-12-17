from test.gamestate import *

gd = GameData()
gc = GameContoller(gd)


# Define tiles
class Tile(object):
    def __init__(self, x, y, full, object_filling, filling_type):
        self.x = x
        self.y = y
        self.full = full
        self.object_filling = object_filling
        self.filling_type = filling_type

    # def __str__(self):
    #     return str(self.X) + ", " + str(self.Y) + ", " + str(self.full) + ", " + str(self.object_filling)

    def interact(self):
        return self.object_filling

    # def get_object_filling(self, source):
    #     for drawable in source:
    #         if drawable.location == gc.room:
    #             gd.tiles[drawable.x][drawable.y].full = True
    #             gd.tiles[drawable.x][drawable.y].object_filling = drawable.name
    #             gd.tiles[drawable.x][drawable.y].filling_type = drawable.classification

    def reset_object_filling(self, source):
        self.full = False
        self.object_filling = "none"
        self.filling_type = "none"

    def get_fill(self):
        print(self.full, self.object_filling)

    def fill_tile(self, full, object_filling, filling_type):
        self.full = full
        self.object_filling = object_filling
        self.filling_type = filling_type


tiles_list_2d = []