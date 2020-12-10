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

    gd.add_player("alien1", Player(2, 2, ["assets/alien1_front.png",
                                          "assets/alien1_back.png",
                                          "assets/alien1_left.png",
                                          "assets/alien1_right.png"], 0, "down"))

    gd.add_character("Zirel", Zirel(4, 3, ["assets/alien2.png"], "none", 0, "Zirel"))
    gd.add_character("IShine", Ishine(5, 6, ["assets/alien3.png"], "none", 0, "IShine"))
    gd.add_character("Zoop", Zoop(3, 7, ["assets/alien4.png"], "none", 0, "Zoop"))
    gd.add_character("Anton", Anton(0, 1, ["assets/alien5.png"], "none", 0, "Anton"))
    gd.add_character("King", King(0, 6, ["assets/alien6.png"], "none", 0, "King"))
    gd.add_character("Galaxar", Galaxar(3, 3, ["assets/alien7.png"], "none", 0, "Galaxar"))
    gd.add_character("Seeder", Seeder(7, 7, ["assets/alien8.png"], "none", 0, "Seeder"))
    gd.add_character("Thickkaelious", Thickkaelious(7, 2, ["assets/alien9.png"], "none", 0, "Thickkaelious"))
    gd.add_character("Seedro", Seedro(4, 1, ["assets/alien10.png"], "none", 0, "Seedro"))
    gd.add_character("Merkle", Merkle(6, 4, ["assets/alien11.png"], "none", 0, "Merkle"))
    gd.add_character("Eveirg", Eveirg(3, 5, ["assets/alien12.png"], "none", 0, "Eveirg"))
    gd.add_character("Japeto", Japeto(1, 4, ["assets/alien14.png"], "none", 0, "Japeto"))
    gd.add_character("Emilius", Emilius(2, 7, ["assets/alien13b.png"], "none", 0, "Emilius"))

    gd.add_bg("bg1", BG(0, 0, ["assets/BG1.png", "assets/BG2.png"]))

    gd.add_prop("desk_left", Prop(0, 2, ["assets/desk_left.png"]))
    gd.add_prop("desk_right", Prop(1, 2, ["assets/desk_right.png"]))

    gd.add_prop("bar_top", Prop(6, 6, ["assets/bar1.png"]))
    gd.add_prop("bar_bottom", Prop(6, 7, ["assets/bar2.png"]))

    gd.add_menu("menu1", Menu(gc.screen, [0, 1, 2, 3], 205, 275, ["Talk", "Give Gift", "Proposition", "Exit"], False))
    gd.add_menu("start_menu", Menu(gc.screen, [0, 1, 2, 3, 4, 5], 290, 100, ["Items", "Setings", "Records", "Phone", "Save", "Exit"], False))

    gd.add_cursor("cursor1", Cursor(gc.screen, gd.menu["menu1"], False, 1))
    gd.add_cursor("start_cursor", Cursor(gc.screen, gd.menu["start_menu"], False, 1))

def run_game_loop():

    animating = False
    menu_state = "talking"

    def update_files():
        for name, o in gd.characters.items():
            tiles_list_2d[int(o.x)][int(o.y)].full = name
        for name, o in gd.prop.items():
            tiles_list_2d[int(o.x)][int(o.y)].full = "full"

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

    def start_draw():
        gd.menu["start_menu"].print_menu()
        gd.cursor["start_cursor"].print_cursor()

    def dance():
        if playing.tock == 10:
            gd.characters["Zirel"].offset += 3.2
            gd.characters["IShine"].offset += 3.2
            gd.characters["Zoop"].offset += 3.2
            gd.characters["Anton"].offset -= 3.2
            gd.characters["King"].offset += 3.2
            gd.characters["Galaxar"].offset -= 3.2
            gd.characters["Seeder"].offset -= 3.2
            gd.characters["Thickkaelious"].offset -= 3.2
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
            gd.characters["Thickkaelious"].offset += 3.2
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
    times = 0

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

                        if facing_tile.full != "none":
                            if facing_tile.full != "full":
                                # gd.characters[facing_tile.interact()].print_phrase(gc.screen, "small_talk1")
                                print(facing_tile.interact())
                                gd.characters[facing_tile.interact()].emote = random.choice(["small_talk1",
                                                                                        "small_talk2",
                                                                                        "small_talk3"])
                                gc.game_state = gc.IN_MENU

                            else:
                                print("full")
                        elif facing_tile.full == "none":
                            print("hi")
                    if event.key == pygame.K_1:
                        gc.game_state = gc.START_MENU

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
                        if gd.cursor["cursor1"].get_cursor_position() == gd.menu["menu1"].y:
                            gc.game_state = gc.TALKING

                        if gd.cursor["cursor1"].get_cursor_position() == gd.menu["menu1"].y+25:
                            print("You gave a gift!")
                            gd.cursor["cursor1"].y = gd.menu["menu1"].y
                            for name in gd.characters:
                                gd.characters[name].emote = "none"
                            gc.game_state = gc.IN_GAME

                        if gd.cursor["cursor1"].get_cursor_position() == gd.menu["menu1"].y+50:
                            gd.cursor["cursor1"].y = gd.menu["menu1"].y
                            print("They slap you in the face!")
                            for name in gd.characters:
                                gd.characters[name].emote = "none"
                            gc.game_state = gc.IN_GAME

                        if gd.cursor["cursor1"].get_cursor_position() == gd.menu["menu1"].y+75:
                            gd.cursor["cursor1"].y = gd.menu["menu1"].y
                            for name in gd.characters:
                                gd.characters[name].emote = "none"
                            gc.game_state = gc.IN_GAME

                    if event.key == pygame.K_SPACE:
                        gd.cursor["cursor1"].y = gd.menu["menu1"].y
                        for name in gd.characters:
                            gd.characters[name].emote = "none"
                        gc.game_state = gc.IN_GAME

                    if event.key == pygame.K_DOWN:
                        gd.cursor["cursor1"].cursor_down()


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
        if gc.game_state == gc.START_MENU:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_RETURN:
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
def kiss():
    pass



if __name__ == "__main__":
    main()