import pygame
from test.gamestate import GameContoller
from test.gamestate import GameData
from test.spritesheet import Spritesheet
from test.gamestate import Character

gd = GameData()
gc = GameContoller(gd)

class Seeder(Character):
    def __init__(self, x, y, img_file_name_list, points, emote, offset, name, classification, feeling,  origin_x, origin_y, on_stage, location):
        super().__init__(x, y, img_file_name_list, points, emote, offset, name, classification, feeling, origin_x, origin_y, on_stage, location)
        self.offset = offset
        self.phrase_counter = 0
        self.phrases = {
            "dtf": ["Well I guess,", "I should probably do a", "bathroom check anyway."],
            "sad": ["Well now I've", "gone and made", "myself sad."],
            "mad": ["I'm sorry, but that", "makes me a little", "uncomfortable."],
            "small_talk0": ["I love this job!", "It gives me the opportunity", "to meet lots of cool folks!"],
            "small_talk1": ["You're probably not supposed", "to be back here, just make ", "sure, my boss doesn't see!"],
            "small_talk2": ["I bartend nights to get", "by while I work on my career", "as a singer!"],
            "small_talk3": ["", "", ""],
            "small_talk4": ["", "", ""],
            "small_talk5": ["", "", ""],
            "small_talk6": ["", "", ""],
            "small_talk7": ["", "", ""],
            "small_talk8": ["", "", ""],
            "small_talk9": ["", "", ""],
            "small_talk10": ["", "", ""],
            "good_gift": ["Oh my goodness!", "This is the best tip", "I've ever received!"],
            "bad_gift": ["Uh, I can't accept something", "like this from a customer.", "Thanks anyway."],
            "information": ["who would you", "like to hear", "about?"],
            "Zirel": ["", "", ""],
            "IShine": ["", "", ""],
            "Zoop": ["", "", ""],
            "Anton": ["", "", ""],
            "Newman": ["I speek a lil Fongalese,", " I think @$@) @)$  @)($@_@", " means muffin!"],
            "Galaxar": ["", "", ""],
            "Seeder": ["", "", ""],
            "Thickky": ["", "", ""],
            "Seedro": ["He's my cousin,", "really sweet dude!", ""],
            "Merkle": ["", "", ""],
            "Eveirg": ["", "", ""],
            "Japeto": ["", "", ""],
            "Emilius": ["", "", ""],
            "follow": ["OooooOOooooOOoO, ", "you kids have fun!", ""]}
        self.emotions = {"happy": ["assets/seeder_happy.png"],
                         "mad": ["assets/mad/seedro_mad.png"],
                         "sad": ["assets/sad/" + "seedro" + "_sad.png"],
                         "horny": ["assets/horny/" + "seedro" + "_horny.png"],
                         "thankful": ["assets/thankful/" + "seedro" + "_thankful.png"]}
        self.current_likes = [["Cookie"], ["Cookie"], ["Cookie"], ["Cookie"], ["Cookie"],
                              ["Cookie"], ["Cookie"], ["Cookie"], ["Cookie"], ["Cookie"], ["Cookie"]]
        self.img_list = [file_name for file_name in
                         img_file_name_list]
        self.cur_img = 0
        self.img = self.img_list[self.cur_img]

    def set_image(self, img_number):
        self.cur_img = img_number
        self.img = self.img_list[self.cur_img]

    def goal_met(self):  # achieve goal by sleeping with 7 other characters
        if self.points >= 0:
            achieve = True
        else:
            achieve = False
        return achieve

    def dance(self, cue):
        if cue == 10:
            self.offset -= 3.2
        if cue == 20:
            self.offset += 3.2
        # if cue == 30:
        #     self.offset += 3.2
        # if cue == 40:
        #     self.offset -= 3.2

