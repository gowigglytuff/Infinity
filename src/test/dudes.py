import pygame

from test.spritesheet import Spritesheet
from test.gamestate import Character


class Galaxar(Character):
    def __init__(self, x, y, img_file_name_list, points, emote, offset, name, width=32, height=40):
        super().__init__(x, y, img_file_name_list, points, emote, offset, name, width=32, height=40)
        self.offset = offset
        self.name = name
        self.phrases = {
            "happy": ["aw...", "um...", "That's uh- that's sweet."],
            "sad": ["Of course,", "this is what happens when", "I try to be nice."],
            "mad": ["Ugh,", "can you just like", "leave me alone, maybe?"],
            "small_talk1": ["I should have worn other", "shoes. These ones are tight", "and now my feet are sweating."],
            "small_talk2": ["This club is always crowded,", "I don't mind people, but I ", "prefer an intimate setting."],
            "small_talk3": ["If you don't know anyone,", "you can dance with us. I", "want everyone to have fun."],
            "good_gift": ["I didn't expect this...", "you really are the nicest!", ""],
            "bad_gift": ["Do I look like someone", "who'd want something like", "this!!??"]}
        self.emotions = {"happy": ["assets/galaxar_happy.png"],
                         "mad": ["assets/mad/galaxar_mad.png"],
                         "sad": ["assets/sad/galaxar_sad.png"]}
        self.likes = [""]

    def goal_met(self):
        if self.points >= 10:
            achieve = True
        else:
            achieve = False
        return achieve

class Ishine(Character):
    def __init__(self, x, y, img_file_name_list, points, emote, offset, name, width=32, height=40):
        super().__init__(x, y, img_file_name_list, points, emote, offset, name, width=32, height=40)
        self.offset = offset
        self.name = name
        self.phrases = {
            "happy": ["Sweet!", "I mean...", "that's fine I guess"],
            "sad": ["Oh... I was kinda hoping...", "nevermind...", ""],
            "mad": ["what!?", "You make no sense,", ""],
            "small_talk1": ["It's too loud in here, can't", "hear myself think... I mean,",
                            "whatever, I don't even care"],
            "small_talk2": ["Everyone in here is trying", "way too hard. they all", "look like posers."],
            "small_talk3": ["I'm just a really casual", "person, it doesn't bother", "me that it smells in here."],
            "good_gift": ["Literally, at last," "someone's' treating my fine", "ass the way i deserve"],
            "bad_gift": ["This is gross, ew", "you're lucky i don't care", ""]}
        self.emotions = {"happy": ["assets/ishine_happy.png"],
                         "mad": ["assets/mad/ishine_mad.png"],
                         "sad": ["assets/sad/ishine_sad.png"]}
        self.likes = ["Vodka_soda"]

    def goal_met(self):
        if self.points >= 10:
            achieve = True
        else:
            achieve = False
        return achieve

class Seeder(Character):
    def __init__(self, x, y, img_file_name_list, points, emote, offset, name, width=32, height=40):
        super().__init__(x, y, img_file_name_list, points, emote, offset, name, width=32, height=40)
        self.offset = offset
        self.name = name
        self.phrases = {
            "happy": ["Awww,", "ain't you just", "the sweetest thing!"],
            "sad": ["Well now I've", "gone and made", "myself sad."],
            "mad": ["I'm sorry, but that", "makes me a little", "uncomfortable."],
            "small_talk1": ["I love this job!", "It gives me the opportunity", "to meet lots of cool folks!"],
            "small_talk2": ["You're probably not supposed", "to be back here, just make ", "sure, my boss doesn't see!"],
            "small_talk3": ["I bartend nights to get", "by while I work on my career", "as a singer!"],
            "good_gift": ["Oh my goodness!", "This is the best tip", "I've ever received!"],
            "bad_gift": ["Uh, I can't accept something", "like this from a customer.", "Thanks anyway."]}
        self.emotions = {"happy": ["assets/seeder_happy.png"],
                         "mad": ["assets/mad/seedro_mad.png"],
                         "sad": ["assets/sad/" + "seedro" + "_sad.png"]}
        self.likes = [""]

    def goal_met(self):
        if self.points >= 10:
            achieve = True
        else:
            achieve = False
        return achieve

