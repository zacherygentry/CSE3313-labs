# Zachery Gentry

import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import read
from scipy.io.wavfile import write


def applyShelvingFilter(inName, outName, g, fc):
    fs, audio = read(inName)
    N = audio.size

    # From their docs
    # https://plot.ly/matplotlib/fft/
    k = np.arange(N)
    print(np.max(audio))
    T = N/fs
    frq = k / T
    frq = frq[range(int(N/2))]
    Y = np.fft.fft(audio).real / N
    Y = Y[range(int(N/2))]
    magn = np.max(Y)
    plt.ylim(0, magn + 100)
    plt.subplot(1, 2, 1)
    plt.plot(frq, abs(Y))

    # gain
    mu = 10 ** (g / 20)
    Oc = 2 * np.pi * fc / fs
    num = 1 - ( 4 / ( 1 + mu) ) * np.tan(Oc / 2)
    den = 1 + ( 4 / ( 1 + mu) ) * np.tan(Oc / 2)
    gamma = num / den
    alpha = (1 - gamma) / 2

    u = [0]
    y = []
    for index, x in enumerate(audio):
        if index < 1:
            continue
        
        # u(n) section
        temp = alpha * (x + audio[index - 1])
        if index == 1:
            u.append(temp)
        else:
            temp = temp + gamma * u[index - 1]
            u.append(temp)
        # y(n) section
        temp = x + (mu - 1) * u[index]
        y.append(temp)

    shelvingOutput = np.convolve(audio, y)
    print(shelvingOutput)
    plt.subplot(1, 2, 2)
    Y = np.fft.fft(shelvingOutput).real / N
    Y = Y[range(int(N / 2))]
    magn = np.max(shelvingOutput)
    plt.plot(frq, abs(Y))
    write(outName, fs, shelvingOutput)
    plt.show()


##########################  main  ##########################
if __name__ == "__main__":
    inName = "P_9_1.wav"
    gain = -5  # can be positive or negative
    # WARNING: small positive values can greatly amplify the sounds
    cutoff = 300
    outName = "shelvingOutput.wav"
    applyShelvingFilter(inName, outName, gain, cutoff)