class Anton(Character):
    def __init__(self, x, y, img_file_name_list, points, emote, offset, name, classification, feeling, origin_x, origin_y, on_stage, location):
        super().__init__(x, y, img_file_name_list, points, emote, offset, name, classification, feeling, origin_x, origin_y, on_stage, location)
        self.offset = offset
        self.phrase_counter = 0
        self.phrases = {
            "dtf": ["oh, uh, well you'd be ", "surprised, I don't get asked", "that a lot. Uh, yes please. "],
            "sad": ["Dude...", "...", "bummer..."],
            "mad": ["Dude...", "What's wrong with you..?", ""],
            "small_talk0": ["Hey buddy,", "you can't be back here.", ""],
            "small_talk1": ["Yo, you want to buy some", "Anton brand sneakers?", "Limited edition!"],
            "small_talk2": ["Man,", "I could use a drink.", ""],
            "small_talk3": ["", "", ""],
            "small_talk4": ["", "", ""],
            "small_talk5": ["", "", ""],
            "small_talk6": ["", "", ""],
            "small_talk7": ["", "", ""],
            "small_talk8": ["", "", ""],
            "small_talk9": ["", "", ""],
            "small_talk10": ["", "", ""],
            "good_gift": ["Uh, hey,", "that's nice,", "I guess..."],
            "bad_gift": ["Look buddy,", "I don't want this.", ""],
            "follow:": ["Oooooooo,", "you two have fun!", ""],
            "request": ["What you feeling", "tonight? Daddy Anton's", "got a lil of everything."],
            "result": ["This one's an Anton", "original! I've got demos", "for sale, spread the word!"],
            "follow": ["OooooOOooooOOoO, ", "you kids have fun!", ""]}
        self.emotions = {"happy": ["assets/anton_happy.png"],
                         "mad": ["assets/mad/anton_mad.png"],
                         "sad": ["assets/sad/" + self.name + "_sad.png"],
                         "horny": ["assets/horny/" + self.name + "_horny.png"],
                         "thankful": ["assets/thankful/" + self.name + "_thankful.png"]}
        self.current_likes = [["Cookie", "Water"], ["Cookie"], ["Cookie", "Water"], ["Cookie"], ["Cookie", "Water"],
                              ["Cookie"], ["Cookie", "Water"], ["Cookie"], ["Cookie", "Water"], ["Cookie"], ["Cookie", "Water"]]
        self.img_list = [file_name for file_name in
                         img_file_name_list]
        self.cur_img = 0
        self.img = self.img_list[self.cur_img]

    def set_image(self, img_number):
        self.cur_img = img_number
        self.img = self.img_list[self.cur_img]

    def goal_met(self):  # Bring him a glass of water every ten minutes
        if self.points >= 0:
            achieve = True
        else:
            achieve = False
        return achieve

    def dance(self, cue):
        if cue == 10:
            self.offset -= 3.2
        if cue == 20:
            self.offset += 3.2
        # if cue == 30:
        #     self.offset += 3.2
        # if cue == 40:
        #     self.offset -= 3.2

class Galaxar(Character):
    def __init__(self, x, y, img_file_name_list, points, emote, offset, name, classification, feeling, origin_x, origin_y, on_stage, location):
        super().__init__(x, y, img_file_name_list, points, emote, offset, name, classification, feeling, origin_x, origin_y, on_stage, location)
        self.offset = offset
        self.phrase_counter = 0
        self.phrases = {
            "dtf": ["aw...", "That's uh- that's sweet.", "Why not, lets fuck!"],
            "sad": ["Of course,", "this is what happens when", "I try to be nice."],
            "mad": ["Ugh,", "can you just like", "leave me alone, maybe?"],
            "small_talk0": ["Sometimes I get grumpy, but", "then I think about muffins ", "and everything is okay."],
            "small_talk1": ["This club is always crowded,", "I don't mind people, but I ", "prefer an intimate setting."],
            "small_talk2": ["If you don't know anyone,", "you can dance with us. I", "want everyone to have fun."],
            "small_talk3": ["I should have worn other", "shoes. These ones are tight", "and now my feet are sweating."],
            "small_talk4": ["4", "", ""],
            "small_talk5": ["5", "", ""],
            "small_talk6": ["6", "", ""],
            "small_talk7": ["7", "", ""],  # information about butter
            "small_talk8": ["8", "", ""],
            "small_talk9": ["9", "", ""],
            "small_talk10": ["10", "", ""],
            "good_gift": ["I didn't expect this...", "you really are the nicest!", ""],
            "bad_gift": ["Do I look like someone", "who'd want something like", "this!!??"],
            "follow": ["OooooOOooooOOoO, ", "you kids have fun!", ""]}
        self.emotions = {"happy": ["assets/galaxar_happy.png"],
                         "mad": ["assets/mad/galaxar_mad.png"],
                         "sad": ["assets/sad/galaxar_sad.png"],
                         "horny": ["assets/horny/" + self.name + "_horny.png"],
                         "thankful": ["assets/thankful/" + self.name + "_thankful.png"]}
        self.current_likes = [["Muffin", "Cookie"], ["Muffin", "Cookie"], ["Muffin", "Cookie"], ["Muffin", "Cookie"], ["Muffin", "Cookie"],
                              ["Muffin", "Cookie"], ["Muffin", "Cookie"], ["Muffin", "Cookie"], ["Muffin", "Cookie"], ["Muffin", "Cookie"], ["Muffin", "Cookie"]]
        self.img_list = [file_name for file_name in
                         img_file_name_list]
        self.cur_img = 0
        self.img = self.img_list[self.cur_img]

    def set_image(self, img_number):
        self.cur_img = img_number
        self.img = self.img_list[self.cur_img]

    def dance(self, cue):
        if cue == 10:
            self.offset -= 3.2
        if cue == 20:
            self.offset += 3.2
        # if cue == 30:
        #     self.offset += 3.2
        # if cue == 40:
        #     self.offset -= 3.2

    def goal_met(self):  # achieve goal by feeding him muffins
        if self.points >= 0:
            achieve = True
        else:
            achieve = False
        return achieve


