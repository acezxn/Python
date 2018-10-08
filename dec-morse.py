
import beep
PLAYSOUND = False

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

# Generate Invert Dictionary
WCODE = {value: key for key, value in MCODE.items()}

in_str = input('Morse Code (- . ):')
if PLAYSOUND :
    MorseSound.play(in_str)

words = in_str.replace("  ", ",").split(',')
out_str = ""
for word in words :
    chars = word.split()
    for char in chars :
        try:
            dec = WCODE[char]
            out_str = out_str + dec
        except Exception as e:
            print("error: " + str(e))

    out_str = out_str + " "

print(out_str)
