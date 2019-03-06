# Zachery Gentry

from scipy.io.wavfile import read
from scipy.io.wavfile import write
from scipy.signal import freqz
import matplotlib.pyplot as plt
import numpy as np



def createLowpassFilter(f_cutoff, fs):
    f_normalized = f_cutoff / fs
    L = 101
    M = L - 1
    fil = np.empty(L)
    for n in range(0, L):
        if(n == M / 2):
            fil[n] = 2 * f_normalized
        else:
            top = np.sin(2*np.pi*f_normalized*(n - M / 2))
            bot = np.pi * (n - M / 2)
            fil[n] = top / bot
    return fil


def createHammingWindow():
    L = 101
    M = L - 1
    fil = np.empty(L)
    for n in range(0, L):
        fil[n] = .54 - .46 * np.cos((2 * np.pi * n) / M)
    return fil


def applyFilter(audio, filt, fs):
    cleanMusic = np.convolve(filt, audio)    
    cleanMusic = np.array(cleanMusic, dtype="int16") # If this isn't set to int16 then OWWWWWW. RIP ears
    write("cleanMusic.wav", fs, cleanMusic)


### M A I N ###
fs, audio = read("P_9_2.wav")


lf = createLowpassFilter(7500, fs)  # Create lowpass filter with 7500Hz cutoff
hw = createHammingWindow()  # Create hamming window

x, y = freqz(lf, 1)  # Plot original filter
plt.plot(x, abs(y), label="original")

# Get new filter with hamming window applied to lowpass filter
filt = np.multiply(lf, hw)

x, y = freqz(filt, 1)  # Plot filter with the window applied
plt.plot(x, abs(y), label="windowed")


applyFilter(audio, filt, fs)

plt.legend(loc='upper right')
plt.title("Frequency Response")
# plt.show()