class Ishine(Character):
    def __init__(self, x, y, img_file_name_list, points, emote, offset, name, classification, feeling, origin_x, origin_y, on_stage, location):
        super().__init__(x, y, img_file_name_list, points, emote, offset, name, classification, feeling, origin_x, origin_y, on_stage, location)
        self.offset = offset
        self.phrases = {
            "dtf": ["Sweet!", "I mean...", "whatever, we may as well"],
            "sad": ["Oh... I was kinda hoping...", "nevermind...", ""],
            "mad": ["what!?", "You make no sense.", ""],
            "small_talk0": ["It's too loud in here, can't", "hear myself think... I mean,",
                            "whatever, I don't even care."],
            "small_talk1": ["Everyone in here is trying", "way too hard. they all", "look like posers."],
            "small_talk2": ["I'm just a really casual", "person, it doesn't bother", "me that it smells in here."],
            "small_talk3": ["", "", ""],
            "small_talk4": ["", "", ""],
            "small_talk5": ["", "", ""],
            "small_talk6": ["", "", ""],
            "small_talk7": ["", "", ""],
            "small_talk8": ["", "", ""],
            "small_talk9": ["", "", ""],
            "small_talk10": ["", "", ""],
            "good_gift": ["Literally, at last,", "someone's' treating my fine", "ass the way i deserve"],
            "bad_gift": ["This is gross, ew", "you're lucky i don't care", ""],
            "follow": ["OooooOOooooOOoO, ", "you kids have fun!", ""]}
        self.emotions = {"happy": ["assets/mad/ishine_mad.png"],
                         "mad": ["assets/mad/ishine_mad.png"],
                         "sad": ["assets/sad/ishine_sad.png"],
                         "horny": ["assets/horny/" + self.name + "_horny.png"],
                         "thankful": ["assets/thankful/" + self.name + "_thankful.png"]}
        self.current_likes = [["Cookie"], ["Cookie"], ["Cookie"], ["Cookie"], ["Cookie"],
                              ["Cookie"], ["Cookie"], ["Cookie"], ["Cookie"], ["Cookie"], ["Cookie"]]
        self.img_list = [file_name for file_name in
                         img_file_name_list]
        self.cur_img = 0
        self.img = self.img_list[self.cur_img]

    def set_image(self, img_number):
        self.cur_img = img_number
        self.img = self.img_list[self.cur_img]

    def goal_met(self):  # achieve goal by ignoring him for x amount of time
        if self.points >= 0:
            achieve = True
        else:
            achieve = False
        return achieve

    def dance(self, cue):
        if cue == 10:
            self.offset += 3.2
        if cue == 20:
            self.offset -= 3.2
        # if cue == 30:
        #     self.offset -= 3.2
        # if cue == 40:
        #     self.offset += 3.2

class Eveirg(Character):
    def __init__(self, x, y, img_file_name_list, points, emote, offset, name, classification, feeling, origin_x, origin_y, on_stage, location):
        super().__init__(x, y, img_file_name_list, points, emote, offset, name, classification, feeling, origin_x, origin_y, on_stage, location)
        self.offset = offset
        self.phrase_counter = 0
        self.phrases = {
            "dtf": ["OMG", "BABE", "<3 <3 <3"],
            "sad": ["...", "...", "..."],
            "mad": ["I...", "I just... You're ", "on my shitlist now bud."],
            "small_talk0": ["I wish they had food here", "maybe a snack platter... I'm ", "craving butter on a stick!"],
            "small_talk1": ["You ever just make a baking ", "soda volcano??? They're not ", "just for kids! BOOM!!!"],
            "small_talk2": ["I don't hold grudges,", "I just get even right away,", "BAM, GLITTER BOMB!"],
            "small_talk3": ["", "", ""],
            "small_talk4": ["", "", ""],
            "small_talk5": ["", "", ""],  # all about butter
            "small_talk6": ["", "", ""],
            "small_talk7": ["", "", ""],
            "small_talk8": ["", "", ""],
            "small_talk9": ["", "", ""],
            "small_talk10": ["", "", ""],
            "good_gift": ["Sweet syrupy nectar", "of ambrosia!", "You're an angel!!!"],
            "bad_gift": ["well, it's not butter", "", ""],
            "follow": ["OooooOOooooOOoO, ", "you kids have fun!", ""]}
        self.emotions = {
            "happy": ["assets/eveirg_happy.png"],
            "mad": ["assets/mad/eveirg_mad.png"],
                    "sad": ["assets/sad/" + self.name + "_sad.png"],
                         "horny": ["assets/horny/" + self.name + "_horny.png"],
                         "thankful": ["assets/thankful/" + self.name + "_thankful.png"]}
        self.current_likes = [["Butter"], ["Butter"], ["Butter"], ["Butter"], ["Butter"],
                              ["Butter"], ["Butter"], ["Butter"], ["Butter"], ["Butter"], ["Butter"]]
        self.img_list = [file_name for file_name in
                         img_file_name_list]
        self.cur_img = 0
        self.img = self.img_list[self.cur_img]

    def set_image(self, img_number):
        self.cur_img = img_number
        self.img = self.img_list[self.cur_img]

    def goal_met(self):  # give them butter!!!
        if self.points >= 1:
            achieve = True
        else:
            achieve = False
        return achieve

    def dance(self, cue):
        if cue == 10:
            self.offset -= 3.2
        if cue == 20:
            self.offset += 3.2
        # if cue == 30:
        #     self.offset += 3.2
        # if cue == 40:
        #     self.offset -= 3.2


