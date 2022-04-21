import random
import sys #two general imports that could help with the idea
from colorama import Fore, Style, Back #import for colored text built into python
import time # for dramatic pauses lol

# To Figure Out
# [X] How to make the user download colorama without them running the specific terminal command (requirements.txt)

# To-Do List
# [X] Define function for choice making
# [X] Define functions for up and down score for final ending
# [X] Outline story through comments
# [X] Define functions for different people to talk (different colors)
# [X] NAME IT!

nullVar = 'null' # a null variable for debugging and ease of access
score = 0 # beginning the universal score that defines the ending of the game
ans = 0 # setting the answer equal to zero so i can use the choice function

def Choice(inp): #function that will call for you to choose between 1 and 2 and return a variable equal to that answer allowing to change score and print outputs
    inp = input('Make your choice...   ')
    if inp == '1':
        global ans
        ans = 1
        return ans
    elif inp == '2':
        ans = 2
        return ans

def scoreUp(amount): # makes the score go up 1 * the amount of importance of the action
    global score
    score = score + (1 * amount)

def scoreDown(amount): # same as score up
    global score
    score = score - (1 * amount) 

# Here down is all function to color the text of the different characters in the terminal

def Choices(str):
    print(Fore.WHITE + str)

def Kasper(str):
    print(Fore.CYAN + str)

def Sawyer(str):
    print(Fore.GREEN + str)

def Markus(str):
    print(Fore.BLUE + str)

def Penelope(str):
    print(Fore.RED + str)

def Donovan(str):
    print(Fore.YELLOW + str)

def Her(str):
    print(Fore.MAGENTA + Style.BRIGHT + str)

def You(str):
    print(Fore.WHITE + Style.BRIGHT + str)

def warning(str):
    print(Back.RED + Fore.WHITE + Style.BRIGHT + str)
    print(Style.RESET_ALL)

# This ends the usable functions

# Second To-Do List
# [X] Functions for different interactions and the three or more endings
# [X] opening scene where the premise is described
# [X] naming of all the characters / colors EXCEPT Her she will always just be called Her
# [X] have the main interactions just happen with occasional score checks to decide the pathway you go down

def KnowItAll(): # functions used to react to different answers
    time.sleep(1)
    Kasper("Of course you know everything... You know that's why I hate you right!")
    time.sleep(2)
    You("I know. I know. I can be a little cocky.")
    time.sleep(2)
    You("I'll try to help you out I promise.")
    scoreUp(1)
    

def NotQuiteSure(): # functions used to react to different answers
    time.sleep(1)
    Kasper("Liar!! You're a know it all and you know it.")
    You("Okay. Okay. Maybe I remember it all.")
    scoreDown(0)

# Opening scene where the premise is introduced

warning('Every choice you make in this story matters so be careful in what you say to people... remember lying is bad!')
time.sleep(3)

Kasper("It was the year we got sent home from school for Covid-19...")
time.sleep(2)
Kasper("Of course that is years ago so I am a little fishy on what happened completely that's what you're here for right?")
time.sleep(3)
Kasper("Right?!")
time.sleep(1)

Choices("1) Of course Kasper I remember it all!")
Choices("2) I think I remember it a little differently...")
Choice(nullVar)

if ans == 1:
    KnowItAll()
elif ans == 2:
    NotQuiteSure()

# Beginning of the real story
# If you are good its Kasper talking at your wedding if you are bad it is Kasper talking about how you messed thing up with a gorgeous girl
# A good number in between is just talking about how they met one of their closest friends

# Description of Her and how they met Her
time.sleep(2)
Kasper("So we were walking into sophmore year of High School right?")
time.sleep(1)
Choices("1) Yeah!")
Choices("2) Oh my god that long ago... Seems like yesterday")
Choice(nullVar)

time.sleep(1)
Kasper("We see this gorgeous looking girl and I swear you were drooling.")
Kasper("The whole gang me, you and Sawyer all looked like deer in headlights.")
time.sleep(3)

