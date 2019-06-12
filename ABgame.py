import random
import os
import csv
import pandas as pd

def csv_write_list(FILENAME,fields,data):
    with open(FILENAME, 'w', newline='') as csvfile:
        # fieldnames = ['name', 'score']
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        for dict in data:
            writer.writerow(dict)

def csv_init(FILENAME,fields):
    with open(FILENAME, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()

def csv_append_list(FILENAME,fields,data):
    with open(FILENAME, 'a', newline='') as csvfile:
        # fieldnames = ['name', 'score']
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
        score = int(row['Score'])
        if score in score_list:
            pass
        else:
            score_list.append(score)
    score_list.sort(reverse=False)

    for row in data:
        score = int(row['Score'])
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
    This is a logical game. The objective is to guess the 4 digits number the computer holds based on clues.
    1) "A" stands for the digits guessed correctly.
    2) "B" stands for the digits guessed correctly, but not in the specific locaton.
    3) The coefficient in front of "A" or "B" stands for how many numbers of each signs.
    Ex: 2A2B means 2 digits were guessed correctly, and the other digits were also guessed correctly, but located in the wrong position.
    SYNTAX LIMITATIONS:
    1) A player can not insert repeated digits.
    2) A player can only insert integers.
    3) A player needed to insert exactly 4 digits.
    * Syntax error do not count in trials. *
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
            score = str(row['Score'])
            rank = str(row['rank'])
            users.append(user)
            scores.append(score)
            ranks.append(rank)
        showing_data = {"Name":users, "Score":scores, "Rank":ranks}
        df = pd.DataFrame(showing_data)
        print(df)
        csv_write_list(FILENAME,fields,data)
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
    '''
    )

def start_game():
    res = ''
    rec = []
    gus = 0
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
            LBD = input("Do you want to record your score?(Y/N)\n: ")
            if LBD == 'Y':
                Name = input("Insert name: ")
                dict = {}
                dict.update({"User":Name,"Score":gus})
                rec.append(dict)
                print(rec)
                csv_append_list(FILENAME,fields,rec)
            break
        if b == 4:
            a = 0
        print(str(a)+"A"+str(b)+"B")

choice = random.randint(1,4)
banner(choice)
secret = ''.join(random.sample("0123456789", 4))
gus = 0
default = None
FILENAME = ".Leaderboard.csv"
fields = ['User', 'Score','rank']
while True:
    f = []
    yes = 0
    f = os.listdir(os.path.abspath(""))
    for file in f:
        print(file)
        if file == ".Leaderboard.csv":
            yes = 1
    if yes == 0:
        csv_init(FILENAME,fields)
    data = csv_read_dict(FILENAME)
    options()
    act = input("\nSelect your choice: ")
    try:
        a = int(act)
        if len(act) >1:
            print(len(act) >1)
            print("Invalid action")
            continue
        elif len(act) == 1:
            if a == 1:
                print("c: 1")
                rules()
                continue
            elif a == 2:
                start_game()
            elif a == 3:
                LdB_core()
                continue
            elif a == 4:
                print("\nThanks for using ABgame.py. See you!\n")
                break
            elif a == 5:
                csv_init(FILENAME, fields)
                print("\nRecord had successfully re-initialized!")
                continue
        else:
            continue
    except:
        if act == 'clear':
            print(chr(27) + "[2J")
            continue
        else:
            print("Invalid action")
