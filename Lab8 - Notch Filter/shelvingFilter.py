import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
from scipy.io.wavfile import read
from scipy.io.wavfile import write


def applyShelvingFilter(inName, outName, g, fc):
    fs, audio = read(inName)
    N = audio.size
    fft = np.fft.fft(audio)[0:int(N / 4)].real
    magn = max(fft)
    plt.ylim(0, magn)
    plt.plot(fft)
    print(fft)
    plt.show()


##########################  main  ##########################
if __name__ == "__main__":
    inName = "P_9_2.wav"
    gain = 5  # can be positive or negative
    # WARNING: small positive values can greatly amplify the sounds
    cutoff = 300
    outName = "shelvingOutput.wav"

    applyShelvingFilter(inName, outName, gain, cutoff)