Choices("1) I was hardly like that. You're being a little silly. haha")
Choices("2) I sure was she was stunning. We gave her a nickname... we called her 'The Girl.'")
Choice(nullVar)

if ans == 1:
    scoreDown(1) # Score can be as low as -1 or as high as 2 at this point
elif ans == 2:
    scoreUp(1)

time.sleep(1)

You("Either way you put it she had poofy brown hair and when she put it in a messy bun it was like the teacher you had a crush on in second grade.")
time.sleep(2)
You("I have to admit to the inital crush but of course that was just off her looks. I'm above that, you know me.")
time.sleep(3)

Kasper("Okay love bird...")
time.sleep(1)
Kasper("We just had to get to know her so we sent Sawyer in and he asked... What did he ask?")

Choices("1) He asked if she would sit with us at lunch")
Choices("2) He asked for her number!!!")
Choice(nullVar)

def AskingforNum(): # functions for different scenarios
    time.sleep(2)
    scoreDown(2)
    Sawyer("Hey there I saw you across the room and thought you were pretty can I have your number?")
    time.sleep(1)
    Her("Sure! You aren't too bad either. Can I sit with you at lunch I don't have friends yet.")
    time.sleep(1)
    Sawyer("No problem you can meet my friends. They're pretty awesome.")
    time.sleep(1)
    Her("Perfect. Hey! Make sure you text me tonight too.")

def LunchTable(): # functions for different scenarios
    time.sleep(2)
    scoreUp(1)
    Sawyer("Wanna sit with us at lunch? My friends thought you seemed cool.")
    time.sleep(1)
    Her("Of course! A little weird, but I'm sure they're normal right?")
    time.sleep(1)
    Sawyer("Normal is a reach, but I like them so surely you will too.")
    time.sleep(2)
    Kasper("She started walking over with Sawyer at lunch and I promise to you I saw you start to sweat and get red!")
    time.sleep(2)
    Choices("1) I did NOT!!!")
    Choices("2) What can I say... I was a little nervous you could say.")
    Choice(nullVar)
    if ans == 1:
        scoreDown(3)
    elif ans == 2:
        scoreUp(1)

if ans == 1:
    LunchTable() # score could be -4 all the way to 3
elif ans == 2:
    AskingforNum()

# Introducing Her to the rest of the friend group
# Save some pee!

def Number(): # Another interaction between characters
    time.sleep(1)
    You("Little did you know Kasper that was hilarious and she gave me a napkin with her number on it!")
    time.sleep(2)
    Kasper("No way! That's not true.")
    time.sleep(1)
    You("I don't lie!")
    scoreUp(1)

def PissJoke(): # A joke I put into the game for my girlfriend that is a little hidden
    time.sleep(2)
    Her("I'm gonna use the bathroom BRB! I like sitting here though I'm not ditching you guys... Promise!")
    Choices("1) Save some for me! In a jar!")
    Choices("2) Good luck... Hope you find your dad!")
    Choice(nullVar)
    if ans == 1:
        scoreUp(2)
        Kasper("Dude... Pause? That isn't even funny it's just weird...")
        Number()
    elif ans == 2:
        Kasper("Dude... Pause? That isn't even funny it's just weird...")
        scoreDown(2)
    time.sleep(1)


def SmoothCriminal(): # Two long functions for the two options
    time.sleep(1)
    Her("Hey there guys I met Sawyer earlier. What are your names?")
    time.sleep(2)
    You("This is Kasper and Markus. Thank you for coming and sitting with us.")
    time.sleep(2)
    Her("Of course. I think I'l keep coming back you all seem really nice.")
    time.sleep(2)
    Markus("Don't you sit next to us in History 2nd period?")
    time.sleep(2)
    You("I knew I remembered seeing her in there!")
    time.sleep(1)
    Her("That was you guys? I couldn't stop laughing in there because of you!")
    time.sleep(2)
    Choices("1) I'll have to get your number to work on that assignment with you later.")
    Choices("2) You know us... We can be funny at times I guess.")
    Choice(nullVar)
    if ans == 2:
        PissJoke()
    elif ans == 1:
        time.sleep(2)
        Kasper("She never gave you her number did she?")
        time.sleep(1)
        Choices("1) Nope. I got it form you that night...")
        Choices("2) I got it. She gave it to me on a napkin when you weren't looking. That little flirt.")
        Choice(nullVar)
        if ans == 2:
            scoreUp(1)
        elif ans == 1:
            scoreDown(4) 

