import pygame

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
        self.settings["resolution"] = (384, 384)
        self.settings["FPS"] = 30
        self.BG = {}
        self.prop = {}
        self.menu = {}
        self.cursor = {}

    def add_character(self, character_name, character_object):
        self.characters[character_name] = character_object

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

    def get_all_drawables(self):
        return list(self.characters.values()) + list(self.player.values()) + list(self.prop.values())

class GameContoller(object):

    IN_MENU = 0
    IN_GAME = 1
    ANIMATING = 2
    CUTSCENE = 3
    TALKING = 4
    START_MENU = 5

    def __init__(self, game_data):
        self.screen = pygame.display.set_mode(game_data.settings["resolution"])
        self.clock = pygame.time.Clock()
        self._FPS = game_data.settings["FPS"]
        self.game_state = GameContoller.IN_GAME

    def tick(self):
        self.clock.tick(self._FPS)

    # decide what order to draw aliens based on y value
    # draw aliens


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


class Thing(Image):
    def __init__(self, x, y, img_file_name_list, width=32, height=40):
        super().__init__(x, y, img_file_name_list)

    def set_image(self, img_number):
        self.cur_img = img_number
        self.img = self.img_list[self.cur_img]

    def draw(self, screen):
        screen.blit(Spritesheet(self.img).image_at((0, 0, self.width, self.height)), [self.x, self.y])

    # def interact(self):
    #     print("INTERACT!", self)


class Character(Thing):
    def __init__(self, x, y, img_file_name_list, emote, offset, name, width=32, height=40):
        super().__init__(x, y, img_file_name_list, width=32, height=40)
        self.offset = offset
        self.emote = emote
        self.name = name
        self.printing_priority = 2
        self.phrases = {}
        self.emotions = {}
        pass

    def draw(self, screen):
        screen.blit((Spritesheet(self.img).image_at((0, 0, 32, 40))), [self.x * 32 + self.offset, self.y * 32 - 16])

    def print_phrase(self, screen, line):
        my_font = pygame.font.Font("assets/PokemonGB-RAeo.ttf", 10)
        label1 = my_font.render(self.phrases[line][0], 1, (255, 255, 255))
        label2 = my_font.render(self.phrases[line][1], 1, (255, 255, 255))
        label3 = my_font.render(self.phrases[line][2], 1, (255, 255, 255))
        screen.blit(label1, (110, 300))
        screen.blit(label2, (110, 320))
        screen.blit(label3, (110, 340))

    def print_name(self, screen):
        my_font = pygame.font.Font("assets/PokemonGB-RAeo.ttf", 10)
        title = my_font.render(self.name, 1, (255, 255, 255))
        screen.blit(title, (105, 275))

    def display(self, screen, line):
        screen.blit((Spritesheet(self.emotions[line][0]).image_at((0, 0, 96, 120))), [10, 256])

class Player(Image):
    def __init__(self, x, y, img_file_name_list, offset, facing, width=32, height=40):
        super().__init__(x, y, img_file_name_list, width=32, height=40)
        self.offset = offset
        self.facing = facing
        self.printing_priority = 2

    def draw(self, screen):
        screen.blit((Spritesheet(self.img).image_at((0, 0, 32, 40))), [self.x * 32 + self.offset, self.y * 32 - 16])


class Prop(Thing):
    def __init__(self, x, y, img_file_name_list, width=32, height=40):
        super().__init__(x, y, img_file_name_list, width=32, height=40)
        self.printing_priority = 1

    def draw(self, screen):
        screen.blit((Spritesheet(self.img).image_at((0, 0, 32, 40))), [self.x * 32, self.y * 32-16])


class BG(Image):
    def __init__(self, x, y, img_file_name_list):
        super().__init__(x, y, img_file_name_list, width=384, height=384)
        self.dest = [0, 0]

    def draw(self, screen):
        screen.blit(pygame.image.load(self.img).convert_alpha(), self.dest)


class Phrase(object):
    def __init__(self, text, on, x, y, colour, size):
        self.text = text
        self.on = on
        self.X = x
        self.Y = y
        self.colour = colour
        self.size = size

    def write(self, screen):
        my_font = pygame.font.Font("assets/PokemonGB-RAeo.ttf", self.size)
        label = my_font.render(self.text, 1, self.colour)
        text = screen.blit(label, (self.X, self.Y))
        return text


class Talk(Phrase):
    def __init__(self, text, on, y):
        super().__init__(text, on, 110, (y*20)+280, (255, 255, 255), 10)


    def write(self, screen):
        my_font = pygame.font.Font("assets/PokemonGB-RAeo.ttf", self.size)
        label1 = my_font.render(self.text[0], 1, self.colour)
        label2 = my_font.render(self.text[1], 1, self.colour)
        label3 = my_font.render(self.text[2], 1, self.colour)
        text = screen.blit(label1, (self.X, self.Y))
        text = screen.blit(label2, (self.X, self.Y+20))
        text = screen.blit(label3, (self.X, self.Y+40))
        return text

class Menu(object):
    def __init__(self, screen, size, x, y, opt1, menu_go):
        self.screen = screen
        self.x = x
        self.y = y
        self.size = size
        self.opt1 = opt1
        self.menu_go = menu_go

    def print_menu(self):
        # my_font = pygame.font.Font("assets/PokemonGB-RAeo.ttf", 10)
        # item1 = my_font.render(self.opt1, 1, (255, 255, 255))
        # item2 = my_font.render(self.opt2, 1, (255, 255, 255))
        # item3 = my_font.render(self.opt3, 1, (255, 255, 255))
        # item4 = my_font.render(self.opt4, 1, (255, 255, 255))
        # self.screen.blit(item1, (self.x, self.y))
        # self.screen.blit(item2, (205, 300))
        # self.screen.blit(item3, (205, 325))
        # self.screen.blit(item4, (205, 350))
        for x in self.size:
            my_font = pygame.font.Font("assets/PokemonGB-RAeo.ttf", 10)
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
        my_font = pygame.font.Font("assets/PokemonGB-RAeo.ttf", 10)
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

        # gd.menu["menu1"].menu_len():