class Zoop(Character):
    def __init__(self, x, y, img_file_name_list, points, emote, offset, name, classification, feeling, origin_x, origin_y, on_stage, location):
        super().__init__(x, y, img_file_name_list, points, emote, offset, name, classification, feeling, origin_x, origin_y, on_stage, location)
        self.offset = offset
        self.phrase_counter = 0
        self.phrases = {  #only speeks in haiku
            "dtf": ["uhn, oh yes master,", "please rearrange my inside,", "I've been very bad."],
            "sad": ["", "", ""],
            "mad": ["", "", ""],
            "small_talk0": ["Is my eye twitching?", "always does when I'm horny,", "oop, there it goes !twitch!"],
            "small_talk1": ["Everyone here could", "be a top tier hottie, but", "I lost my glasses"],
            "small_talk2": ["I'm kinda thirsty", "I mean, for a drink that is,", "no wait, that's not it..."],
            "small_talk3": ["", "", ""],
            "small_talk4": ["", "", ""],
            "small_talk5": ["", "", ""],
            "small_talk6": ["", "", ""],
            "small_talk7": ["", "", ""],
            "small_talk8": ["", "", ""],
            "small_talk9": ["", "", ""],
            "small_talk10": ["", "", ""],
            "follow": ["OooooOOooooOOoO, ", "you kids have fun!", ""],
            "good_gift": ["This is such a", "wondeful gift to receive", "indubitably!"],
            "bad_gift": ["ew, um, like, well, uh,", "This really isn't my thing,", "but thanks any way"]}
        self.emotions = {"happy": ["assets/zoop_happy.png"],
                         "mad": ["assets/mad/zoop_mad.png"],
                         "sad": ["assets/sad/" + self.name + "_sad.png"],
                         "horny": ["assets/horny/" + self.name + "_horny.png"],
                         "thankful": ["assets/thankful/" + self.name + "_thankful.png"]}
        self.current_likes = [["Cookie"], ["Cookie"], ["Cookie"], ["Cookie"], ["Cookie"],
                              ["Cookie"], ["Cookie"], ["Cookie"], ["Cookie"], ["Cookie"], ["Cookie"]]
        self.img_list = [file_name for file_name in
                         img_file_name_list]
        self.cur_img = 0
        self.img = self.img_list[self.cur_img]

    def set_image(self, img_number):
        self.cur_img = img_number
        self.img = self.img_list[self.cur_img]

    def goal_met(self):  # will sleep with you right away and as many times as you want
        # each of his small talks will hint at the way to successfully proposition another character
        if self.points >= 0:
            achieve = True
        else:
            achieve = False
        return achieve

    def dance(self, cue):
        if cue == 10:
            self.offset += 3.2
        if cue == 20:
            self.offset -= 3.2
        # if cue == 30:
        #     self.offset -= 3.2
        # if cue == 40:
        #     self.offset += 3.2

class Zirel(Character):
    def __init__(self, x, y, img_file_name_list, points, emote, offset, name, classification, feeling, origin_x, origin_y, on_stage, location):
        super().__init__(x, y, img_file_name_list, points, emote, offset, name, classification, feeling, origin_x, origin_y, on_stage, location)
        self.offset = offset
        self.phrase_counter = 0
        self.phrases = {
            "dtf": ["...", "...", "..."],
            "sad": ["???", "???", "???"],
            "mad": ["!!!", "!!!", "!!!"],
            "small_talk0": ["???", "!!!", "..."],
            "small_talk1": ["?", "!", "."],
            "small_talk2": ["?!.", "?!.", "?!."],
            "small_talk3": ["", "", ""],
            "small_talk4": ["", "", ""],
            "small_talk5": ["", "", ""],
            "small_talk6": ["", "", ""],
            "small_talk7": ["", "", ""],
            "small_talk8": ["", "", ""],
            "small_talk9": ["", "", ""],
            "small_talk10": ["", "", ""],
            "good_gift": ["...", "...", "..!"],
            "bad_gift": ["...", "", ""],
            "follow": ["OooooOOooooOOoO, ", "you kids have fun!", ""]}
        self.emotions = {"happy": ["assets/zirel_happy.png"],
                         "mad": ["assets/mad/zirel_mad.png"],
                         "sad": ["assets/sad/" + self.name + "_sad.png"],
                         "horny": ["assets/horny/" + self.name + "_horny.png"],
                         "thankful": ["assets/thankful/" + self.name + "_thankful.png"]}
        self.current_likes = [["Cookie"], ["Cookie"], ["Cookie"], ["Cookie"], ["Cookie"],
                              ["Cookie"], ["Cookie"], ["Cookie"], ["Cookie"], ["Cookie"], ["Cookie"]]
        self.img_list = [file_name for file_name in
                         img_file_name_list]
        self.cur_img = 0
        self.img = self.img_list[self.cur_img]

    def set_image(self, img_number):
        self.cur_img = img_number
        self.img = self.img_list[self.cur_img]

    def goal_met(self):
        if self.points >= 10:
            achieve = True
        else:
            achieve = False
        return achieve

    def dance(self, cue):
        if cue == 10:
            self.offset += 3.2
        if cue == 20:
            self.offset -= 3.2
        # if cue == 30:
        #     self.offset -= 3.2
        # if cue == 40:
        #     self.offset += 3.2

