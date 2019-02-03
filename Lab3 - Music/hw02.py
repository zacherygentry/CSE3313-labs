# Zachery Gentry

import soundfile as sf
import numpy as np

f = sf.SoundFile('twinkle.wav', 'w+', 8000, channels=1, subtype='PCM_24')


def getFrequency(keyNumber):
    return float(440 * np.power(2, (keyNumber - 49)/12))


def writeNote(keyNumber, length=.5):
    sample = 8000
    x = np.arange(sample * length)
    freq = getFrequency(keyNumber)
    y = np.sin(2 * np.pi * freq * x / sample)
    
    pos = f.tell()
    f.seek(pos)

    f.write(y)



### M A I N ###
writeNote(52) # C
writeNote(52) # C
writeNote(59) # G
writeNote(59) # G
writeNote(61) # A
writeNote(61) # A
writeNote(59) # G
writeNote(59) # G
writeNote(57) # F
writeNote(57) # F
writeNote(56) # E
writeNote(56) # E

writeNote(54) # D
writeNote(54) # D
writeNote(56) # E
writeNote(52) # C
writeNote(59) # G
writeNote(59) # G
writeNote(57) # F
writeNote(57) # F
writeNote(56) # E
writeNote(56) # E
writeNote(54) # D
writeNote(54) # D