def IsThatFlirting():
    time.sleep(1)
    Her("Hey there guys I met Sawyer earlier. What are your names?")
    time.sleep(2)
    You("This is Kasper and Markus. Thank you for coming and sitting with us.")
    time.sleep(2)
    You("You're really... Sorry I'm nervous right now.")
    time.sleep(2)
    Her("Why is that?")
    time.sleep(1)
    Markus("Yeah kid! Why are you scared?!")
    time.sleep(2)
    Choices("1) I'm not scared she is just really pretty okay?")
    Choices("2) Shut up Markus!")
    Choice(nullVar)
    if ans == 1:
        time.sleep(2)
        Her("That is really sweet. You're very handsome too.")
        time.sleep(3)
        Kasper("WOAH WOAH WOAH! That doesn't sound awful?!")
        time.sleep(1)
        You("Okay maybe that part was a lie. Markus still made fun of me that kinda sucks!")
        time.sleep(2)
        scoreUp(5)
    elif ans == 2:
        scoreDown(4)
        Markus("Calm down buddy... I get she is pretty though.")
        time.sleep(1)
        Markus("Wanna grab food after school?")
        time.sleep(2)
        Her("Of course I will! Call it a date.")
        time.sleep(1)

time.sleep(3)
Kasper("She came over at lunch time to meet all of us and it went well I guess.")
Choices("1) I thought it went really well for me. I am a ladies man.")
Choices("2) Actually... I thought it went awful. I could not talk to her")
Choice(nullVar)
if ans == 1:
    SmoothCriminal()
    time.sleep(2)
elif ans == 2:
    IsThatFlirting() # Score is between -8 and 8 here

# Her telling us about her friends

def Girlfriend():
    time.sleep(3)
    Penelope("She calls you her boyfriend?")
    time.sleep(1)
    You("I haven't asked her out yet.")
    time.sleep(2)
    scoreUp(6)
    Penelope("Well get on that ASAP she really likes you.")
    time.sleep(1)
    You("Okay I will!")
    time.sleep(3)
    Kasper("Well what did you do after that? I forget this part!")
    Choices("1) I walked up to her right then and asked her out!")
    Choices("2) Well I was way too scared I couldn't ask her. I just let her assume.")
    Choice(nullVar)
    if ans == 2:
        scoreDown(2)
        time.sleep(1)
        Kasper("That is soooo LAME!")
        time.sleep(1)
        You("I know it is but whatever it worked didn't it??")
        time.sleep(2)
    elif ans == 1:
        time.sleep(1)
        scoreUp(8)
        You("She said yes!")
        time.sleep(1)
        Kasper("Well obviously! You know where we are right???")


def Friend():
    time.sleep(1)
    Penelope("Oh you aren't Markus are you?")
    time.sleep(1)
    You("No? Who are you?")
    time.sleep(1)
    Penelope("I am Penelope. Markus' girlfriend is my friend.")
    time.sleep(2)
    You("I'm sorry Markus has a girlfriend???")
    time.sleep(3)
    scoreDown(1000)
    Kasper("You should've seen your face!")
    time.sleep(1)
    You("I was so shocked to hear it! But really happy for Markus.")
    time.sleep(2)
    You("Markus you deserve it you two are perfect for each other.")
    time.sleep(1)


