import pygame
from pygame import mixer
import math
import time
from test.spritesheet import Spritesheet

from test.tiles import *



class Game(object):
    def __init__(self, state, tick, tock):
        self.state = state
        self.tick = tick
        self.tock = tock


playing = Game("play", 0, 0)


class GameData(object):
    def __init__(self):
        self.characters = {}
        self.player = {}
        self.settings = {}
        self.settings["resolution"] = (416, 416)
        self.settings["FPS"] = 30
        self.BG = {}
        self.prop = {}
        self.menu = {}
        self.cursor = {}
        self.item = {}
        self.item_list = {}
        self.audio = {}
        self.bathroom_characters = {}
        self.bathroom_props = {}
        self.tiles = []
        self.tiles_array = []
        self.game_width = 8
        self.game_height = 8
        self.rooms = {}
        self.doors = {}
        self.empty_tiles = []

    def add_character(self, character_name, character_object):
        self.characters[character_name] = character_object

    def add_bathroom_charatcers(self, character_name, character_object):
        self.bathroom_characters[character_name] = character_object

    def add_bathroom_prop(self, prop_name, prop_object):
        self.bathroom_props[prop_name] = prop_object


    def add_player(self, player_name, player_object):
        self.player[player_name] = player_object

    def add_bg(self, bg_name, bg_object):
        self.BG[bg_name] = bg_object

        print(bg_name, bg_object)

    def add_prop(self, prop_name, prop_object):
        self.prop[prop_name] = prop_object

    def add_menu(self, menu_name, menu_object):
        self.menu[menu_name] = menu_object

    def add_cursor(self, cursor_name, cursor_object):
        self.cursor[cursor_name] = cursor_object

    def add_item(self, item_name, item_object):
        self.item[item_name] = item_object

    def add_audio(self, audio_name, audio_object):
        self.audio[audio_name] = audio_object

    def add_item_list(self, item_list_name, item_list_object):
        self.item_list[item_list_name] = item_list_object

    def get_all_drawables(self):
        return list(self.characters.values()) + list(self.player.values()) + list(self.prop.values())

    def get_all_drawables_bathroom(self):
        return list(self.bathroom_characters.values()) + list(self.player.values()) + list(self.bathroom_props.values())

    def get_all_items(self):
        return list(self.item.keys())

    def add_room(self, room_name, room_object):
        self.rooms[room_name] = room_object

    def add_door(self, door_name, door_object):
        self.doors[door_name] = door_object

    def add_tile(self, tile_object):
        self.tiles.append(tile_object)


class GameContoller(object):

    IN_MENU = 0
    IN_GAME = 1
    ANIMATING = 2
    CUTSCENE = 3
    TALKING = 4
    START_MENU = 5
    GIFT = 6
    PROPOSITION = 7
    INVENTORY = 8
    GIFT_RECEIVED = 9
    BAR = 10
    INFORMATION = 11
    SEEDER = 12
    ANTON = 13
    REQUEST = 14
    FOLLOW = 15
    SASS = 16
    CUTSCENE1 = 17
    FOUND_ITEM = 18

    DISCO = "disco"
    BATHROOM = "bathroom"

    NONE = "none"
    MENU = "menu"

    def __init__(self, game_data):
        self.screen = pygame.display.set_mode(game_data.settings["resolution"])
        self.clock = pygame.time.Clock()
        self._FPS = game_data.settings["FPS"]
        self.game_state = GameContoller.IN_GAME
        self.tock = 0
        self.room = "disco"
        self.canvas = "none"


    def tick(self):
        self.clock.tick(self._FPS)

    # decide what order to draw aliens based on y value
    # draw aliens

class Hour(object):
    def __init__(self, screen):
        self.initiate_clock = 0
        self.begin_hours = 10
        self.begin_minutes = 0
        self.minutes_add = 0
        self.set_timer = int(math.trunc(time.perf_counter()))
        self.screen = screen
        self.item_counter = False

    def print_clock(self):

        if self.begin_minutes == 6:
            self.begin_hours += 1
            self.begin_minutes = 0

        if self.set_timer + 10 == int(math.trunc(time.perf_counter())):
            self.set_timer = int(math.trunc(time.perf_counter()))
            self.item_counter = True
            self.begin_minutes += 1

        my_font = pygame.font.Font("assets/PokemonGB-RAeo.ttf", 10)
        label3 = my_font.render(str(self.begin_hours) + ":" + str(self.begin_minutes) + str(self.minutes_add) + "pm", 1, (255, 255, 255))
        self.screen.blit(label3, (320, 64))

