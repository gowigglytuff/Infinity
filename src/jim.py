import pygame
import copy
import random
from test.tiles import tiles_list_2d
from test.tiles import *
from test.spritesheet import Spritesheet
from test.gamestate import *
from test.dudes import *


gd = GameData()
gc = GameContoller(gd)

current_tile = "Galaxar"


def main():
    init_game()
    run_game_loop()
    print(tiles_list_2d[0][0])


def init_game():
    # initialize pygame
    pygame.init()

    pygame.display.set_caption('Infinity')

    gd.add_player("alien1", Player(6, 1, ["assets/alien1_front.png",
                                          "assets/alien1_back.png",
                                          "assets/alien1_left.png",
                                          "assets/alien1_right.png"], 0, "down", "None", "alien1", "player"))

    gd.add_character("Zirel", Zirel(4, 3, ["assets/alien2.png"], 0, False, 0, "Zirel", "character", "none"))
    gd.add_character("IShine", Ishine(5, 6, ["assets/alien3.png"], 0, False, 0, "IShine", "character", "none"))
    gd.add_character("Zoop", Zoop(3, 7, ["assets/alien4.png"], 0, False, 0, "Zoop", "character", "none"))
    gd.add_character("Anton", Anton(0, 1, ["assets/alien5.png"], 0, False, 0, "Anton", "character", "none"))
    gd.add_character("King", King(0, 6, ["assets/alien6.png"], 0, False, 0, "King", "character", "none"))
    gd.add_character("Galaxar", Galaxar(3, 3, ["assets/alien7.png"], 0, False, 0, "Galaxar", "character", "none"))
    gd.add_character("Seeder", Seeder(7, 7, ["assets/alien8.png"], 0, False, 0, "Seeder", "character", "none"))
    gd.add_character("Thickky", Thickkaelious(7, 2, ["assets/alien9.png"], 0, False, 0, "Thickky", "character", "none"))
    gd.add_character("Seedro", Seedro(4, 1, ["assets/alien10.png"], 0, False, 0, "Seedro", "character", "none"))
    gd.add_character("Merkle", Merkle(6, 4, ["assets/alien11.png"], 0, False, 0, "Merkle", "character", "none"))
    gd.add_character("Eveirg", Eveirg(3, 5, ["assets/alien12.png"], 0, False, 0, "Eveirg", "character", "none"))
    gd.add_character("Japeto", Japeto(1, 4, ["assets/alien14.png"], 0, False, 0, "Japeto", "character", "none"))
    gd.add_character("Emilius", Emilius(2, 7, ["assets/alien13b.png"], 0, False, 0, "Emilius", "character", "none"))

    gd.add_bg("bg1", BG(0, 0, ["assets/BG1.png", "assets/BG2.png"]))

    gd.add_prop("desk_left", Prop(0, 2, ["assets/desk_left.png"], "desk_left", "prop"))
    gd.add_prop("desk_right", Prop(1, 2, ["assets/desk_right.png"], "desk_right", "prop"))

    gd.add_prop("bar_top", Prop(6, 6, ["assets/bar1.png"], "bar_top", "prop"))
    gd.add_prop("bar_bottom", Prop(6, 7, ["assets/bar2.png"], "bar_bottom", "prop"))

    gd.add_menu("menu1", Menu(gc.screen, [0, 1, 2, 3], 230, 275, ["Talk", "Give Gift", "Proposition", "Exit"], False))
    gd.add_menu("start_menu", Menu(gc.screen, [0, 1, 2, 3, 4, 5], 280, 100, ["Items", "Setings", "Records", "Phone",
                                                                             "Save", "Exit"], False))

    gd.add_cursor("cursor1", Cursor(gc.screen, gd.menu["menu1"], False, 1))
    gd.add_cursor("start_cursor", Cursor(gc.screen, gd.menu["start_menu"], False, 1))


    gd.add_item("Cup", Item("Cup", 0))
    gd.add_item("Water", Item("Water", 0))
    gd.add_item("Soda", Item("Soda", 0))
    gd.add_item("Butter", Item("Butter", 1))
    gd.add_item("Gum", Item("Gum", 2))
    gd.add_item("Sp. Coke", Item("Sp. Coke", 0))
    gd.add_item("Muffin", Item("Muffin", 6))
    gd.add_item("Cookie", Item("Cookie", 0))
    gd.add_item("Cheese", Item("Cheese", 0))
    gd.add_item("Donut", Item("Donut", 1))
    gd.add_item("Sticker", Item("Sticker", 1))

    gd.add_item_list("inventory", ItemList(gc.screen, 1, True, [gd.item][0], gd.get_all_items()))
    gd.add_cursor("item_cursor", ItemCursor(gc.screen, gd.item_list["inventory"], False, 1))

    gd.add_menu("character_menu", Menu(gc.screen, [0, 1, 2, 3], 205, 275, ["Talk", "Give Gift",
                                                                           "Proposition", "Exit"], False))

    character_names = []
    for x in gd.characters:
        character_names.append(x)

    gd.add_menu("info_menu", Menu(gc.screen, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 280, 50, character_names,
                                  False))
    gd.add_cursor("info_cursor", Cursor(gc.screen, gd.menu["info_menu"], False, 1))

    gd.add_menu("request_menu", Menu(gc.screen, [0, 1, 2, 3, 4], 275, 50, ["A.A. Bop", "A.A Jam",
                                                                        "A.A. Banger", "DJ A.A.", "A.A. Ska"], False))
    gd.add_cursor("request_cursor", Cursor(gc.screen, gd.menu["request_menu"], False, 1))