class Eveirg(Character):
    def __init__(self, x, y, img_file_name_list, points, emote, offset, name, width=32, height=40):
        super().__init__(x, y, img_file_name_list, points, emote, offset, name, width=32, height=40)
        self.offset = offset
        self.name = name
        self.phrases = {
            "happy": ["OMG", "BABE", "<3 <3 <3"],
            "sad": ["...", "...", "..."],
            "mad": ["I...", "I just... You're ", "on my shitlist now bud."],
            "small_talk1": ["I wish they had food here", "maybe a snack platter... I'm ", "craving butter on a stick!"],
            "small_talk2": ["You ever just make a baking ", "soda volcano??? They're not ", "just for kids! BOOM!!!"],
            "small_talk3": ["I don't hold grudges,", "I just get even right away,", "BAM, GLITTER BOMB!"],
            "good_gift": ["Sweet syrupy nectar", "of ambrosia!", "You're an angel!!!"],
            "bad_gift": ["well, it's not butter", "", ""]}
        self.emotions = {
            "happy": ["assets/eveirg_happy.png"],
            "mad": ["assets/mad/eveirg_mad.png"],
                    "sad": ["assets/sad/" + self.name + "_sad.png"]}
        self.likes = ["butter"]

    def goal_met(self):
        if self.points >= 10:
            achieve = True
        else:
            achieve = False
        return achieve

class Anton(Character):
    def __init__(self, x, y, img_file_name_list, points, emote, offset, name, width=32, height=40):
        super().__init__(x, y, img_file_name_list, points, emote, offset, name, width=32, height=40)
        self.offset = offset
        self.name = name
        self.phrases = {
            "happy": ["Ahahaha", "You're alright, I guess.", ""],
            "sad": ["Dude...", "...", "bummer..."],
            "mad": ["Dude...", "What's wrong with you..?", ""],
            "small_talk1": ["Hey buddy,", "you can't be back here.", ""],
            "small_talk2": ["Yo, you want to buy some", "Anton brand sneakers?", "Limited edition!"],
            "small_talk3": ["Man,", "I could use a drink.", ""],
            "good_gift": ["Uh, hey,", "that's nice,", "I guess..."],
            "bad_gift": ["Look buddy,", "I don't want this.", ""]}
        self.emotions = {"happy": ["assets/anton_happy.png"],
                         "mad": ["assets/mad/anton_mad.png"],
                         "sad": ["assets/sad/" + self.name + "_sad.png"]}
        self.likes = ["Water"]

    def goal_met(self):
        if self.points >= 10:
            achieve = True
        else:
            achieve = False
        return achieve

class Zoop(Character):
    def __init__(self, x, y, img_file_name_list, points, emote, offset, name, width=32, height=40):
        super().__init__(x, y, img_file_name_list, points, emote, offset, name, width=32, height=40)
        self.offset = offset
        self.name = name
        self.phrases = {
            "happy": ["", "", ""],
            "sad": ["", "", ""],
            "mad": ["", "", ""],
            "small_talk1": ["Is my eye twitching?", "always does when I'm horny,", "oop, there it goes !twitch!"],
            "small_talk2": ["everyone here could", "be a top tier hottie, but", "I lost my glasses"],
            "small_talk3": ["I'm kinda thirsty", "I mean, for a drink that is,", "no wait, that's not it..."],
            "good_gift": ["This is such a", "wondeful gift to receive", "indubitably!"],
            "bad_gift": ["ew, um, like, well, uh,", "This really isn't my thing,", "thanks any way"]}
        self.emotions = {"happy": ["assets/zoop_happy.png"],
                         "mad": ["assets/mad/zoop_mad.png"],
                         "sad": ["assets/sad/" + self.name + "_sad.png"]}
        self.likes = [""]

    def goal_met(self):
        if self.points >= 10:
            achieve = True
        else:
            achieve = False
        return achieve

