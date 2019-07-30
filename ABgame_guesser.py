import random
def poss_gen():
    i = 123
    comb = []
    while i <= 9876:
        if i < 1000:
            temp = '0'+str(i)
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
total = []
total = poss_gen()
print('initial possibilities: {}'.format(len(total)))
ans = input('Pick your secret number: ')
A = 0
B = 0
trials = 0
a = 0
while a != 4:
    trials += 1
    q = random.choice(total)
    print("Computer guessed: {}".format(q))
    a,b = compare(ans, q)
    if a == 4:
        print("\nComputer wins with {} trials!".format(trials))
        break
    print(str(a)+'A'+str(b)+'B')
    print("{} trials with {} possibilities".format(trials, len(total)))
    total.remove(q)
    i = 0
    while i <= len(total)-1:
        element = total[i]
        A,B = compare(q, element)
        if a != 0 or b != 0: # if the guess have possible answer
            if A != a or B != b: # if the condition is not the same
                total.remove(element)
                i = i - 1
                #print("deleted: {}".format(element))
        i = i + 1