class Image(object):
    def __init__(self, x, y, img_file_name_list, width=32, height=40):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.img_list = [file_name for file_name in
                         img_file_name_list]
        self.cur_img = 0
        self.img = self.img_list[self.cur_img]

    def set_image(self, img_number):
        self.cur_img = img_number
        self.img = self.img_list[self.cur_img]

    def draw(self, screen):
        screen.blit(Spritesheet(self.img).image_at((0, 0, self.width, self.height)), [self.x, self.y])


class Feature(Image):
    def __init__(self, x, y, img_file_name_list, name, classification, location, on_stage):
        super().__init__(x, y, img_file_name_list)
        self.name = name
        self.classification = classification
        self.location = location
        self.on_stage = on_stage
        self.img_list = [file_name for file_name in
                         img_file_name_list]
        self.cur_img = 0
        self.img = self.img_list[self.cur_img]

    def set_image(self, img_number):
        self.cur_img = img_number
        self.img = self.img_list[self.cur_img]


    def draw(self, screen):
        screen.blit(Spritesheet(self.img).image_at((0, 0, self.width, self.height)), [self.x, self.y])

    # def interact(self):
    #     print("INTERACT!", self)


class Character(Feature):
    def __init__(self, x, y, img_file_name_list, points, emote, offset, name, classification, feeling, origin_x, origin_y, on_stage, location):
        super().__init__(x, y, img_file_name_list, name, classification, location, on_stage)
        self.feeling = feeling
        self.offset = offset
        self.emote = emote
        self.name = name
        self.printing_priority = 2
        self.phrases = {}
        self.emotions = {}
        self.points = points
        self.phrase_counter = 0
        self.origin_x = origin_x
        self.origin_y = origin_y
        self.img_list = [file_name for file_name in
                         img_file_name_list]
        self.cur_img = 0
        self.img = self.img_list[self.cur_img]

    def draw(self, screen):
        screen.blit((Spritesheet(self.img).image_at((0, 0, 32, 40))), [self.x * 32 + self.offset, self.y * 32 - 16])


    def print_phrase(self, screen, line):
        my_font = pygame.font.Font("assets/PokemonGB-RAeo.ttf", 10)
        label1 = my_font.render(self.phrases[line][0], 1, (255, 255, 255))
        label2 = my_font.render(self.phrases[line][1], 1, (255, 255, 255))
        label3 = my_font.render(self.phrases[line][2], 1, (255, 255, 255))
        screen.blit(label1, (142, 332))
        screen.blit(label2, (142, 352))
        screen.blit(label3, (142, 372))

    def print_name(self, screen):
        my_font = pygame.font.Font("assets/PressStart2P-Regular.ttf", 10)
        title = my_font.render(self.name + "[" + str(self.points) + "]", 1, (255, 255, 255))
        screen.blit(title, (137, 310))

    def display(self, screen, line):
        screen.blit((Spritesheet(self.emotions[line][0]).image_at((0, 0, 96, 120))), [42, 292])

    def reset_phrase_counter(self):
        if self.phrase_counter > self.points:
            self.phrase_counter = 0

    def add_point(self):
        self.points += 1
        self.phrase_counter = self.points

    def fill_points(self):
        self.points += (10-self.points)
        self.phrase_counter = self.points

class Player(Feature):
    def __init__(self, x, y, img_file_name_list, offset, facing, follow, name, classification, location, on_stage, item_received):
        super().__init__(x, y, img_file_name_list, name, classification, location, on_stage)
        self.classification = classification
        self.name = name
        self.offset = offset
        self.facing = facing
        self.printing_priority = 2
        self.follow = follow
        self.item_received = item_received
        self.img_list = [file_name for file_name in
                         img_file_name_list]
        self.cur_img = 0
        self.img = self.img_list[self.cur_img]

    def draw(self, screen):
        screen.blit((Spritesheet(self.img).image_at((0, 0, 32, 40))), [self.x * 32 + self.offset, self.y * 32 - 16])


