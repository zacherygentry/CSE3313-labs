# Zachery Gentry

import numpy as np
import matplotlib.pyplot as plt


def createLowpassFilter(f_cutoff, fs=2000):
    f_normalized = f_cutoff / fs
    L = 21
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


def createHighPassFilter(f_cutoff, fs=2000):
    f_normalized = f_cutoff / fs
    L = 21
    M = L - 1
    fil = np.empty(L)
    for n in range(0, L):
        if(n == M / 2):
            fil[n] = 1 - 2 * f_normalized
        else:
            top = -1 * np.sin(2*np.pi*f_normalized*(n - M / 2))
            bot = np.pi * (n - M / 2)
            fil[n] = top / bot
    return fil


### M A I N ###
data = np.genfromtxt('data-filtering.csv', delimiter=',')

fs = 2000
x = np.arange(0, fs, 1)

plt.figure(0)
plt.subplot(3, 1, 1)
plt.title("Original Signal")
plt.plot(x, data)

f = 4
y = np.cos(2*np.pi*f*x/fs)
plt.subplot(3, 1, 2)
plt.title("4 Hz Signal")
plt.plot(x, y)

low_pass = createLowpassFilter(50)
result = np.convolve(data, low_pass)

x = np.arange(0, len(result), 1)
plt.subplot(3, 1, 3)
plt.title("application of lowpass filter")
plt.plot(x, result)
plt.tight_layout()


x = np.arange(0, 100, 1)

plt.figure(1)
plt.subplot(3, 1, 1)
plt.title("original signal")
plt.plot(x, data[0:100])

f = 330
y = np.cos(2*np.pi*f*x/fs)
plt.subplot(3, 1, 2)
plt.title("330 Hz signal")
plt.plot(x, y[0:100])

high_pass = createHighPassFilter(280)
result = np.convolve(data, high_pass)

x = np.arange(0, 100, 1)
plt.subplot(3, 1, 3)
plt.title("application of highpass filter")
plt.plot(x, result[0:100])

plt.tight_layout()

plt.show()
