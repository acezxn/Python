import random
secret = ''.join(random.sample("0123456789", 4))
gus = 0
#print(secret)
print("     /\  \         /\  \    ")
print("    /::\  \       /::\  \   ")
print("   /:/\:\  \     /:/\:\  \  ")
print("  /::\~\:\  \   /::\~\:\__\ ")
print(" /:/\:\ \:\__\ /:/\:\ \:|__|")
print(" \/__\:\/:/  / \:\~\:\/:/  /")
print("      \::/  /   \:\ \::/  / ")
print("      \::/  /   \:\ \::/  / ")
print("      /:/  /     \:\/:/  /  ")
print("     /:/  /       \::/__/   ")
print("     \/__/         ~~       ")
res = -1
secret = ''.join(random.sample("0123456789", 4))
#print(secret)
print("\n4 digits random number GENERATED! ")
while True:
    res = input("Guess a 4 digits number: ")
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