class Prop(Feature):
    def __init__(self, x, y, img_file_name_list, name,  classification, on_stage, location):
        super().__init__(x, y, img_file_name_list, name, classification, location, on_stage)
        self.printing_priority = 1
        self.img_list = [file_name for file_name in
                         img_file_name_list]
        self.cur_img = 0
        self.img = self.img_list[self.cur_img]

    def draw(self, screen):
        screen.blit((Spritesheet(self.img).image_at((0, 0, 32, 40))), [self.x * 32, self.y * 32-16])


class StageProp(Prop):
    def __init__(self, x, y, img_file_name_list, name,  classification, location, on_stage):
        super().__init__(x, y, img_file_name_list, name,  classification, on_stage, location)
        self.img_list = [file_name for file_name in
                         img_file_name_list]
        self.cur_img = 0
        self.img = self.img_list[self.cur_img]

    def draw(self, screen):
        screen.blit((Spritesheet(self.img).image_at((0, 0, 32, 40))), [self.x * 32, self.y * 32 - 8])


class BG(Image):
    def __init__(self, x, y, name, img_file_name_list):
        super().__init__(x, y, name, img_file_name_list)
        self.name = name
        self.img_list = [file_name for file_name in
                         img_file_name_list]
        self.cur_img = 0
        self.img = self.img_list[self.cur_img]

    def draw(self, screen):
        screen.blit(pygame.image.load(self.img).convert_alpha(), (self.x*32, self.y*32))


class Phrase(object):
    def __init__(self, text, on, x, y, colour, size):
        self.text = text
        self.on = on
        self.X = x
        self.Y = y
        self.colour = colour
        self.size = size

    def write(self, screen):
        my_font = pygame.font.Font("assets/PressStart2P-Regular.ttf", self.size)
        label = my_font.render(self.text, 1, self.colour)
        text = screen.blit(label,
                           (self.X, self.Y))
        return text


class Talk(Phrase):
    def __init__(self, text, on, y):
        super().__init__(text, on, 110, (y*20)+280, (255, 255, 255), 10)


    def write(self, screen):
        my_font = pygame.font.Font("assets/PressStart2P-Regular.ttf", self.size)
        label1 = my_font.render(self.text[0], 1, self.colour)
        label2 = my_font.render(self.text[1], 1, self.colour)
        label3 = my_font.render(self.text[2], 1, self.colour)
        text = screen.blit(label1, (self.X, self.Y))
        text = screen.blit(label2, (self.X, self.Y+20))
        text = screen.blit(label3, (self.X, self.Y+40))
        return text


class Menu(object):
    def __init__(self, screen, size, x, y, opt1, menu_go, cursor):
        self.screen = screen
        self.x = x
        self.y = y
        self.size = size
        self.opt1 = opt1
        self.menu_go = menu_go
        self.cursor = cursor

    def print_menu(self):
        for x in self.size:
            my_font = pygame.font.Font("assets/PressStart2P-Regular.ttf", 10)
            item = my_font.render(self.opt1[x], 1, (255, 255, 255))
            self.screen.blit(item, (self.x, self.y + (x*25)))

    def menu_len(self):
        total = len(self.size)
        return total


class Cursor(object):
    def __init__(self, screen, menu, cursor_go, option):
        self.y = menu.y
        self.menu = menu
        self.x = menu.x
        self.cursor_go = cursor_go
        self.screen = screen
        self.option = option

    def print_cursor(self):
        my_font = pygame.font.Font("assets/PressStart2P-Regular.ttf", 10)
        cursor1 = my_font.render("-", 1, (255, 255, 255))
        self.screen.blit(cursor1, (self.x-15, self.y))

    def cursor_down(self):
        if self.y == self.menu.y + self.menu.size[-1]*25:
            self.y = self.menu.y
        else:
            self.y += 25

    def cursor_up(self):
        if self.y == self.menu.y:
            self.y = self.menu.y + self.menu.size[-1]*25
        else:
            self.y -= 25
    def get_cursor_position(self):
        cursor_position = self.y
        return cursor_position

    def get_item(self):
        return self.menu.opt1[int(((self.y - 50) / 25))]

    def cursor_reset(self):
        self.y = self.menu.y