class Seedro(Character):
    def __init__(self, x, y, img_file_name_list, points, emote, offset, name, classification, feeling, origin_x, origin_y, on_stage, location):
        super().__init__(x, y, img_file_name_list, points, emote, offset, name, classification, feeling, origin_x, origin_y, on_stage, location)
        self.offset = offset
        self.phrase_counter = 0
        self.phrases = {
            "dtf": ["", "", ""],
            "sad": ["", "", ""],
            "mad": ["", "", ""],
            "small_talk0": ["What's worse than", "raining cats and dogs?", "Hailing taxis!"],
            "small_talk1": ["Why was the kingdom", "so wet? The queen had", "been reigning for 40 years!"],
            "small_talk2": ["What did the tricycle", "say when it say it's rival?", "Wheel, wheel, wheel..."],
            "small_talk3": ["", "", ""],
            "small_talk4": ["", "", ""],
            "small_talk5": ["", "", ""],
            "small_talk6": ["", "", ""],
            "small_talk7": ["", "", ""],
            "small_talk8": ["", "", ""],
            "small_talk9": ["", "", ""],
            "small_talk10": ["", "", ""],
            "good_gift": ["", "", ""],
            "bad_gift": ["", "", ""],
            "follow": ["OooooOOooooOOoO, ", "you kids have fun!", ""]}
        self.emotions = {"happy": ["assets/seedro_happy.png"],
                         "mad": ["assets/mad/seedro_mad.png"],
                         "sad": ["assets/sad/" + self.name + "_sad.png"],
                         "horny": ["assets/horny/" + self.name + "_horny.png"],
                         "thankful": ["assets/thankful/" + self.name + "_thankful.png"]}
        self.current_likes = [["Cookie"], ["Cookie"], ["Cookie"], ["Cookie"], ["Cookie"],
                              ["Cookie"], ["Cookie"], ["Cookie"], ["Cookie"], ["Cookie"], ["Cookie"]]
        self.img_list = [file_name for file_name in
                         img_file_name_list]
        self.cur_img = 0
        self.img = self.img_list[self.cur_img]

    def set_image(self, img_number):
        self.cur_img = img_number
        self.img = self.img_list[self.cur_img]

    def goal_met(self):  #
        if self.points >= 10:
            achieve = True
        else:
            achieve = False
        return achieve

    def dance(self, cue):
        if cue == 10:
            self.offset -= 3.2
        if cue == 20:
            self.offset += 3.2
        # if cue == 30:
        #     self.offset += 3.2
        # if cue == 40:
        #     self.offset -= 3.2

class Thickkaelious(Character):
    def __init__(self, x, y, img_file_name_list, points, emote, offset, name, classification, feeling, origin_x, origin_y, on_stage, location):
        super().__init__(x, y, img_file_name_list, points, emote, offset, name, classification, feeling, origin_x, origin_y, on_stage, location)
        self.offset = offset
        self.phrase_counter = 0
        self.phrases = {
            "dtf": ["", "", ""],
            "sad": ["", "", ""],
            "mad": ["", "", ""],
            "small_talk0": ["Hey faaaam, having a", "great time!! Follow me at", "@Thickkaelious, #werk"],
            "small_talk1": ["", "", ""],
            "small_talk2": ["", "", ""],
            "small_talk3": ["", "", ""],
            "small_talk4": ["", "", ""],
            "small_talk5": ["", "", ""],
            "small_talk6": ["", "", ""],
            "small_talk7": ["", "", ""],
            "small_talk8": ["", "", ""],
            "small_talk9": ["", "", ""],
            "small_talk10": ["", "", ""],
            "good_gift": ["", "", ""],
            "bad_gift": ["", "", ""],
            "follow": ["OooooOOooooOOoO, ", "you kids have fun!", ""]}
        self.emotions = {"happy": ["assets/thickkaelious_happy.png"],
                         "mad": ["assets/mad/thickkaelious_mad.png"],
                         "sad": ["assets/sad/" + self.name + "_sad.png"],
                         "horny": ["assets/horny/" + self.name + "_horny.png"],
                         "thankful": ["assets/thankful/" + self.name + "_thankful.png"]}
        self.current_likes = [["Cookie"], ["Cookie"], ["Cookie"], ["Cookie"], ["Cookie"],
                              ["Cookie"], ["Cookie"], ["Cookie"], ["Cookie"], ["Cookie"], ["Cookie"]]
        self.img_list = [file_name for file_name in
                         img_file_name_list]
        self.cur_img = 0
        self.img = self.img_list[self.cur_img]

    def set_image(self, img_number):
        self.cur_img = img_number
        self.img = self.img_list[self.cur_img]

    def goal_met(self):  # have atleast 2 points with every character
        if self.points >= 10:
            achieve = True
        else:
            achieve = False
        return achieve

    def dance(self, cue):
        if cue == 10:
            self.offset -= 3.2
        if cue == 20:
            self.offset += 3.2
        # if cue == 30:
        #     self.offset += 3.2
        # if cue == 40:
        #     self.offset -= 3.2

