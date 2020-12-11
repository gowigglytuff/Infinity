import pygame

from test.spritesheet import Spritesheet
from test.gamestate import Character


class Galaxar(Character):
    def __init__(self, x, y, img_file_name_list, points, emote, offset, name, width=32, height=40):
        super().__init__(x, y, img_file_name_list, points, emote, offset, name, width=32, height=40)
        self.offset = offset
        self.name = name
        self.phrases = {
            "dtf": ["aw...", "That's uh- that's sweet.", "Why not, lets fuck!"],
            "sad": ["Of course,", "this is what happens when", "I try to be nice."],
            "mad": ["Ugh,", "can you just like", "leave me alone, maybe?"],
            "small_talk0": ["I should have worn other", "shoes. These ones are tight", "and now my feet are sweating."],
            "small_talk1": ["This club is always crowded,", "I don't mind people, but I ", "prefer an intimate setting."],
            "small_talk2": ["If you don't know anyone,", "you can dance with us. I", "want everyone to have fun."],
            "small_talk3": ["", "", ""],
            "small_talk4": ["", "", ""],
            "small_talk5": ["", "", ""],
            "small_talk6": ["", "", ""],
            "small_talk7": ["", "", ""],
            "small_talk8": ["", "", ""],
            "small_talk9": ["", "", ""],
            "small_talk10": ["", "", ""],
            "good_gift": ["I didn't expect this...", "you really are the nicest!", ""],
            "bad_gift": ["Do I look like someone", "who'd want something like", "this!!??"]}
        self.emotions = {"happy": ["assets/galaxar_happy.png"],
                         "mad": ["assets/mad/galaxar_mad.png"],
                         "sad": ["assets/sad/galaxar_sad.png"]}
        self.likes = ["Muffin"]

    def goal_met(self):
        if self.points >= 3:
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
            "good_gift": ["Literally, at last," "someone's' treating my fine", "ass the way i deserve"],
            "bad_gift": ["This is gross, ew", "you're lucky i don't care", ""]}
        self.emotions = {"happy": ["assets/mad/ishine_mad.png"],
                         "mad": ["assets/mad/ishine_mad.png"],
                         "sad": ["assets/sad/ishine_sad.png"]}
        self.likes = ["Vodka_soda"]

    def goal_met(self):
        if self.points >= 0:
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
            "dtf": ["Awww,", "ain't you just", "the sweetest thing!"],
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
            "information": ["what can I get you?", "", ""]}
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
            "dtf": ["OMG", "BABE", "<3 <3 <3"],
            "sad": ["...", "...", "..."],
            "mad": ["I...", "I just... You're ", "on my shitlist now bud."],
            "small_talk0": ["I wish they had food here", "maybe a snack platter... I'm ", "craving butter on a stick!"],
            "small_talk1": ["You ever just make a baking ", "soda volcano??? They're not ", "just for kids! BOOM!!!"],
            "small_talk2": ["I don't hold grudges,", "I just get even right away,", "BAM, GLITTER BOMB!"],
            "small_talk3": ["", "", ""],
            "small_talk4": ["", "", ""],
            "small_talk5": ["", "", ""],
            "small_talk6": ["", "", ""],
            "small_talk7": ["", "", ""],
            "small_talk8": ["", "", ""],
            "small_talk9": ["", "", ""],
            "small_talk10": ["", "", ""],
            "good_gift": ["Sweet syrupy nectar", "of ambrosia!", "You're an angel!!!"],
            "bad_gift": ["well, it's not butter", "", ""]}
        self.emotions = {
            "happy": ["assets/eveirg_happy.png"],
            "mad": ["assets/mad/eveirg_mad.png"],
                    "sad": ["assets/sad/" + self.name + "_sad.png"]}
        self.likes = ["Butter"]

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
            "dtf": ["Ahahaha", "You're alright, I guess.", ""],
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
            "dtf": ["", "", ""],
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
            "bad_gift": ["", "", ""]}
        self.emotions = {"happy": ["assets/japeto_happy.png"],
                         "mad": ["assets/mad/japeto_mad.png"],
                         "sad": ["assets/sad/" + self.name + "_sad.png"]}
        self.likes = ["Muffin"]

    def goal_met(self):
        if self.points >= 5:
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