class ItemCursor(Cursor):
    def __init__(self, screen, menu, cursor_go, option):
        super(). __init__(screen, menu, cursor_go, option)
        self.y = menu.y

    def cursor_down(self):
        if self.y == self.menu.y + (self.menu.total_items)*25:
            self.y = self.menu.y
        else:
            self.y += 25
    def cursor_up(self):
        if self.y == self.menu.y:
            self.y = self.menu.y + (self.menu.total_items)*25
        else:
            self.y -= 25

    def get_item(self):
        return self.menu.item_order[int(((self.y-self.menu.y)/25))].name


class ItemList(object):
    def __init__(self, screen, opt1, item_list_go, source, key):
        self.screen = screen
        self.x = 312
        self.y = 132
        self.size = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.opt1 = opt1
        self.item_list_go = item_list_go
        self.source = source
        self.key = key
        self.successes = 0
        self.total_items = 0
        self.item_order = []

    def print_item_list(self):
        self.item_order.clear()
        for v in self.size:
            if self.source[self.key[v]].quantity > 0:
                my_font = pygame.font.Font("assets/PressStart2P-Regular.ttf", 10)
                item = my_font.render(self.source[self.key[v]].name, 1, (255, 255, 255))
                item2 = my_font.render(str(self.source[self.key[v]].quantity), 1, (255, 255, 255))
                self.screen.blit(item, (self.x, self.y + self.successes * 25))
                self.screen.blit(item2, (self.x + 75, self.y + self.successes * 25))
                self.successes += 1
                self.item_order.append(self.source[self.key[v]])
        self.total_items = self.successes
        self.successes = 0
        exit_menu = my_font.render("Exit", 1, (255, 255, 255))
        self.screen.blit(exit_menu, (self.x, self.y + self.total_items * 25))


    def item_list_len(self):
        total = len(self.size)
        return total


class Item(object):
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def item_got(self, screen):
        my_font = pygame.font.Font("assets/PressStart2P-Regular.ttf", 10)
        item = my_font.render("You got (1) " + self.name +"!", 1, (255, 255, 255))
        screen.blit(item, (120, 340))
    print("woot")
        # gd.menu["menu1"].menu_len():


class Audio(object):
    def __init__(self, name, file):
        self.name = name
        self.file = file

    def sing(self):
        mixer.music.load(self.file)
        mixer.music.set_volume(0.7)
        mixer.music.play(-1)


# Define tiles
class Tile(object):
    def __init__(self, x, y, full, object_filling, filling_type, has_item, item_name):
        self.x = x
        self.y = y
        self.full = full
        self.object_filling = object_filling
        self.filling_type = filling_type
        self.has_item = has_item
        self.item_name = item_name

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


class Room(object):
    def __init__(self, name, edge_x, edge_y, width, height, offset_x, offset_y, doors_list, images_list):
        self.name = name
        self.edge_x = edge_x
        self.edge_y = edge_y
        self.width = width
        self.height = height
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.doors_list = doors_list
        self.tiles_array = []
        self.images_list = images_list

        self.tiles_array = []
        self.tiles_list = []



    def generate_room_grid(self):
        for section in range(self.width + 3):
            section_name = []
            self.tiles_array.append(section_name)


        for letter in range(self.width + 2):
            for number in range(self.height + 3):
                spot_name = Tile(letter, number, False, "none", "none", False, "none")
                self.tiles_array[letter].append(spot_name)
                self.tiles_list.append(spot_name)


class Door(object):
    def __init__(self, room_from, room_to, x, y, door_exit_x, door_exit_y):
        self.room_from = room_from
        self.room_to = room_to
        self.x = x
        self.y = y
        self.door_exit_x = door_exit_x
        self.door_exit_y = door_exit_y