class Newman(Character):
    def __init__(self, x, y, img_file_name_list, points, emote, offset, name, classification, feeling, origin_x, origin_y, on_stage, location):
        super().__init__(x, y, img_file_name_list, points, emote, offset, name, classification, feeling, origin_x, origin_y, on_stage, location)
        self.offset = offset
        self.phrase_counter = 0
        self.phrases = {
            "dtf": ["", "", ""],
            "sad": ["", "", ""],
            "mad": ["", "", ""],
            "small_talk0": ["$%#(@)#", "@$@) @)$  @)($@_@", "*#@&$@&@("],
            "small_talk1": ["#$&*&()()", "^%$^%&^((", "%^&(*)("],
            "small_talk2": ["/*-*-/*/-*/*-", "*//-", "-/*-/-//-*/"],
            "small_talk3": ["", "", ""],
            "small_talk4": ["", "", ""],
            "small_talk5": ["", "", ""],
            "small_talk6": ["", "", ""],
            "small_talk7": ["", "", ""],
            "small_talk8": ["", "", ""],
            "small_talk9": ["", "", ""],
            "small_talk10": ["", "", ""],
            "good_gift": ["$$$$$", "$$$$$$$$", "$$$$$$"],
            "bad_gift": ["&&&&&&", "&&&&&&", "&&&&&&&&&"],
            "follow": ["OooooOOooooOOoO, ", "you kids have fun!", ""]}
        self.emotions = {"happy": ["assets/king_happy.png"],
                         "mad": ["assets/mad/king_mad.png"],
                         "sad": ["assets/sad/" "king" "_sad.png"],
                         "horny": ["assets/horny/" "king" "_horny.png"],
                         "thankful": ["assets/thankful/" + "king" + "_thankful.png"]}
        self.current_likes = [["Cookie"], ["Cookie"], ["Cookie"], ["Cookie"], ["Cookie"],
                              ["Cookie"], ["Cookie"], ["Cookie"], ["Cookie"], ["Cookie"], ["Cookie"]]
        self.img_list = [file_name for file_name in
                         img_file_name_list]
        self.cur_img = 0
        self.img = self.img_list[self.cur_img]

    def set_image(self, img_number):
        self.cur_img = img_number
        self.img = self.img_list[self.cur_img]

    def goal_met(self):  # give him the specific gifts he requests by translating his words
        if self.points >= 10:
            achieve = True
        else:
            achieve = False
        return achieve

    def dance(self, cue):
        if cue == 10:
            self.offset += 3.2
        if cue == 20:
            self.offset -= 3.2
        # if cue == 30:
        #     self.offset -= 3.2
        # if cue == 40:
        #     self.offset += 3.2

class Japeto(Character):
    def __init__(self, x, y, img_file_name_list, points, emote, offset, name, classification, feeling, origin_x, origin_y, on_stage, location):
        super().__init__(x, y, img_file_name_list, points, emote, offset, name, classification, feeling, origin_x, origin_y, on_stage, location)
        self.offset = offset
        self.phrase_counter = 0
        self.phrases = {
            "dtf": ["", "", ""],
            "sad": ["", "", ""],
            "mad": ["", "", ""],
            "small_talk0": ["I can read your mind...", "...but I don't want to", "...bet it's filthy in there."],
            "small_talk1": ["Hmmm, you're thinking about", "butter! No wait, I think I'm ", "getting some interference."],
            "small_talk2": ["Why don't you try", "reading my mind? I'll give", "you a hint, I'm tired."],
            "small_talk3": ["", "", ""],
            "small_talk4": ["", "", ""],
            "small_talk5": ["", "", ""],
            "small_talk6": ["", "", ""],
            "small_talk7": ["", "", ""],
            "small_talk8": ["", "", ""],
            "small_talk9": ["", "", ""],
            "small_talk10": ["", "", ""],
            "good_gift": ["", "", ""],
            "bad_gift": ["", "", ""],
            "follow": ["OooooOOooooOOoO, ", "you kids have fun!", ""]}
        self.emotions = {"happy": ["assets/japeto_happy.png"],
                         "mad": ["assets/mad/japeto_mad.png"],
                         "sad": ["assets/sad/" + self.name + "_sad.png"],
                         "horny": ["assets/horny/" + self.name + "_horny.png"],
                         "thankful": ["assets/thankful/" + self.name + "_thankful.png"]}
        self.current_likes = [["Cookie"], ["Cookie"], ["Cookie"], ["Cookie"], ["Cookie"],
                              ["Cookie"], ["Cookie"], ["Cookie"], ["Cookie"], ["Cookie"], ["Cookie"]]
        self.img_list = [file_name for file_name in
                         img_file_name_list]
        self.cur_img = 0
        self.img = self.img_list[self.cur_img]

    def set_image(self, img_number):
        self.cur_img = img_number
        self.img = self.img_list[self.cur_img]

    def goal_met(self):  #
        if self.points >= 5:
            achieve = True
        else:
            achieve = False
        return achieve

    def dance(self, cue):
        if cue == 10:
            self.offset += 3.2
        if cue == 20:
            self.offset -= 3.2
        # if cue == 30:
        #     self.offset -= 3.2
        # if cue == 40:
        #     self.offset += 3.2