def run_game_loop():

    animating = False

    def update_files():
        drawables_list = gd.get_all_drawables()

        # figure out what is filling each tile
        for tile in tiles_list:
            tile.reset_object_filling()
        for tile in tiles_list:
            tile.get_object_filling(drawables_list)

        for name in gd.characters:
            if gd.characters[name].points < 0:
                gd.characters[name].points = 0
            if gd.characters[name].points > 10:
                gd.characters[name].points = 10


    def big_draw():
        # fix drawing hierarchy

        BG.draw(gd.BG["bg1"], gc.screen)

        alien1 = gd.player["alien1"]

        drawables_list = gd.get_all_drawables()
        drawables_list = sorted(drawables_list, key=lambda x: (x.y, x.printing_priority))
        for drawable in drawables_list:
            drawable.draw(gc.screen)

    def menu_draw():

        for dude in gd.characters:
            if gd.characters[dude].emote == True:
                gd.characters[dude].print_name(gc.screen)
                gd.characters[dude].display(gc.screen, "happy")

        gd.menu["menu1"].print_menu()
        gd.cursor["cursor1"].print_cursor()

    def talking_draw():
        for name in gd.characters:
            if gd.characters[name].emote == True:
                gd.characters[name].print_name(gc.screen)
                gd.characters[name].display(gc.screen, "happy")
                gd.characters[name].print_phrase(gc.screen, gd.characters[name].feeling)

    def sass_draw():
        for name in gd.characters:
            if gd.characters[name].emote == "follow":
                gd.characters[name].print_name(gc.screen)
                gd.characters[name].display(gc.screen, "happy")
                gd.characters[name].print_phrase(gc.screen, gd.characters[name].emote)

    def proposition_draw():
        for name in gd.characters:
            if gd.characters[name].emote == True:
                gd.characters[name].print_name(gc.screen)
                if gd.characters[name].goal_met():
                    gd.characters[name].display(gc.screen, "horny")
                if not gd.characters[name].goal_met():
                    gd.characters[name].display(gc.screen, "mad")
                gd.characters[name].print_phrase(gc.screen, gd.characters[name].feeling)

    def gift_draw():
        gd.item_list["inventory"].print_item_list()
        gd.cursor["item_cursor"].print_cursor()
        for name in gd.characters:
            if gd.characters[name].emote != "none":
                gd.characters[name].print_name(gc.screen)
                gd.characters[name].display(gc.screen, "happy")

    def start_draw():
        gd.menu["start_menu"].print_menu()
        gd.cursor["start_cursor"].print_cursor()

    def inventory_draw():
        gd.item_list["inventory"].print_item_list()
        gd.cursor["item_cursor"].print_cursor()

    def gift_received_draw():

        if gd.characters[facing_tile.interact()].feeling == "good_gift":
            for name in gd.characters:
                if gd.characters[name].emote == True:
                    gd.characters[name].print_name(gc.screen)
                    gd.characters[name].display(gc.screen, "thankful")
                    gd.characters[name].print_phrase(gc.screen, "good_gift")
                    print(gd.characters[name].emote)
        elif gd.characters[facing_tile.interact()].feeling == "bad_gift":
            for name in gd.characters:
                if gd.characters[name].emote == True:
                    gd.characters[name].print_name(gc.screen)
                    gd.characters[name].display(gc.screen, "sad")
                    gd.characters[name].print_phrase(gc.screen, "bad_gift")

    def seeder_draw():
        gd.characters["Seeder"].print_name(gc.screen)
        gd.characters["Seeder"].display(gc.screen, "happy")
        gd.characters["Seeder"].print_phrase(gc.screen, "information")
        gd.menu["info_menu"].print_menu()
        gd.cursor["info_cursor"].print_cursor()
        # gd.characters["Seeder"].print_phrase(gc.screen, gd.characters[Seeder].emote)

    def information_draw():
        gd.characters["Seeder"].print_name(gc.screen)
        gd.characters["Seeder"].display(gc.screen, "happy")
        if gd.characters["Seeder"].emote != "none":
            gd.characters["Seeder"].print_phrase(gc.screen, str(gd.characters["Seeder"].emote))
        print(gd.characters["Seeder"].emote)

    def anton_draw():
        gd.characters["Anton"].print_name(gc.screen)
        gd.characters["Anton"].display(gc.screen, "happy")
        gd.characters["Anton"].print_phrase(gc.screen, "request")
        gd.menu["request_menu"].print_menu()
        gd.cursor["request_cursor"].print_cursor()
        # gd.characters["Seeder"].print_phrase(gc.screen, gd.characters[Seeder].emote)

    def request_draw():
        gd.characters["Anton"].print_name(gc.screen)
        gd.characters["Anton"].display(gc.screen, "happy")
        gd.characters["Anton"].print_phrase(gc.screen, "result")

        # gd.characters["Seeder"].print_phrase(gc.screen, gd.characters[Seeder].emote)

    def dance():
        if playing.tock == 10:
            gd.characters["Zirel"].offset += 3.2
            gd.characters["IShine"].offset += 3.2
            gd.characters["Zoop"].offset += 3.2
            gd.characters["Anton"].offset -= 3.2
            gd.characters["King"].offset += 3.2
            gd.characters["Galaxar"].offset -= 3.2
            gd.characters["Seeder"].offset -= 3.2
            gd.characters["Thickky"].offset -= 3.2
            gd.characters["Seedro"].offset -= 3.2
            gd.characters["Merkle"].offset += 3.2
            gd.characters["Eveirg"].offset -= 3.2
            gd.characters["Emilius"].offset -= 3.2
            gd.characters["Japeto"].offset += 3.2

            gd.BG["bg1"].set_image(1)
        if playing.tock == 16:
            pass

        if playing.tock == 20:
            gd.characters["Zirel"].offset -= 3.2
            gd.characters["IShine"].offset -= 3.2
            gd.characters["Zoop"].offset -= 3.2
            gd.characters["Anton"].offset += 3.2
            gd.characters["King"].offset -= 3.2
            gd.characters["Galaxar"].offset += 3.2
            gd.characters["Seeder"].offset += 3.2
            gd.characters["Thickky"].offset += 3.2
            gd.characters["Seedro"].offset += 3.2
            gd.characters["Merkle"].offset -= 3.2
            gd.characters["Eveirg"].offset += 3.2
            gd.characters["Emilius"].offset += 3.2
            gd.characters["Japeto"].offset -= 3.2

            gd.BG["bg1"].set_image(0)
            playing.tock = 0

        playing.tock += 1


    alien1 = gd.player["alien1"]

    # game loop
    running = True

    while running:
        if gc.game_state == gc.IN_GAME:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                # if keystroke is pressed check whether right or left
                if event.type == pygame.KEYDOWN:

                    for name in gd.characters:
                        gd.characters[name].emote = "none"

                    if event.key == pygame.K_LEFT:
                        gd.player["alien1"].facing = "left"
                        alien1.set_image(2)
                        if not alien1.x <= 0:
                            if not tiles_list_2d[int(alien1.x)-1][int(alien1.y)].full:
                                playing.state = "left"
                                animating = True

                    if event.key == pygame.K_RIGHT:
                        gd.player["alien1"].facing = "right"
                        alien1.set_image(3)
                        if not alien1.x >= 7:
                            if not tiles_list_2d[int(alien1.x)+1][int(alien1.y)].full:
                                playing.state = "right"
                                animating = True

                    if event.key == pygame.K_SPACE:
                        alien1.set_image(0)
                        gd.player["alien1"].facing = "down"

                    if event.key == pygame.K_UP:
                        alien1.set_image(1)
                        gd.player["alien1"].facing = "up"
                        if not alien1.y <= 1:
                            if not tiles_list_2d[int(alien1.x)][int(alien1.y-1)].full:
                                playing.state = "up"
                                animating = True

                    if event.key == pygame.K_DOWN:
                        alien1.set_image(0)
                        gd.player["alien1"].facing = "down"
                        if not alien1.y >= 7:
                            if not tiles_list_2d[int(alien1.x)][int(alien1.y+1)].full:
                                playing.state = "down"
                                animating = True

                    if event.key == pygame.K_RETURN:
                        facing_tile_y = 0
                        facing_tile_x = 0
                        if gd.player["alien1"].facing == "up":
                            facing_tile_y = int(alien1.y - 1)
                            facing_tile_x = int(alien1.x)

                        elif gd.player["alien1"].facing == "down":
                            facing_tile_y = int(alien1.y + 1)
                            facing_tile_x = int(alien1.x)

                        elif gd.player["alien1"].facing == "left":
                            facing_tile_y = int(alien1.y)
                            facing_tile_x = int(alien1.x - 1)

                        elif gd.player["alien1"].facing == "right":
                            facing_tile_y = int(alien1.y)
                            facing_tile_x = int(alien1.x + 1)

                        facing_tile = tiles_list_2d[facing_tile_x][facing_tile_y]

                        if facing_tile.full:
                            if facing_tile.filling_type == "character":
                                print(facing_tile.full)
                                print(facing_tile.object_filling)
                                if facing_tile.object_filling == gd.characters[facing_tile.interact()].name:
                                    gc.game_state = gc.IN_MENU
                            elif facing_tile.filling_type == "prop":
                                if facing_tile.object_filling == "desk_left":
                                    gc.game_state = gc.ANTON
                                elif facing_tile.full == "bar_bottom":
                                    gc.game_state = gc.SEEDER

                    if event.key == pygame.K_1:
                        gc.game_state = gc.START_MENU
                    if event.key == pygame.K_2:
                        print(gd.characters["Zirel"].phrases["mad"])


                if event.type == pygame.KEYUP:
                    pass


            while animating:

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False

                if playing.state == "left":
                    if playing.tick == 0:
                        alien1.x -= .25
                    if playing.tick == 1:
                        alien1.x -= .25
                    if playing.tick == 2:
                        alien1.x -= .25
                    if playing.tick == 3:
                        alien1.x -= .25

                if playing.state == "right":
                    if playing.tick == 0:
                        alien1.x += .25
                    if playing.tick == 1:
                        alien1.x += .25
                    if playing.tick == 2:
                        alien1.x += .25
                    if playing.tick == 3:
                        alien1.x += .25

                if playing.state == "down":
                    if playing.tick == 0:
                        alien1.y += .25
                    if playing.tick == 1:
                        alien1.y += .25
                    if playing.tick == 2:
                        alien1.y += .25
                    if playing.tick == 3:
                        alien1.y += .25

                if playing.state == "up":
                    if playing.tick == 0:
                        alien1.y -= .25
                    if playing.tick == 1:
                        alien1.y -= .25
                    if playing.tick == 2:
                        alien1.y -= .25
                    if playing.tick == 3:
                        alien1.y -= .25

                if playing.tick == 4:
                    playing.tick = 0
                    playing.state = "none"
                    animating = False

                if animating:
                    playing.tick += 1

                dance()
                big_draw()
                pygame.display.update()
                gc.tick()


            update_files()
            dance()
            big_draw()
            pygame.display.update()
            gc.tick()

        if gc.game_state == gc.IN_MENU:

            gd.characters[facing_tile.interact()].emote = True

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                # if keystroke is pressed check whether right or left
                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_RETURN:

                        # Make small talk with alien
                        if gd.cursor["cursor1"].get_cursor_position() == gd.menu["menu1"].y:
                            gd.characters[facing_tile.interact()].emote = True

                            if gd.characters[facing_tile.interact()].points <= 9:
                                gd.characters[facing_tile.interact()].feeling = "small_talk" + \
                                    str(gd.characters[facing_tile.interact()].points)

                            elif gd.characters[facing_tile.interact()].points <= 10:
                                gd.characters[facing_tile.interact()].feeling = "small_talk10"

                            gd.characters[facing_tile.interact()].points += 1
                            gc.game_state = gc.TALKING

                        # Give a gift
                        if gd.cursor["cursor1"].get_cursor_position() == gd.menu["menu1"].y+25:
                            gc.game_state = gc.GIFT

                        # Make a proposition
                        if gd.cursor["cursor1"].get_cursor_position() == gd.menu["menu1"].y+50:
                            gd.characters[facing_tile.interact()].emote = True

                            if not gd.characters[facing_tile.interact()].goal_met():
                                gd.characters[facing_tile.interact()].feeling = ["mad"][0]

                            else:
                                gd.characters[facing_tile.interact()].feeling = ["dtf"][0]

                            gc.game_state = gc.PROPOSITION

                        # Exit Menu
                        if gd.cursor["cursor1"].get_cursor_position() == gd.menu["menu1"].y+75:
                            for name in gd.characters:
                                gd.characters[name].emote = "none"
                            gc.game_state = gc.IN_GAME

                        # reset cursor
                        gd.cursor["cursor1"].cursor_reset()

                    # move menu cursor down
                    if event.key == pygame.K_DOWN:
                        gd.cursor["cursor1"].cursor_down()

                    # move menu cursor up
                    if event.key == pygame.K_UP:
                        gd.cursor["cursor1"].cursor_up()

            update_files()
            dance()
            big_draw()
            menu_draw()
            pygame.display.update()
            gc.tick()

        if gc.game_state == gc.TALKING:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_RETURN:
                        for name in gd.characters:
                            gd.characters[name].emote = "none"
                        gc.game_state = gc.IN_GAME

            update_files()
            dance()
            big_draw()
            talking_draw()
            pygame.display.update()
            gc.tick()

        if gc.game_state == gc.GIFT:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_RETURN:
                        gd.item[gd.cursor["item_cursor"].get_item()].quantity -= 1
                        gd.characters[facing_tile.interact()].emote = True
                        if gd.characters[facing_tile.interact()].likes.count(gd.cursor["item_cursor"].get_item()) > 0:
                            gd.characters[facing_tile.interact()].points += 1
                            gd.characters[facing_tile.interact()].feeling = "good_gift"
                        else:
                            gd.characters[facing_tile.interact()].points -= 1
                            gd.characters[facing_tile.interact()].feeling = "bad_gift"
                        gd.cursor["item_cursor"].cursor_reset()
                        gc.game_state = gc.GIFT_RECEIVED


                    if event.key == pygame.K_DOWN:
                        gd.cursor["item_cursor"].cursor_down()

                    if event.key == pygame.K_UP:
                        gd.cursor["item_cursor"].cursor_up()


            update_files()
            dance()
            big_draw()
            gift_draw()
            pygame.display.update()
            gc.tick()

        if gc.game_state == gc.GIFT_RECEIVED:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_RETURN:
                        for name in gd.characters:
                            gd.characters[name].emote = "none"
                        gc.game_state = gc.IN_GAME

            update_files()
            dance()
            big_draw()
            gift_received_draw()
            pygame.display.update()
            gc.tick()

        if gc.game_state == gc.PROPOSITION:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_RETURN:
                        if gd.characters[facing_tile.interact()].feeling == ["mad"][0]:
                            for name in gd.characters:
                                gd.characters[name].emote = "none"
                            gc.game_state = gc.IN_GAME

                        if gd.characters[facing_tile.interact()].feeling == ["dtf"][0]:
                            for name in gd.characters:
                                gd.characters[name].emote = "none"
                            gc.game_state = gc.IN_GAME
                            # gd.player["alien1"].follow = gd.characters[facing_tile.interact()].name
                            # gc.game_state = gc.FOLLOW
            update_files()
            dance()
            big_draw()
            proposition_draw()
            pygame.display.update()
            gc.tick()

        if gc.game_state == gc.START_MENU:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_RETURN:
                        if gd.cursor["start_cursor"].get_cursor_position() == gd.menu["start_menu"].y:
                            gc.game_state = gc.INVENTORY
                        else:
                            for name in gd.characters:
                                gd.characters[name].emote = "none"
                            gc.game_state = gc.IN_GAME

                    if event.key == pygame.K_DOWN:
                        gd.cursor["start_cursor"].cursor_down()


                    if event.key == pygame.K_UP:
                        gd.cursor["start_cursor"].cursor_up()


            update_files()
            dance()
            big_draw()
            start_draw()
            pygame.display.update()
            gc.tick()

        if gc.game_state == gc.INVENTORY:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_RETURN:
                        print(gd.cursor["item_cursor"].get_item())
                        for name in gd.characters:
                            gd.characters[name].emote = "none"
                        gc.game_state = gc.IN_GAME

                    if event.key == pygame.K_DOWN:
                        gd.cursor["item_cursor"].cursor_down()
                    if event.key == pygame.K_UP:
                        gd.cursor["item_cursor"].cursor_up()

            update_files()
            dance()
            big_draw()
            inventory_draw()
            pygame.display.update()
            gc.tick()

        if gc.game_state == gc.SEEDER:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_RETURN:
                        print(gd.cursor["info_cursor"].get_item())
                        gd.characters["Seeder"].emote = gd.cursor["info_cursor"].get_item()
                        gc.game_state = gc.INFORMATION

                    if event.key == pygame.K_DOWN:
                        gd.cursor["info_cursor"].cursor_down()
                    if event.key == pygame.K_UP:
                        gd.cursor["info_cursor"].cursor_up()

            update_files()
            dance()
            big_draw()
            seeder_draw()
            pygame.display.update()
            gc.tick()

        if gc.game_state == gc.INFORMATION:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_RETURN:
                        for name in gd.characters:
                            gd.characters[name].emote = "none"
                        gc.game_state = gc.IN_GAME

            update_files()
            dance()
            big_draw()
            information_draw()
            pygame.display.update()
            gc.tick()

        if gc.game_state == gc.ANTON:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_RETURN:
                        print(gd.cursor["request_cursor"].get_item())
                        gc.game_state = gc.REQUEST

                    if event.key == pygame.K_DOWN:
                        gd.cursor["request_cursor"].cursor_down()
                    if event.key == pygame.K_UP:
                        gd.cursor["request_cursor"].cursor_up()

            update_files()
            dance()
            big_draw()
            anton_draw()
            pygame.display.update()
            gc.tick()

        if gc.game_state == gc.REQUEST:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_RETURN:
                        for name in gd.characters:
                            gd.characters[name].emote = "none"
                        gc.game_state = gc.IN_GAME

            update_files()
            dance()
            big_draw()
            request_draw()
            pygame.display.update()
            gc.tick()

        if gc.game_state == gc.FOLLOW:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                # if keystroke is pressed check whether right or left
                if event.type == pygame.KEYDOWN:

                    for name in gd.characters:
                        gd.characters[name].emote = "none"

                    if event.key == pygame.K_LEFT:
                        for x in gd.characters:
                            if gd.characters[x].name == gd.player["alien1"].follow:
                                gd.player["alien1"].facing = "left"
                                alien1.set_image(2)
                                if not alien1.x <= 0:
                                    if tiles_list_2d[int(alien1.x) - 1][int(alien1.y)].full == gd.characters[x].name:
                                        playing.state = "left"
                                        animating = True
                                        gd.characters[x].x = gd.player["alien1"].x
                                        gd.characters[x].y = gd.player["alien1"].y
                                    elif tiles_list_2d[int(alien1.x) - 1][int(alien1.y)].full == "none":
                                        playing.state = "left"
                                        animating = True
                                        gd.characters[x].x = gd.player["alien1"].x
                                        gd.characters[x].y = gd.player["alien1"].y

                    if event.key == pygame.K_RIGHT:
                        for x in gd.characters:
                            if gd.characters[x].name == gd.player["alien1"].follow:
                                gd.player["alien1"].facing = "right"
                                alien1.set_image(3)
                                if not alien1.x >= 7:
                                    if tiles_list_2d[int(alien1.x) + 1][int(alien1.y)].full == gd.characters[x].name:
                                        playing.state = "right"
                                        animating = True
                                        gd.characters[x].x = gd.player["alien1"].x
                                        gd.characters[x].y = gd.player["alien1"].y
                                    if tiles_list_2d[int(alien1.x) + 1][int(alien1.y)].full == "none":
                                        playing.state = "right"
                                        animating = True
                                        gd.characters[x].x = gd.player["alien1"].x
                                        gd.characters[x].y = gd.player["alien1"].y

                    if event.key == pygame.K_SPACE:
                        alien1.set_image(0)
                        gd.player["alien1"].facing = "down"

                    if event.key == pygame.K_UP:
                        for x in gd.characters:
                            if gd.characters[x].name == gd.player["alien1"].follow:
                                alien1.set_image(1)
                                gd.player["alien1"].facing = "up"
                                if not alien1.y <= 1:
                                    if tiles_list_2d[int(alien1.x)][int(alien1.y - 1)].full == gd.characters[x].name:
                                        playing.state = "up"
                                        animating = True
                                        gd.characters[x].x = gd.player["alien1"].x
                                        gd.characters[x].y = gd.player["alien1"].y
                                    if tiles_list_2d[int(alien1.x)][int(alien1.y - 1)].full == "none":
                                        playing.state = "up"
                                        animating = True
                                        gd.characters[x].x = gd.player["alien1"].x
                                        gd.characters[x].y = gd.player["alien1"].y

                    if event.key == pygame.K_DOWN:
                        for x in gd.characters:
                            if gd.characters[x].name == gd.player["alien1"].follow:
                                alien1.set_image(0)
                                gd.player["alien1"].facing = "down"
                                if not alien1.y >= 7:
                                    if tiles_list_2d[int(alien1.x)][int(alien1.y + 1)].full == gd.characters[x].name:
                                        playing.state = "down"
                                        animating = True
                                        gd.characters[x].x = gd.player["alien1"].x
                                        gd.characters[x].y = gd.player["alien1"].y
                                    if tiles_list_2d[int(alien1.x)][int(alien1.y + 1)].full == "none":
                                        playing.state = "down"
                                        animating = True
                                        gd.characters[x].x = gd.player["alien1"].x
                                        gd.characters[x].y = gd.player["alien1"].y


                    if event.key == pygame.K_RETURN:
                        if gd.player["alien1"].facing == "up":
                            facing_tile_y = int(alien1.y - 1)
                            facing_tile_x = int(alien1.x)

                        elif gd.player["alien1"].facing == "down":
                            facing_tile_y = int(alien1.y + 1)
                            facing_tile_x = int(alien1.x)

                        elif gd.player["alien1"].facing == "left":
                            facing_tile_y = int(alien1.y)
                            facing_tile_x = int(alien1.x - 1)

                        elif gd.player["alien1"].facing == "right":
                            facing_tile_y = int(alien1.y)
                            facing_tile_x = int(alien1.x + 1)

                        facing_tile = tiles_list_2d[facing_tile_x][facing_tile_y]
                        print(facing_tile.full)
                        if facing_tile.full != "none":
                            if facing_tile.full != "bar":
                                if facing_tile.full != "desk":
                                    if facing_tile.full != "full":
                                        if facing_tile.full == gd.characters[facing_tile.interact()].name:
                                            gd.characters[facing_tile.interact()].emote = "follow"
                                            gc.game_state = gc.SASS

                if event.type == pygame.KEYUP:
                    pass


            while animating:

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False

                if playing.state == "left":
                    if playing.tick == 0:
                        alien1.x -= .25
                    if playing.tick == 1:
                        alien1.x -= .25
                    if playing.tick == 2:
                        alien1.x -= .25
                    if playing.tick == 3:
                        alien1.x -= .25

                if playing.state == "right":
                    if playing.tick == 0:
                        alien1.x += .25
                    if playing.tick == 1:
                        alien1.x += .25
                    if playing.tick == 2:
                        alien1.x += .25
                    if playing.tick == 3:
                        alien1.x += .25

                if playing.state == "down":
                    if playing.tick == 0:
                        alien1.y += .25
                    if playing.tick == 1:
                        alien1.y += .25
                    if playing.tick == 2:
                        alien1.y += .25
                    if playing.tick == 3:
                        alien1.y += .25

                if playing.state == "up":
                    if playing.tick == 0:
                        alien1.y -= .25
                    if playing.tick == 1:
                        alien1.y -= .25
                    if playing.tick == 2:
                        alien1.y -= .25
                    if playing.tick == 3:
                        alien1.y -= .25

                if playing.tick == 4:
                    playing.tick = 0
                    playing.state = "none"
                    animating = False

                if animating:
                    playing.tick += 1

                dance()
                big_draw()
                pygame.display.update()
                gc.tick()


            update_files()
            dance()
            big_draw()
            pygame.display.update()
            gc.tick()

        if gc.game_state == gc.SASS:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_RETURN:
                        for name in gd.characters:
                            gd.characters[name].emote = "none"
                        gc.game_state = gc.FOLLOW

            update_files()
            dance()
            big_draw()
            sass_draw()
            pygame.display.update()
            gc.tick()

def kiss():
    pass



if __name__ == "__main__":
    main()