class Zirel(Character):
    def __init__(self, x, y, img_file_name_list, points, emote, offset, name, width=32, height=40):
        super().__init__(x, y, img_file_name_list, points, emote, offset, name, width=32, height=40)
        self.offset = offset
        self.name = name
        self.phrases = {
            "happy": ["...", "...", "..."],
            "sad": ["???", "???", "???"],
            "mad": ["!!!", "!!!", "!!!"],
            "small_talk1": ["???", "!!!", "..."],
            "small_talk2": ["?", "!", "."],
            "small_talk3": ["?!.", "?!.", "?!."],
            "good_gift": ["...", "...", "..!"],
            "bad_gift": ["...", "", ""]}
        self.emotions = {"happy": ["assets/zirel_happy.png"],
                         "mad": ["assets/mad/zirel_mad.png"],
                         "sad": ["assets/sad/" + self.name + "_sad.png"]}
        self.likes = [""]

    def goal_met(self):
        if self.points >= 10:
            achieve = True
        else:
            achieve = False
        return achieve

class Seedro(Character):
    def __init__(self, x, y, img_file_name_list, points, emote, offset, name, width=32, height=40):
        super().__init__(x, y, img_file_name_list, points, emote, offset, name, width=32, height=40)
        self.offset = offset
        self.name = name
        self.phrases = {
            "happy": ["", "", ""],
            "sad": ["", "", ""],
            "mad": ["", "", ""],
            "small_talk1": ["What's worse than", "raining cats and dogs?", "Hailing taxis!"],
            "small_talk2": ["Why was the kingdom", "so wet? The queen had", "been reigning for 40 years!"],
            "small_talk3": ["What did the tricycle", "say when it say it's rival?", "Wheel, wheel, wheel..."],
            "good_gift": ["", "", ""],
            "bad_gift": ["", "", ""]}
        self.emotions = {"happy": ["assets/seedro_happy.png"],
                         "mad": ["assets/mad/seedro_mad.png"],
                         "sad": ["assets/sad/" + self.name + "_sad.png"]}
        self.likes = [""]

    def goal_met(self):
        if self.points >= 10:
            achieve = True
        else:
            achieve = False
        return achieve

class Thickkaelious(Character):
    def __init__(self, x, y, img_file_name_list, points, emote, offset, name, width=32, height=40):
        super().__init__(x, y, img_file_name_list, points, emote, offset, name, width=32, height=40)
        self.offset = offset
        self.name = name
        self.phrases = {
            "happy": ["", "", ""],
            "sad": ["", "", ""],
            "mad": ["", "", ""],
            "small_talk1": ["Hey faaaam, having a", "great time!! Follow me at", "@Thickkaelious, #werk"],
            "small_talk2": ["", "", ""],
            "small_talk3": ["", "", ""],
            "good_gift": ["", "", ""],
            "bad_gift": ["", "", ""]}
        self.emotions = {"happy": ["assets/thickkaelious_happy.png"],
                         "mad": ["assets/mad/thickkaelious_mad.png"],
                         "sad": ["assets/sad/" + self.name + "_sad.png"]}
        self.likes = [""]

    def goal_met(self):
        if self.points >= 10:
            achieve = True
        else:
            achieve = False
        return achieve