class Merkle(Character):
    def __init__(self, x, y, img_file_name_list, points, emote, offset, name, classification, feeling, origin_x, origin_y, on_stage, location):
        super().__init__(x, y, img_file_name_list, points, emote, offset, name, classification, feeling, origin_x, origin_y, on_stage, location)
        self.offset = offset
        self.phrase_counter = 0
        self.phrases = {
            "dtf": ["", "", ""],
            "sad": ["", "", ""],
            "mad": ["", "", ""],
            "small_talk0": ["TURN IT UP", "TURN IT UUUPPP", "TURN IT UUUUUUUUUPPPPP"],
            "small_talk1": ["", "", ""],
            "small_talk2": ["", "", ""],
            "small_talk3": ["", "", ""],
            "small_talk4": ["", "", ""],
            "small_talk5": ["", "", ""],
            "small_talk6": ["", "", ""],
            "small_talk7": ["", "", ""],
            "small_talk8": ["", "", ""],
            "small_talk9": ["", "", ""],
            "small_talk10": ["", "", ""],
            "good_gift": ["", "", ""],
            "bad_gift": ["", "", ""],
            "follow": ["OooooOOooooOOoO, ", "you kids have fun!", ""]}
        self.emotions = {"happy": ["assets/merkle_happy.png"],
                         "mad": ["assets/mad/merkle_mad.png"],
                         "sad": ["assets/sad/" + self.name + "_sad.png"],
                         "horny": ["assets/horny/" + self.name + "_horny.png"],
                         "thankful": ["assets/thankful/" + self.name + "_thankful.png"]}
        self.current_likes = [["Cookie"], ["Cookie"], ["Cookie"], ["Cookie"], ["Cookie"],
                              ["Cookie"], ["Cookie"], ["Cookie"], ["Cookie"], ["Cookie"], ["Cookie"]]
        self.img_list = [file_name for file_name in
                         img_file_name_list]
        self.cur_img = 0
        self.img = self.img_list[self.cur_img]

    def set_image(self, img_number):
        self.cur_img = img_number
        self.img = self.img_list[self.cur_img]

    def goal_met(self): # atleast 5 points and have volume all the way up
        if self.points >= 10:
            achieve = True
        else:
            achieve = False
        return achieve

    def dance(self, cue):
        if cue == 10:
            self.offset += 3.2
        if cue == 20:
            self.offset -= 3.2
        # if cue == 30:
        #     self.offset -= 3.2
        # if cue == 40:
        #     self.offset += 3.2

class Emilius(Character):
    def __init__(self, x, y, img_file_name_list, points, emote, offset, name, classification, feeling, origin_x, origin_y, on_stage, location):
        super().__init__(x, y, img_file_name_list, points, emote, offset, name, classification, feeling, origin_x, origin_y, on_stage, location)
        self.offset = offset
        self.phrase_counter = 0
        self.phrases = {
            "dtf": ["", "", ""],
            "sad": ["", "", ""],
            "mad": ["", "", ""],
            "small_talk0": ["Hey fam, by any chance, do", "you know where I could get", "my hands on some Space-E?"],
            "small_talk1": ["", "", ""],
            "small_talk2": ["", "", ""],
            "small_talk3": ["", "", ""],
            "small_talk4": ["", "", ""],
            "small_talk5": ["", "", ""],
            "small_talk6": ["", "", ""],
            "small_talk7": ["", "", ""],
            "small_talk8": ["", "", ""],
            "small_talk9": ["", "", ""],
            "small_talk10": ["", "", ""],
            "good_gift": ["", "", ""],
            "bad_gift": ["", "", ""],
            "follow": ["OooooOOooooOOoO, ", "you kids have fun!", ""]}
        self.emotions = {"happy": ["assets/emilius_happy.png"],
                         "mad": ["assets/mad/emilius_mad.png"],
                         "sad": ["assets/sad/" + self.name + "_sad.png"],
                         "horny": ["assets/horny/" + self.name + "_horny.png"],
                         "thankful": ["assets/thankful/" + self.name + "_thankful.png"]}
        self.current_likes = [["Cookie"], ["Cookie"], ["Cookie"], ["Cookie"], ["Cookie"],
                              ["Cookie"], ["Cookie"], ["Cookie"], ["Cookie"], ["Cookie"], ["Cookie"]]
        self.img_list = [file_name for file_name in
                         img_file_name_list]
        self.cur_img = 0
        self.img = self.img_list[self.cur_img]

    def set_image(self, img_number):
        self.cur_img = img_number
        self.img = self.img_list[self.cur_img]

    def goal_met(self):  # give various drugs
        if self.points >= 10:
            achieve = True
        else:
            achieve = False
        return achieve

    def dance(self, cue):
        if cue == 10:
            self.offset -= 3.2
        if cue == 20:
            self.offset += 3.2
        # if cue == 30:
        #     self.offset += 3.2
        # if cue == 40:
        #     self.offset -= 3.2

