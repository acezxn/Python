import beep
PLAYSOUND = False
Continue = True
MCODE = {
    'A': '.-',     'B': '-...',   'C': '-.-.',
    'D': '-..',    'E': '.',      'F': '..-.',
    'G': '--.',    'H': '....',   'I': '..',
    'J': '.---',   'K': '-.-',    'L': '.-..',
    'M': '--',     'N': '-.',     'O': '---',
    'P': '.--.',   'Q': '--.-',   'R': '.-.',
    'S': '...',    'T': '-',      'U': '..-',
    'V': '...-',   'W': '.--',    'X': '-..-',
    'Y': '-.--',   'Z': '--..',
    '0': '-----',  '1': '.----',  '2': '..---',
    '3': '...--',  '4': '....-',  '5': '.....',
    '6': '-....',  '7': '--...',  '8': '---..',
    '9': '----.',
    ' ': ' '
    }


while Continue:
    ac = input("Do you want to play sound? Y(yes)/ N(no)/ X(exit)")
    if ac == "Y" or ac == "y":
        PLAYSOUND = True
        Continue = True
    elif ac == "N" or ac == "n":
        PLAYSOUND = False
        Continue = True
    elif ac == "X" or ac == "x":
        Continue = False

    if Continue == True:
        in_str = input('MESSAGE(A-Z, 0-9):')
        out_str = ""

        for char in in_str:
            try:
                enc = MCODE[char.upper()]
                out_str = out_str + enc + " "
            except Exception as e:
                print("error: " + str(e))

        print(out_str)
        if PLAYSOUND :
            beep.play(out_str)
