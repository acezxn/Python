import random
import os
import csv
try:
    from pyfiglet import Figlet
    import pandas as pd
except:
    os.system('pip install pyfiglet')
    os.system('pip install pandas')
    from pyfiglet import Figlet
    import pandas as pd


def poss_gen():
    i = 123
    comb = []
    while i <= 9876:
        if i < 1000:
            temp = '0' + str(i)
        else:
            temp = str(i)
        if len(list(temp)) == len(set(temp)):
            comb.append(temp)
        i = i + 1
    return comb


def compare(q, element):
    A = 0
    B = 0
    for I, L in enumerate(list(q)):
        for i, l in enumerate(list(element)):
            if I == i and L == l:
                A += 1
            elif l == L:
                B += 1
    return A, B


def csv_write_list(FILENAME, fields, data):
    with open(FILENAME, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        for dict in data:
            writer.writerow(dict)


def csv_init(FILENAME, fields):
    with open(FILENAME, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()


def csv_append_list(FILENAME, fields, data):
    with open(FILENAME, 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        for dict in data:
            writer.writerow(dict)


def csv_read_dict(FILENAME):
    users = []
    with open(FILENAME, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            users.append(row)

    return users


def ranking(data):
    score_list = []
    for row in data:
        score = int(row['Trials'])
        if score in score_list:
            pass
        else:
            score_list.append(score)
    score_list.sort(reverse=False)

    for row in data:
        score = int(row['Trials'])
        rank = score_list.index(score) + 1
        row['rank'] = rank


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
    if choice == 4:
        print(
            '''
    ╦  ┬  ┌─┐┬  ┬┌─┐  ┬  ┌─┐┌─┐┬┌─┐
    ║  │  │ │└┐┌┘├┤   │  │ ││ ┬││
    ╩  ┴─┘└─┘ └┘ └─┘  ┴─┘└─┘└─┘┴└─┘
            ╦  ┬  ┌─┐┬  ┬┌─┐  ┬  ┌─┐┌─┐┬┌─┐
            ║  │  │ │└┐┌┘├┤   │  │ ││ ┬││
            ╩  ┴─┘└─┘ └┘ └─┘  ┴─┘└─┘└─┘┴└─┘
                    ╦  ┬  ┌─┐┬  ┬┌─┐  ┬  ┌─┐┌─┐┬┌─┐
                    ║  │  │ │└┐┌┘├┤   │  │ ││ ┬││
                    ╩  ┴─┘└─┘ └┘ └─┘  ┴─┘└─┘└─┘┴└─┘
                            ╦  ┬  ┌─┐┬  ┬┌─┐  ┬  ┌─┐┌─┐┬┌─┐
                            ║  │  │ │└┐┌┘├┤   │  │ ││ ┬││
                            ╩  ┴─┘└─┘ └┘ └─┘  ┴─┘└─┘└─┘┴└─┘
        '''
        )


def rules():
    print(
        '''
    WHAT is ABgame.py???

    This is a logical game. The objective is to guess the 4 digits number the computer holds based on clues.
    1) "A" stands for the digits guessed correctly.
    2) "B" stands for the digits guessed correctly, but not in the specific location.
    3) The coefficient in front of "A" or "B" stands for how many numbers of each sign.
    Ex: 2A2B means 2 digits were guessed correctly, and the other digits were also guessed correctly, but located in the wrong position.

    SYNTAX LIMITATIONS:
    1) A player can not insert repeated digits.
    2) A player can only insert integers.
    3) A player needed to insert exactly 4 digits.
    * Syntax error does not count in trials. *

    If you are already mastered this game, go challenge the Mighty Python. To beat python, you must figure out its secret number first.

    Enjoy, have fun, and have a pleasant journey in logic path~
    '''
    )


def LdB_core():
    try:
        print(
            '''
             _                    _           _                         _
            | |                  | |         | |                       | |_
            | |     ___  __ _  __| | ___ _ __| |__   ___   __ _ _ __ __| (_)
            | |    / _ \/ _` |/ _` |/ _ \ '__| '_ \ / _ \ / _` | '__/ _` |
            | |___|  __/ (_| | (_| |  __/ |  | |_) | (_) | (_| | | | (_| |_
            |______\___|\__,_|\__,_|\___|_|  |_.__/ \___/ \__,_|_|  \__,_(_)
'''
        )
        print("___________________________________________________________")
        data = csv_read_dict(FILENAME)
        ranking(data)
        users = []
        scores = []
        ranks = []
        for row in data:
            user = row['User']
            score = str(row['Trials'])
            rank = str(row['rank'])
            users.append(user)
            scores.append(score)
            ranks.append(rank)
        showing_data = {"Name": users, "Trials": scores, "Rank": ranks}
        df = pd.DataFrame(showing_data)
        print(df)
        csv_write_list(FILENAME, fields, data)
    except Exception as e:
        print(e)


def options():
    print(
        '''
    Actions:
    1) About this game
    2) Start playing
    3) Check leaderboard
    4) Quit
    5) Initialize leaderboard (YOU WILL LOSE ALL RECORDS)
    6) Challenge the Mighty Python
    '''
    )


def start_game(honesty):
    lie = 1 - honesty
    thresh = lie * 10
    res = ''
    rec = []
    gus = 0
    LBD = ''
    secret = ''.join(random.sample("0123456789", 4))
    print("\n4 digits random number GENERATED! ")
    while True:
        rand = random.randint(1, 10)
        res = input("Guess a 4 digits number: ")
        s_char = False
        if len(res) > 4 or len(res) < 4:  # to keep gueses to 4 digits.
            print("Not a 4 digits #! ╭∩╮༼ಠ益ಠ༽ ╭∩╮༼ಠ益ಠ༽")
            continue
        a = 0
        b = 0
        if res == "DANI":  # the backdoor
            print(
                "<:::::[]=¤༼ຈل͜ຈ༽ﾉ  <:::::[]=¤༼ຈل͜ຈ༽ﾉ\nGot the backdoor key? The number is " + secret)
            break
        try:  # to keep guess an integer
            intr = int(res)
            intr = None
        except:
            print("Not a 4 digits #! ╭∩╮༼ಠ益ಠ༽ ╭∩╮༼ಠ益ಠ༽")
            continue
        if len(res) > len(set(res)):  # to avoid guess from repeating digits.
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
                elif al == AL:
                    b += 1
        if a == 4:
            b = 0
            print("Correct  ヽ༼ຈل͜ຈ༽ﾉ︵┻━┻")
            print("You took " + str(gus) + " gueses!")
            LBD = input("Do you want to record your score?(Y/N)\n: ")
            while True:
                if LBD == 'Y' or LBD == 'y':
                    Name = input("Insert name: ")
                    dict = {}
                    dict.update({"User": Name, "Trials": gus})
                    rec.append(dict)
                    csv_append_list(FILENAME, fields, rec)
                    break
                elif LBD == 'N' or LBD == 'n':
                    break
                else:
                    continue
            break

        elif rand <= thresh:
            print(str(random.randint(0, 2)) + 'A' +
                  str(random.randint(0, 2)) + 'B')
            continue
        if b == 4:
            a = 0
        print(str(a) + "A" + str(b) + "B")


def Masterpy():
    total_poss = []
    total_poss = poss_gen()
    total = []
    total += total_poss
    trials = 0
    res = ''
    gus = 0
    turn = 1
    secret = ''.join(random.sample("0123456789", 4))
    guss = {}
    print(chr(27) + "[2J")
    print('''

                                         .o@*hu
                  ..      .........   .u*"    ^Rc
                oP""*Lo*#"""""""""""7d" .d*N.   $
               @  u@""           .u*" o*"   #L  ?b
              @   "              " .d"  .d@@e$   ?b.
             8                    @*@me@#         '"Nu
            @                                        '#b
          .P                                           $r
        .@"                                  $L        $
      .@"                                   8"R      dP
   .d#"                                  .dP d"   .d#
  xP              .e                 .ud#"  dE.o@"(
  $             s*"              .u@*""     '""\dP"
  ?L  ..                    ..o@""        .$  uP
   #c:$"*u.             .u@*""$          uR .@"
    ?L$. '"""***Nc    x@""   @"         d" JP
     ^#$.        #L  .$     8"         d" d"
       '          "b.'$.   @"         $" 8"
                   '"*@$L $"         $  @
                   @L    $"         d" 8\

                   $ """   o      dP xR
                   $      dFNu...@"  $
                   "N..   ?B ^"""   :R
                     """"* RL       d>
                            "$u.   .$
                              ^"*bo@"

    ''')
    print("\n4 digits random number GENERATED! ")
    win = False
    while True:
        Your_ans = input('Enter your secret number: ')
        s_char = False
        # to keep gueses to 4 digits.
        if len(Your_ans) > 4 or len(Your_ans) < 4:
            print("Not a 4 digits #! ╭∩╮༼ಠ益ಠ༽ ╭∩╮༼ಠ益ಠ༽")
            continue
        a = 0
        b = 0
        try:  # to keep guess an integer
            intr = int(Your_ans)
            intr = None
        except:
            print("Not a 4 digits #! ╭∩╮༼ಠ益ಠ༽ ╭∩╮༼ಠ益ಠ༽")
            continue
        # to avoid guess from repeating digits.
        if len(Your_ans) > len(set(Your_ans)):
            print("Digits can not be repeated!! （͡°͜ʖ͡°）")
            continue
        for i in Your_ans:
            if i == "-" or i == "_" or i == "+" or i == "=":
                print("Insert digits!!!")
                s_char = True
                break
        if s_char:
            continue
        else:
            break
    while not win:
        if turn % 2 != 0:
            while True:
                res = input("\nGuess a 4 digits number: ")
                s_char = False
                if len(res) > 4 or len(res) < 4:  # to keep gueses to 4 digits.
                    print("Not a 4 digits #! ╭∩╮༼ಠ益ಠ༽ ╭∩╮༼ಠ益ಠ༽")
                    continue
                a = 0
                b = 0
                if res == "DANI":  # the backdoor
                    print(
                        "<:::::[]=¤༼ຈل͜ຈ༽ﾉ  <:::::[]=¤༼ຈل͜ຈ༽ﾉ\nGot the backdoor key? The number is " + secret)
                    break
                try:  # to keep guess an integer
                    intr = int(res)
                    intr = None
                except:
                    print("Not a 4 digits #! ╭∩╮༼ಠ益ಠ༽ ╭∩╮༼ಠ益ಠ༽")
                    continue
                # to avoid guess from repeating digits.
                if len(res) > len(set(res)):
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
                a, b = compare(res, secret)
                if a == 4:
                    print('''

                                         .o@*hu
                  ..      .........   .u*"    ^Rc
                oP""*Lo*#"""""""""""7d"         $
               @  u@""                 @@    @@ ?b
              @   "                       @@     ?b.
             8                            @@        '"Nu
            @                          @@    @@      '#b
          .P                                           $r
        .@"                                  $L        $
      .@"                                   8"R      dP
   .d#"                                  .dP d"   .d#
  xP              .e                 .ud#"  dE.o@"(
  $             s*"              .u@*""     '""\dP"
  ?L  ..                    ..o@""        .$  uP
   #c:$"*u.             .u@*""$          uR .@"
    ?L$. '"""***Nc    x@""   @"         d" JP
     ^#$.        #L  .$     8"         d" d"
       '          "b.'$.   @"         $" 8"
                   '"*@$L $"         $  @
                   @L    $"         d" 8\

                   $ """   o      dP xR
                   $      dFNu...@"  $
                   "N..   ?B ^"""   :R
                     """"* RL       d>
                            "$u.   .$
                              ^"*bo@"

                    ''')
                    print('You beated python for {} trials!'.format(gus))
                    win = True
                    break
                print(f'{a}A{b}B')
                turn += 1
                break

        else:
            A = 0
            B = 0
            a = 0
            trials += 1
            q = random.choice(total)
            print('\nPython: {}'.format(q))
            a, b = compare(Your_ans, q)
            print(f'{a}A{b}B')
            if a == 4:
                print(chr(27) + "[2J")
                print('''

████████▄     ▄████████    ▄████████    ▄████████    ▄████████     ███
███   ▀███   ███    ███   ███    ███   ███    ███   ███    ███ ▀█████████▄
███    ███   ███    █▀    ███    █▀    ███    █▀    ███    ███    ▀███▀▀██
███    ███  ▄███▄▄▄      ▄███▄▄▄      ▄███▄▄▄       ███    ███     ███   ▀
███    ███ ▀▀███▀▀▀     ▀▀███▀▀▀     ▀▀███▀▀▀     ▀███████████     ███
███    ███   ███    █▄    ███          ███    █▄    ███    ███     ███
███   ▄███   ███    ███   ███          ███    ███   ███    ███     ███
████████▀    ██████████   ███          ██████████   ███    █▀     ▄████▀

                ''')
                custom_fig = Figlet(font='big')
                print(custom_fig.renderText('                          ' + q))
                print(
                    "\nComputer wins with {} trials! Try again next time~".format(trials))
                break
            total.remove(q)
            i = 0
            while i <= len(total) - 1:
                element = total[i]
                A, B = compare(q, element)
                if A != a or B != b:  # if the condition is not the same
                    total.remove(element)
                    i = i - 1
                    #print("deleted: {}".format(element))
                i = i + 1
            turn += 1


choice = random.randint(1, 4)
print(chr(27) + "[2J")
banner(choice)
secret = ''.join(random.sample("0123456789", 4))
gus = 0
default = None
FILENAME = ".Leaderboard.csv"
fields = ['User', 'Trials', 'rank']
while True:
    f = []
    yes = 0
    f = os.listdir(os.path.abspath(""))
    for file in f:
        if file == ".Leaderboard.csv":
            yes = 1
    if yes == 0:
        csv_init(FILENAME, fields)
    data = csv_read_dict(FILENAME)
    options()
    act = input("\nSelect your choice: ")
    try:
        a = int(act)
        if len(act) > 1:
            print(chr(27) + "[2J")
            print("Invalid action")
            continue
        elif len(act) == 1:
            if a == 1:
                print(chr(27) + "[2J")
                rules()
                continue
            elif a == 2:
                honesty = float(
                    input('Insert honsety number (0 is for all lying, 1 is for all honest): '))
                print(chr(27) + "[2J")
                start_game(honesty)
            elif a == 3:
                print(chr(27) + "[2J")
                LdB_core()
                continue
            elif a == 4:
                print("\nThanks for using ABgame.py. See you!\n")
                break
            elif a == 5:
                print(chr(27) + "[2J")
                csv_init(FILENAME, fields)
                print("\nRecord had successfully re-initialized!")
                continue
            elif a == 6:
                Masterpy()
            else:
                print(chr(27) + "[2J")
                print("Invalid action")
                continue
        else:
            continue
    except Exception as e:
        if act == 'clear':
            print(chr(27) + "[2J")
            continue
        else:
            print("Invalid action: " + str(e))
