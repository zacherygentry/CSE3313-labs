# Zachery Gentry

import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt


def processFile(fn, offset):
    data, samplerate = sf.read(fn)

    altered_data = np.asarray(np.fft.fft(data))
    n = altered_data.size

    # For even list only, grabs left hand side of midpoint
    midpoint = int(n / 2) - 1
    altered_data[midpoint - offset + 1: midpoint + 1] = 0
    altered_data[midpoint + 1: midpoint + 1 + offset] = 0
    altered_data = np.fft.ifft(altered_data).real

    plt.subplot(1, 2, 1)
    plt.plot(data)
    plt.subplot(1, 2, 2)
    plt.plot(altered_data)
    plt.show()

    sf.write('cleanMusic.wav', altered_data, samplerate)


##############  main  ##############
if __name__ == "__main__":
    filename = "P_9_2.wav"
    offset = 10000

    # this function should be how your code knows the name of
    #   the file to process and the offset to use
    processFile(filename, offset)