Kasper("Flash forward. It is like a month from that day and she sat with us every day at lunch")
time.sleep(2)
You("She had made some friends from volleyball and she was introducing us to them.")
time.sleep(2)
Choices("1) I thought they were nice, and not to mention pretty.")
Choices("2) I didn't think much about them. My eyes were still on her.")
Choice(nullVar)
time.sleep(1)
if ans == 1:
    scoreDown(4)
    Kasper("I knew you liked them a little bit.")
    time.sleep(1)
    Kasper("You were looking at Penelope. I could tell because you kept flirting with her.")
    time.sleep(2)
    Penelope("Hey there! How are you doing?")
    time.sleep(1)
    You("Hey Penelope. I'm great and you look great today too.")
    time.sleep(2)
    Kasper("It was always you and Penelope and never you and Kasper!")
    time.sleep(2)
    You("Whoops!!")
elif ans == 2:
    Kasper("I knew you liked her!")
    You("Well... I can't lie to you I did like her just a little bit")
    time.sleep(2)
    scoreUp(3)
    Penelope("Hey there! I'm Penelope. Your girlfriends like new best friend.")
    time.sleep(1)
    Choices("1) I don't have a girlfriend?")
    Choices("2) Oh! You're her friend? It is fantastic to meet you. Where did you hear 'girlfriend.'")
    Choice(nullVar)
    if ans == 1:
        Friend()
    elif ans == 2:
        Girlfriend()

# Score minimum is -10 maximum is 16 alt ending is -300 or less

# Below are the functions for the ending and the conclusions of the story

def GoodEnding():
    time.sleep(5)
    Kasper("Thank you for letting me be the best man at your wedding by the way guys!")
    time.sleep(2)
    You("Of course!")
    Her("Your speech was perfect. I'd listen to that story a million time over.")
    time.sleep(3)
    Kasper("And that kids is how I met the bride and her beautiful groom!")
    time.sleep(2)
    You("We talked about this you can't keep flirting with me once I'm married.")
    time.sleep(2)
    Sawyer("That's not what you told me last night!")
    time.sleep(3)
    You("Sawyer I said never mention that ever again!")
    time.sleep(2)
    Her("Sorry boys... He's all mine forever and ever. Try again next lifetime!")
    time.sleep(2)
    Markus("Dangit!")
    Sawyer("Rats!")
    Kasper("we will see about that. Nothing can get in the way of true love!")
    time.sleep(4)
    Her("You can fight me for him!")
    time.sleep(1)
    You("Guys not at my wedding please!")
    time.sleep(2)
    Sawyer("Fine.")

def BadEnding():
    time.sleep(5)
    Donovan("Why exactly are you telling me this?")
    time.sleep(3)
    You("Well you need to know our whole back story before you can date our friend? Duh!")
    time.sleep(4)
    Kasper("YEAH")
    Markus("Uh huh!")
    Penelope("That's like totally true!")
    time.sleep(3)
    Her("Thank you for being so grateful and telling Donovan the whole story...")
    time.sleep(3)
    Donovan("We better get out of here before they tell us another story!")
    time.sleep(3)
    Her("You can say that again! Haha!")
    time.sleep(5)
    warning("You then watched the secret love of your life walk out of the door... No one knew how you felt, but it still hurts.")
    time.sleep(2)
    warning("You left those two with one final remark...")
    time.sleep(2)
    You("Have fun you two love birds...")

def AltEnding():
    time.sleep(5)
    Kasper("Thank you Markus for making me your best man at your wedding!")
    time.sleep(2)
    Kasper("From the second I heard you two were dating I knew it was gonna work out.")
    time.sleep(4)
    You("High school sweethearts and what not!")
    time.sleep(3)
    Markus("Thank you guys for being so nice in your speech!")
    time.sleep(3)
    Her("Seriously... We never would've gotten married if not for you.")
    time.sleep(8)
    warning("Flash forward eight years")
    time.sleep(3)
    You("I still haven't forgiven Markus for taking her from me. I'm only slightly kidding about that!")
    You("He knew how I felt!")
    time.sleep(6)

if score >= 8: # The if else statements that compare you score to give you the right ending
    GoodEnding()
elif score <= -300:
    AltEnding()
else:
    BadEnding()

time.sleep(5)
warning("Thank you for playing my short story game! There are a lot of inside jokes for my own enjoyment...")
warning("There are three possible endings try to get all of them.")
print("Your final score is: ")
print(score)
time.sleep(15)