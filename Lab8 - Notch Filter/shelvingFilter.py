# Zachery Gentry

import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import read
from scipy.io.wavfile import write
from scipy.signal import lfilter


def applyShelvingFilter(inName, outName, g, fc):
    fs, audio = read(inName)
    N = audio.size

    # From their docs
    # https://plot.ly/matplotlib/fft/
    k = np.arange(N)
    T = N/fs
    frq = k / T
    frq = frq[range(int(N/4))]
    Y = np.fft.fft(audio).real / N
    Y = Y[range(int(N/4))]
    magn1 = np.max(Y)
    plt.subplot(1, 2, 1)
    plt.plot(frq, abs(Y))

    # gain
    b, a = shelvingFilter(g, fc, fs)
    newAudio = lfilter(b, a, audio)
    Y = np.fft.fft(newAudio).real / N
    Y = Y[range(int(N / 4))]
    magn2 = np.max(Y)

    if magn1 > magn2:
        magn = magn1
    else:
        magn = magn2
    plt.ylim(0, magn + 100)
    plt.subplot(1, 2, 2)
    plt.ylim(0, magn + 100)
    plt.plot(frq, abs(Y))

    write(outName, fs, newAudio)
    plt.show()


def shelvingFilter(g, fc, fs):
    K = np.tan((np.pi * fc)/fs)
    V0 = 10 ** (g / 20)
    root2 = np.sqrt(2)

    if V0 < 1:
        V0 = 1/V0

    if g > 0:
        b0 = (V0 + root2*np.sqrt(V0)*K + K**2) / (1 + root2*K + K**2)
        b1 = (2 * (K**2 - V0)) / (1 + root2*K + K**2)
        b2 = (V0 - root2*np.sqrt(V0)*K + K**2) / (1 + root2*K + K**2)
        a1 = (2 * (K**2 - 1)) / (1 + root2*K + K**2)
        a2 = (1 - root2*K + K**2) / (1 + root2*K + K**2)
    elif g < 0:
        b0 = (1 + root2*K + K**2) / (V0 + root2*np.sqrt(V0)*K + K**2)
        b1 = (2 * (K**2 - 1)) / (V0 + root2*np.sqrt(V0)*K + K**2)
        b2 = (1 - root2*K + K**2) / (V0 + root2*np.sqrt(V0)*K + K**2)
        a1 = (2 * ((K**2)/V0 - 1)) / (1 + root2/np.sqrt(V0)*K + (K**2)/V0)
        a2 = (1 - root2/np.sqrt(V0)*K + (K**2)/V0) / \
            (1 + root2/np.sqrt(V0)*K + (K**2)/V0)
    else:
        b0 = V0
        b1 = 0
        b2 = 0
        a1 = 0
        a2 = 0

    b = [b0, b1, b2]
    a = [1, a1, a2]

    return b, a


##########################  main  ##########################
if __name__ == "__main__":
    inName = "P_9_1.wav"
    gain = 2  # can be positive or negative
    # WARNING: small positive values can greatly amplify the sounds
    cutoff = 300
    outName = "shelvingOutput.wav"
    applyShelvingFilter(inName, outName, gain, cutoff)
