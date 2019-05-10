# Zachery Gentry
# this was difficult

import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import read
from scipy.io.wavfile import write
from scipy import signal


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
    plt.title("original")
    plt.xlabel('Hz')
    plt.plot(frq, abs(Y))

    # gain
    newAudio = shelvingFilter(g, fc, fs, audio)
    print(audio)
    print(newAudio)
    Y = np.fft.fft(newAudio).real / N
    Y = Y[range(int(N / 4))]
    magn2 = np.max(Y)

    if magn1 > magn2:
        magn = magn1
    else:
        magn = magn2
    plt.ylim(0, magn + 100)
    plt.subplot(1, 2, 2)
    plt.title('filtered signal')
    plt.xlabel('Hz')
    plt.ylim(0, magn + 100)
    plt.plot(frq, abs(Y))

    write(outName, fs, newAudio)
    plt.show()


def shelvingFilter(g, fc, fs, audio):
    mu = 10 ** (g / 20)
    thetac = 2 * np.pi * fc / fs
    num = 1 - (4 / (1 + mu)) * np.tan(thetac / 2)
    den = 1 + (4 / (1 + mu)) * np.tan(thetac / 2)
    gamma = num / den
    alpha = (1 - gamma) / 2

    u = np.array([0], dtype='int16')
    y = np.array([0], dtype='int16')
    for index, x in enumerate(audio):
        if index == 0:
            continue
        u1 = alpha * (x + np.int32(audio[index - 1]))
        u2 = gamma * u[index - 1]
        utemp = np.int16(u1 + u2)
        u = np.append(u, utemp)

        ytemp = np.int16(x + (mu - 1) * u[index])
        y = np.append(y, ytemp)

    return y


##########################  main  ##########################
if __name__ == "__main__":
    inName = "P_9_1.wav"
    gain = 5  # can be positive or negative
    # WARNING: small positive values can greatly amplify the sounds
    cutoff = 300
    outName = "shelvingOutput.wav"
    applyShelvingFilter(inName, outName, gain, cutoff)