class King(Character):
    def __init__(self, x, y, img_file_name_list, points, emote, offset, name, width=32, height=40):
        super().__init__(x, y, img_file_name_list, points, emote, offset, name, width=32, height=40)
        self.offset = offset
        self.name = name
        self.phrases = {
            "happy": ["", "", ""],
            "sad": ["", "", ""],
            "mad": ["", "", ""],
            "small_talk1": ["$%#(@)#", "@$@) @)$  @)($@_@", "*#@&$@&@("],
            "small_talk2": ["#$&*&()()", "^%$^%&^((", "%^&(*)("],
            "small_talk3": ["/*-*-/*/-*/*-", "*//-", "-/*-/-//-*/"],
            "good_gift": ["", "", ""],
            "bad_gift": ["", "", ""]}
        self.emotions = {"happy": ["assets/king_happy.png"],
                         "mad": ["assets/mad/king_mad.png"],
                         "sad": ["assets/sad/" + self.name + "_sad.png"]}
        self.likes = [""]

    def goal_met(self):
        if self.points >= 10:
            achieve = True
        else:
            achieve = False
        return achieve

class Japeto(Character):
    def __init__(self, x, y, img_file_name_list, points, emote, offset, name, width=32, height=40):
        super().__init__(x, y, img_file_name_list, points, emote, offset, name, width=32, height=40)
        self.offset = offset
        self.name = name
        self.phrases = {
            "happy": ["", "", ""],
            "sad": ["", "", ""],
            "mad": ["", "", ""],
            "small_talk1": ["I can read your mind...", "...but I don't want to", "...bet it's filthy in there."],
            "small_talk2": ["Hmmm, you're thinking about", "butter! No wait, I think I'm ", "getting some interference."],
            "small_talk3": ["Why don't you try", "reading my mind? I'll give", "you a hint, I'm tired."],
            "good_gift": ["", "", ""],
            "bad_gift": ["", "", ""]}
        self.emotions = {"happy": ["assets/japeto_happy.png"],
                         "mad": ["assets/mad/japeto_mad.png"],
                         "sad": ["assets/sad/" + self.name + "_sad.png"]}
        self.likes = ["Muffin"]

    def goal_met(self):
        if self.points >= 10:
            achieve = True
        else:
            achieve = False
        return achieve

class Merkle(Character):
    def __init__(self, x, y, img_file_name_list, points, emote, offset, name, width=32, height=40):
        super().__init__(x, y, img_file_name_list, points, emote, offset, name, width=32, height=40)
        self.offset = offset
        self.name = name
        self.phrases = {
            "happy": ["", "", ""],
            "sad": ["", "", ""],
            "mad": ["", "", ""],
            "small_talk1": ["TURN IT UP", "TURN IT UUUPPP", "TURN IT UUUUUUUUUPPPPP"],
            "small_talk2": ["", "", ""],
            "small_talk3": ["", "", ""],
            "good_gift": ["", "", ""],
            "bad_gift": ["", "", ""]}
        self.emotions = {"happy": ["assets/merkle_happy.png"],
                         "mad": ["assets/mad/merkle_mad.png"],
                         "sad": ["assets/sad/" + self.name + "_sad.png"]}
        self.likes = [""]

    def goal_met(self):
        if self.points >= 10:
            achieve = True
        else:
            achieve = False
        return achieve

class Emilius(Character):
    def __init__(self, x, y, img_file_name_list, points, emote, offset, name, width=32, height=40):
        super().__init__(x, y, img_file_name_list, points, emote, offset, name, width=32, height=40)
        self.offset = offset
        self.name = name
        self.phrases = {
            "happy": ["", "", ""],
            "sad": ["", "", ""],
            "mad": ["", "", ""],
            "small_talk1": ["Hey fam, by any chance, do", "you know where I could get", "my hands on some Space-E?"],
            "small_talk2": ["", "", ""],
            "small_talk3": ["", "", ""],
            "good_gift": ["", "", ""],
            "bad_gift": ["", "", ""]}
        self.emotions = {"happy": ["assets/emilius_happy.png"],
                         "mad": ["assets/mad/emilius_mad.png"],
                         "sad": ["assets/sad/" + self.name + "_sad.png"]}
        self.likes = [""]

    def goal_met(self):
        if self.points >= 10:
            achieve = True
        else:
            achieve = False
        return achieve

# print(self.name.__class__)