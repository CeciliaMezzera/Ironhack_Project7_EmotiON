import time
from pygame import mixer

def play(soundfile, duration_secs):
    """Play a soundfile for defined duration"""
    mixer.init()
    mixer.music.load(soundfile)
    mixer.music.play()
    time.sleep(duration_secs)
    mixer.music.stop()
    mixer.quit()
    return 

# play('1647456249_neutral/neutral.mp3', 5)