class Queen(Character):
    def __init__(self, x, y, img_file_name_list, points, emote, offset, name, classification, feeling, origin_x, origin_y, on_stage, location):
        super().__init__(x, y, img_file_name_list, points, emote, offset, name, classification, feeling, origin_x, origin_y, on_stage, location)
        self.offset = offset
        self.phrase_counter = 0
        self.phrases = {
            "dtf": ["", "", ""],
            "sad": ["", "", ""],
            "mad": ["", "", ""],
            "small_talk0": ["", "", ""],
            "small_talk1": ["", "", ""],
            "small_talk2": ["", "", ""],
            "small_talk3": ["", "", ""],
            "small_talk4": ["", "", ""],
            "small_talk5": ["", "", ""],  # all about butter
            "small_talk6": ["", "", ""],
            "small_talk7": ["", "", ""],
            "small_talk8": ["", "", ""],
            "small_talk9": ["", "", ""],
            "small_talk10": ["", "", ""],
            "good_gift": ["", "", ""],
            "bad_gift": ["", "", ""],
            "follow": ["OooooOOooooOOoO, ", "you kids have fun!", ""]}
        self.emotions = {}
        self.current_likes = [["Cookie"], ["Cookie"], ["Cookie"], ["Cookie"], ["Cookie"],
                              ["Cookie"], ["Cookie"], ["Cookie"], ["Cookie"], ["Cookie"], ["Cookie"]]
        self.img_list = [file_name for file_name in
                         img_file_name_list]
        self.cur_img = 0
        self.img = self.img_list[self.cur_img]

    def set_image(self, img_number):
        self.cur_img = img_number
        self.img = self.img_list[self.cur_img]

    def goal_met(self):  # give them butter!!!
        if self.points >= 1:
            achieve = True
        else:
            achieve = False
        return achieve

    def dance(self, cue):
        if cue == 10:
            self.offset += 3.2
        if cue == 20:
            self.offset -= 3.2
        # if cue == 30:
        #     self.offset += 3.2
        # if cue == 40:
        #     self.offset -= 3.2

    def draw(self, screen):
        screen.blit((Spritesheet(self.img).image_at((0, 0, 32, 40))), [self.x * 32 + self.offset, (self.y * 32 - 16) - 16])

class Peach(Character):
    def __init__(self, x, y, img_file_name_list, points, emote, offset, name, classification, feeling, origin_x, origin_y, on_stage, location):
        super().__init__(x, y, img_file_name_list, points, emote, offset, name, classification, feeling, origin_x, origin_y, on_stage, location)
        self.offset = offset
        self.phrase_counter = 0
        self.phrases = {
            "dtf": ["", "", ""],
            "sad": ["", "", ""],
            "mad": ["", "", ""],
            "small_talk0": ["", "", ""],
            "small_talk1": ["", "", ""],
            "small_talk2": ["", "", ""],
            "small_talk3": ["", "", ""],
            "small_talk4": ["", "", ""],
            "small_talk5": ["", "", ""],  # all about butter
            "small_talk6": ["", "", ""],
            "small_talk7": ["", "", ""],
            "small_talk8": ["", "", ""],
            "small_talk9": ["", "", ""],
            "small_talk10": ["", "", ""],
            "good_gift": ["", "", ""],
            "bad_gift": ["", "", ""],
            "follow": ["OooooOOooooOOoO, ", "you kids have fun!", ""]}
        self.emotions = {"happy": ["assets/emilius_happy.png"],
                         "mad": ["assets/mad/emilius_mad.png"],
                         "sad": ["assets/sad/" + self.name + "_sad.png"],
                         "horny": ["assets/horny/" + self.name + "_horny.png"],
                         "thankful": ["assets/thankful/" + self.name + "_thankful.png"]}
        self.current_likes = [["Cookie"], ["Cookie"], ["Cookie"], ["Cookie"], ["Cookie"],
                              ["Cookie"], ["Cookie"], ["Cookie"], ["Cookie"], ["Cookie"], ["Cookie"]]
        self.img_list = [file_name for file_name in
                         img_file_name_list]
        self.cur_img = 0
        self.img = self.img_list[self.cur_img]

    def set_image(self, img_number):
        self.cur_img = img_number
        self.img = self.img_list[self.cur_img]

    def goal_met(self):  # give them butter!!!
        if self.points >= 1:
            achieve = True
        else:
            achieve = False
        return achieve

    def dance(self, cue):
        if cue == 10:
            self.offset += 3.2
        if cue == 20:
            self.offset -= 3.2
        # if cue == 30:
        #     self.offset += 3.2
        # if cue == 40:
        #     self.offset -= 3.2

    def draw(self, screen):
        screen.blit((Spritesheet(self.img).image_at((0, 0, 32, 40))), [self.x * 32 + self.offset, (self.y * 32 - 16)])
# print(self.name.__class__)