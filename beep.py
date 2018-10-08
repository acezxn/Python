import time, sys
from pygame import mixer

def play(str) :
    mixer.init()

    long_sound = mixer.Sound("beep500.wav")
    short_sound = mixer.Sound("beep200.wav")

    for char in str :
        while mixer.get_busy() :
            time.sleep(0.1)

        if char == '-' :
            long_sound.play()
        elif char == '.' :
            short_sound.play()
        elif char == ' ' :
            time.sleep(0.5)
#pygame.mixer.music.load("beep800.wav")
#pygame.mixer.music.play()
#pygame.event.wait()
