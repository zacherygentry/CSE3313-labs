# Zachery Gentry

import soundfile as sf
import numpy as np

f = sf.SoundFile('twinkle.wav', 'w+', 8000, channels=1, subtype='PCM_24')


def getFrequency(keyNumber):
    return float(440 * np.power(2, (keyNumber - 49)/12))


def writeNote(keyNumber, bassKey=-1, length=.5):
    sample = 8000
    x = np.arange(sample * length)
    y = np.sin(2 * np.pi * getFrequency(keyNumber) * x / sample)
    if bassKey != -1:
        y2 = np.sin(2 * np.pi * getFrequency(bassKey - 24) * x / sample)
    else:
        y2 = 0

    pos = f.tell()
    f.seek(pos)

    f.write(y + y2)


d = {'C': 52, 'D': 54, 'E': 56, 'F': 57, 'G': 59, 'A': 61, 'B': 63}
### M A I N ###
writeNote(d['C'])  # C
writeNote(d['C'])  # C
writeNote(d['G'])  # G
writeNote(d['G'])  # G
writeNote(d['A'])  # A
writeNote(d['A'])  # A
writeNote(d['G'])  # G
writeNote(d['G'])  # G
writeNote(d['F'])  # F
writeNote(d['F'])  # F
writeNote(d['E'])  # E
writeNote(d['E'])  # E

writeNote(d['D'])  # D
writeNote(d['D'])  # D
writeNote(d['E'])  # E
writeNote(d['C'])  # C
writeNote(d['G'])  # G
writeNote(d['G'])  # G
writeNote(d['F'])  # F
writeNote(d['F'])  # F
writeNote(d['E'])  # E
writeNote(d['E'])  # E
writeNote(d['D'])  # D
writeNote(d['D'])  # D
