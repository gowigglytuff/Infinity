import pygame
import copy
import random
from test.tiles import tiles_list_2d
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
                                          "assets/alien1_right.png"], 0, "down"))

    gd.add_character("Zirel", Zirel(4, 3, ["assets/alien2.png"], 0, "none", 0, "Zirel"))
    gd.add_character("IShine", Ishine(5, 6, ["assets/alien3.png"], 0, "none", 0, "IShine"))
    gd.add_character("Zoop", Zoop(3, 7, ["assets/alien4.png"], 0, "none", 0, "Zoop"))
    gd.add_character("Anton", Anton(0, 1, ["assets/alien5.png"], 0, "none", 0, "Anton"))
    gd.add_character("King", King(0, 6, ["assets/alien6.png"], 0, "none", 0, "King"))
    gd.add_character("Galaxar", Galaxar(3, 3, ["assets/alien7.png"], 0, "none", 0, "Galaxar"))
    gd.add_character("Seeder", Seeder(7, 7, ["assets/alien8.png"], 0, "none", 0, "Seeder"))
    gd.add_character("Thickky", Thickkaelious(7, 2, ["assets/alien9.png"], 0, "none", 0, "Thickky"))
    gd.add_character("Seedro", Seedro(4, 1, ["assets/alien10.png"], 0, "none", 0, "Seedro"))
    gd.add_character("Merkle", Merkle(6, 4, ["assets/alien11.png"], 0, "none", 0, "Merkle"))
    gd.add_character("Eveirg", Eveirg(3, 5, ["assets/alien12.png"], 0, "none", 0, "Eveirg"))
    gd.add_character("Japeto", Japeto(1, 4, ["assets/alien14.png"], 0, "none", 0, "Japeto"))
    gd.add_character("Emilius", Emilius(2, 7, ["assets/alien13b.png"], 0, "none", 0, "Emilius"))

    gd.add_bg("bg1", BG(0, 0, ["assets/BG1.png", "assets/BG2.png"]))

    gd.add_prop("desk_left", Prop(0, 2, ["assets/desk_left.png"]))
    gd.add_prop("desk_right", Prop(1, 2, ["assets/desk_right.png"]))

    gd.add_prop("bar_top", Prop(6, 6, ["assets/bar1.png"]))
    gd.add_prop("bar_bottom", Prop(6, 7, ["assets/bar2.png"]))

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
        for name, o in gd.characters.items():
            tiles_list_2d[int(o.x)][int(o.y)].full = name
        tiles_list_2d[gd.prop["bar_bottom"].x][gd.prop["bar_bottom"].y].full = "bar"
        tiles_list_2d[gd.prop["bar_top"].x][gd.prop["bar_top"].y].full = "full"
        tiles_list_2d[gd.prop["desk_right"].x][gd.prop["desk_right"].y].full = "full"
        tiles_list_2d[gd.prop["desk_left"].x][gd.prop["desk_left"].y].full = "desk"
        # for name, o in gd.prop.items():
        #     tiles_list_2d[int(o.x)][int(o.y)].full = "bar"
        #     print(name, o)
        for name in gd.characters:
            if gd.characters[name].points < 0:
                gd.characters[name].points = 0


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
            if gd.characters[dude].emote != "none":
                gd.characters[dude].print_name(gc.screen)
                gd.characters[dude].display(gc.screen, "happy")


        gd.menu["menu1"].print_menu()
        gd.cursor["cursor1"].print_cursor()

    def talking_draw():

        for name in gd.characters:
            if gd.characters[name].emote != "none":
                gd.characters[name].print_name(gc.screen)
                gd.characters[name].display(gc.screen, "happy")
                gd.characters[name].print_phrase(gc.screen, gd.characters[name].emote)

    def proposition_draw():
        for name in gd.characters:
            if gd.characters[name].emote != "none":
                gd.characters[name].print_name(gc.screen)
                if gd.characters[name].goal_met():
                    gd.characters[name].display(gc.screen, "horny")
                if not gd.characters[name].goal_met():
                    gd.characters[name].display(gc.screen, "mad")
                gd.characters[name].print_phrase(gc.screen, gd.characters[name].emote)

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

        for name in gd.characters:
            if gd.characters[name].emote == "good_gift":
                gd.characters[name].print_name(gc.screen)
                gd.characters[name].display(gc.screen, "thankful")
                gd.characters[name].print_phrase(gc.screen, gd.characters[name].emote)
                print(gd.characters[name].emote)
            if gd.characters[name].emote == "bad_gift":
                gd.characters[name].print_name(gc.screen)
                gd.characters[name].display(gc.screen, "sad")
                gd.characters[name].print_phrase(gc.screen, gd.characters[name].emote)

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
                            if tiles_list_2d[int(alien1.x)-1][int(alien1.y)].full == "none":
                                playing.state = "left"
                                animating = True

                    if event.key == pygame.K_RIGHT:
                        gd.player["alien1"].facing = "right"
                        alien1.set_image(3)
                        if not alien1.x >= 7:

                            if tiles_list_2d[int(alien1.x)+1][int(alien1.y)].full == "none":
                                playing.state = "right"
                                animating = True

                    if event.key == pygame.K_SPACE:
                        alien1.set_image(0)
                        gd.player["alien1"].facing = "down"

                    if event.key == pygame.K_UP:
                        alien1.set_image(1)
                        gd.player["alien1"].facing = "up"
                        if not alien1.y <= 1:
                            if tiles_list_2d[int(alien1.x)][int(alien1.y-1)].full == "none":
                                playing.state = "up"
                                animating = True

                    if event.key == pygame.K_DOWN:
                        alien1.set_image(0)
                        gd.player["alien1"].facing = "down"
                        if not alien1.y >= 7:
                            if tiles_list_2d[int(alien1.x)][int(alien1.y+1)].full == "none":
                                playing.state = "down"
                                animating = True

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
                                            gd.characters[facing_tile.interact()].print_phrase(gc.screen, "small_talk1")
                                            print(facing_tile.full)
                                            gd.characters[facing_tile.interact()].emote = "on"
                                            gc.game_state = gc.IN_MENU
                                elif facing_tile.full == "desk":
                                    gc.game_state = gc.ANTON
                                    print(gc.game_state)
                            elif facing_tile.full == "bar":
                                gc.game_state = gc.SEEDER

                    if event.key == pygame.K_1:
                        gc.game_state = gc.START_MENU
                    if event.key == pygame.K_2:
                        gd.item_list["inventory"].print_item_list()


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

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                # if keystroke is pressed check whether right or left
                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_RETURN:
                        # Make small talk with alien
                        if gd.cursor["cursor1"].get_cursor_position() == gd.menu["menu1"].y:
                            if gd.characters[facing_tile.interact()].points <= 9:
                                print(gd.characters[facing_tile.interact()].points)
                                gd.characters[facing_tile.interact()].emote = "small_talk" + \
                                    str(gd.characters[facing_tile.interact()].points)
                                gd.characters[facing_tile.interact()].points += 1
                                gc.game_state = gc.TALKING
                            elif gd.characters[facing_tile.interact()].points <= 10:
                                gd.characters[facing_tile.interact()].emote = "small_talk10"
                                gc.game_state = gc.TALKING

                        # Give a gift
                        if gd.cursor["cursor1"].get_cursor_position() == gd.menu["menu1"].y+25:
                            print("You gave a gift!")
                            gd.cursor["cursor1"].y = gd.menu["menu1"].y
                            gd.characters[facing_tile.interact()].emote = ["bad_gift"][0]
                            gc.game_state = gc.GIFT

                        # Make a proposition
                        if gd.cursor["cursor1"].get_cursor_position() == gd.menu["menu1"].y+50:
                            gd.cursor["cursor1"].y = gd.menu["menu1"].y
                            if not gd.characters[facing_tile.interact()].goal_met():
                                gd.characters[facing_tile.interact()].emote = ["mad"][0]
                                gc.game_state = gc.PROPOSITION
                            else:
                                gd.characters[facing_tile.interact()].emote = ["dtf"][0]
                                gc.game_state = gc.PROPOSITION

                        # Exit Menu
                        if gd.cursor["cursor1"].get_cursor_position() == gd.menu["menu1"].y+75:
                            gd.cursor["cursor1"].y = gd.menu["menu1"].y
                            for name in gd.characters:
                                gd.characters[name].emote = "none"
                            gc.game_state = gc.IN_GAME

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
                        if gd.characters[facing_tile.interact()].likes.count(gd.cursor["item_cursor"].get_item()) > 0:
                            gd.characters[facing_tile.interact()].points += 1
                            gd.characters[facing_tile.interact()].emote = "good_gift"
                            gc.game_state = gc.GIFT_RECEIVED
                        else:
                            gd.characters[facing_tile.interact()].points -= 1
                            gd.characters[facing_tile.interact()].emote = "bad_gift"
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
                        for name in gd.characters:
                            gd.characters[name].emote = "none"
                        gc.game_state = gc.IN_GAME

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

def kiss():
    pass



if __name__ == "__main__":
    main()