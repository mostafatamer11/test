# by mostafa tamer mostafa
# Just before you can see this program
# I should NOTE that it contains some advanced 
# python principles 
# the reason for me being able to do all of that is 
# the UDACITY and DECI introduction to 
# programming just want to thank you all

class GameLooserError(Exception):
    def __init__(self, exception):
        self.exception = exception

class GameEndError(Exception):
    def __init__(self, exception):
        self.exception = exception


LINK = "https://www.udacity.com/"
print(f"look at {LINK} for cool courses")

from time import sleep 
from keyboard import is_pressed as key

CHARS = ["\\", "|", "/", "|"]

LINEUP = "\033[1A"
LINECLEAR = "\x1b[2K"

# I will make a class to make the code easier to read and more organized
class game:
    import random
    THINGS = ["Harry potter", "Marlin", "The magical dragon", "The fairy"]
    PEOPLE = ["Magician", "Pirate", "Evil Fairy", "Troll"]
    LOST = ["a frog", "an ant", "an ugly bird"]
    
    sb = random.choice(PEOPLE)
    smth = random.choice(THINGS)
    lost = random.choice(LOST)
    
    print("hold \'esc\' to skip animation", end="\n\n")
    doneCave = False
    run = False
    score = 1
    def initilize(self):
        self.write("You find yourself standing in an open field, filled with grass and yellow wildflowers.")
        self.write(f"Rumor has it that a {self.sb} is somewhere around here, and has been terrifying the nearby villages.")
        self.write("In front of you is a house.")
        self.write("To your right is a dark cave.")
        self.write("In your hand you hold your trusty (but not very effective) rusty old magic wand.")
        self.write("")

    def __init__(self):
        print(f"score: {self.score}", "\n"*2)
        self.initilize() if not (self.doneCave or self.run) else ...
        self.run = False
        self.choice()
        if self.theMoveNo_ == 1: 
            self.house()
            if self.run:
                self.write("You run back into the field. Luckily, you don't seem to have been followed.")
                self.__init__()
            elif not self.run and self.doneCave: self.win()
            else: self.lose()
        else:
            self.cave1() if not self.doneCave else self.cave2()
            self.__init__()

    ###########################################
    #-------------- description --------------#
    ###########################################
    # this function is made to 
    # write the text character character 
    # to give the illusion that its being written 
    # by hand
    
    ###########################################
    #-------------- How it work --------------#
    ###########################################
    # it sclices the text so that each item is 
    # more than the one before it by one character
    # then it prints each item then clear it then
    # it writes the next item
    
    ###########################################
    #---------------- example ----------------#
    ###########################################
    # >>>write("hello, how are you?")
    # h (then clear it)
    # he (then clear it)
    # hel (then clear it)
    # and so on
    
    def write(self, text:str): 
        chars = []                              # create the list

        for indx in range(len(text)+1):         # the slicing loop
            chars.append(text[:indx])           # appends the slice to the list

        for lett in chars:                      # the writig loop
            if not key("esc"):                  # checks if I pressed "esc"
                print(LINEUP, end=LINECLEAR)    # clear the line before it
                sleep(0.07)                     
                print(lett)                     # then prints each indivisual
                if self.score < 0:
                    raise GameLooserError(f"score: {self.score}")
            else: print(text); break     # if you pressed "esc" it will print the text then stop the loop 
        sleep(0.5)

    ###########################################
    #-------------- description --------------#
    ###########################################

    # this function is an input function but will only accept 1 or 2 as a string
    # then return it as an intsince it only accept 1 or 2
    ###########################################
    #-------------- How it work --------------#
    ###########################################

    # it will taake the input in a variable then enter a loop
    # that loop will stop when the input is equal to 1 or 2
    # that means that if the input is 1 or 2 the loop won't activate
    # inside the loop it asks for the input until its 1 or 2

    ###########################################
    #---------------- example ----------------#
    ###########################################
    # >>> inp()
    #   (input 1 or 2)3
    #   (input 1 or 2)7khc 
    #   (input 1 or 2)2
    #

    def inp(self):
        ans = input("\t(Please enter 1 or 2.)")       # takes the input
        while not (ans == "1" or ans =="2"):          # the loop
            ans = input("\t(Please enter 1 or 2.)")   # takes input if the first input != 1 | 2
        return int(ans)                               # when the loop is done return the input as an int (1 or 2)
    
    def house(self):
        self.write("You approach the door of the house.")
        self.write(f"You are about to knock when the door opens and out steps a {self.sb}.")
        self.write("Eep! This is the troll's house!")
        self.write("The troll finds you!")
        if not self.doneCave:
            self.write("You feel a bit under-prepared for this, what with only having a tiny, rusty old magic wand.")
        self.write("Would you like to (1) cast a spell or (2) run away?")
        self.run = self.inp() == 2
        if self.run: self.score -= 1
        
    def choice(self):
        print("Enter 1 to knock on the door of the house.")
        print("Enter 2 to peer into the cave.")
        self.write("What would you like to do?")
        self.theMoveNo_ = self.inp()
    
    def cave1(self):
        self.write("You peer cautiously into the cave.")
        self.write("It turns out to be only a very small cave.")
        self.write("Your eye catches a glint of metal behind a rock.")
        self.write(f"You have found the magical Wand of {self.smth}!")
        self.write(f"You discard your rusty old magic wand and take the Wand of {self.smth} with you.")
        self.write("You walk back out to the field.")
        self.doneCave = True
        self.score += 1
        
    def cave2(self):
        self.write("You peer cautiously into the cave.")
        self.write("You've been here before, and gotten all the good stuff. It's just an empty cave now.")
        self.write("You walk back out to the field.")
        self.score -= 1

    def win(self):
        self.write(f"As the {self.sb} moves to cast a spell, you raise your new Wand of {self.smth}.")
        self.write(f"The Wand of {self.smth} shines brightly in your hand as you brace yourself for the spell.")
        self.write(f"But the {self.sb} takes one look at your shiny new wand and runs away!")
        self.write("You have rid the town of the troll. You are victorious!")

    def lose(self):
        self.write("You do your best...")
        self.write(f"but your rusty old magic wand is no match for the {self.sb}.")
        self.write(f"You have been turned into {self.lost}!")

def ask_game():
        inpt = input("do you wanna play again(y/n)")
        while not inpt in "yn" and inpt != "":
            inpt = input("do you wanna play again(y/n)")
        if inpt.lower() == "n":
            print("""thank you for playing my game,
    if want to see more of my games,
    well you won\'t be able to because this is my only game"""); return True

def play():
    try:
        game()
        print("\n")
        if ask_game(): raise GameEndError("Game shuted down")
    except KeyboardInterrupt:
        print("\n\n\nI\'m sad,\nwhy you wanna close my game????????\n")
        if ask_game(): raise GameEndError("Game shuted down")
    except GameLooserError as gg:
        print(f"you lost because your score dropped to \'-1\'\n{gg.exception}")
        if ask_game(): raise GameEndError("Game shuted down")

while True:
    try:
        play()
    except KeyboardInterrupt: print("\nok, ok I will shut it"); break
    except: break