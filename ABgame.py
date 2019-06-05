import random
secret = ''.join(random.sample("0123456789", 4))
gus = 0
#print(secret)
choice = random.randint(1,3)
def banner(choice):
    if choice == 1:
        print(
        '''
           ▄████████ ▀█████████▄
          ███    ███   ███    ███
          ███    ███   ███    ███
          ███    ███  ▄███▄▄▄██▀
        ▀███████████ ▀▀███▀▀▀██▄
          ███    ███   ███    ██▄
          ███    ███   ███    ███
          ███    █▀  ▄█████████▀

        ''')
    if choice == 2:
        print(
        '''
        ▄• ▄▌.▄▄ · ▄▄▄ .
        █▪██▌▐█ ▀. ▀▄.▀·
        █▌▐█▌▄▀▀▀█▄▐▀▀▪▄
        ▐█▄█▌▐█▄▪▐█▐█▄▄▌
        ▀▀▀  ▀▀▀▀  ▀▀▀
        ▄▄▌         ▄▄ • ▪   ▄▄·
        ██•  ▪     ▐█ ▀ ▪██ ▐█ ▌▪
        ██▪   ▄█▀▄ ▄█ ▀█▄▐█·██ ▄▄
        ▐█▌▐▌▐█▌.▐▌▐█▄▪▐█▐█▌▐███▌
        .▀▀▀  ▀█▄▀▪·▀▀▀▀ ▀▀▀·▀▀▀

        ▀
        ''')
    if choice == 3:
        print(
        '''
██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗██╗
██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝██║
██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗  ██║
██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝  ╚═╝
╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗██╗
 ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝╚═╝
        '''
        )
banner(choice)
while True:
    print(
    '''
    Actions:
    1) About this game
    2) Start playing
    3) Quit
    '''
    )
    act = input("\nSelect your choice: ")
    print(act)
    if len(act) >1:
        print("Invalid action")
        continue
    elif act == '1':
        print(
        '''
        This is a logical game. The objective is to guess the 4 digits number the computer holds based on cluesself.
        1) "A" stands for the digits guessed correctly.
        2) "B" stands for the digits guessed correctly, but not in the specific locaton.
        3) The coefficient in front of "A" or "B" stands for how many numbers of each signs.

        Ex: 2A2B means 2 digit guessed correctly, and the other digits also guessed correctly, but located in the wrong position.

        SYNTAX LIMITATIONS:
        1) A player can not insert repeated digits.
        2) A player can only insert integers.
        3) A player needed to insert exactly 4 digits.

        * Syntax error do not count in trials.

        Enjoy, have fun, and have a pleasant journey in logic path~
        '''
        )
        continue
    elif act == '2':
        pass
    elif act == '3':
        print("\nThanks for using ABgame.py. See you!\n")
        break
    res = ''
    secret = ''.join(random.sample("0123456789", 4))
    #print(secret)
    print("\n4 digits random number GENERATED! ")
    while True:
        res = input("Guess a 4 digits number: ")
        s_char = False
        if len(res) > 4 or len(res) < 4: #to keep gueses to 4 digits.
            print("Not a 4 digits #! ╭∩╮༼ಠ益ಠ༽ ╭∩╮༼ಠ益ಠ༽")
            continue
        sI = []
        a = 0
        b = 0
        if res == "DANI": #the backdoor
            print("<:::::[]=¤༼ຈل͜ຈ༽ﾉ  <:::::[]=¤༼ຈل͜ຈ༽ﾉ\nGot the backdoor key? The number is "+secret)
            break
        try: #to keep guess an integer
            intr = int(res)
            intr = None
        except:
            print("Not a 4 digits #! ╭∩╮༼ಠ益ಠ༽ ╭∩╮༼ಠ益ಠ༽")
            continue
        if len(res) > len(set(res)): #to avoid guess from repeating digits.
            print("Digits can not be repeated!! （͡°͜ʖ͡°）")
            continue
        for i in res:
            if i == "-" or i == "_" or i == "+" or i == "=":
                print("Insert digits!!!")
                s_char = True
                break
        if s_char:
            continue
        gus += 1
        for i, al in enumerate(list(str(secret))):
            for I, AL in enumerate(list(res)):
                if I == i and al == AL:
                    a += 1
                    sI.append(AL)
                elif al == AL:
                    if AL not in sI:
                        b += 1
                        sI.append(AL)
        if a == 4:
            b = 0
            print("Correct  ヽ༼ຈل͜ຈ༽ﾉ︵┻━┻")
            print("You took "+str(gus)+" gueses!")
            break
        if b == 4:
            a = 0
        print(str(a)+"A"+str(b)+"B")
