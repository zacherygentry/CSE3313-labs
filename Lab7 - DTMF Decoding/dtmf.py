# Zachery Gentry

from scipy.signal import freqz
import numpy as np
import matplotlib.pyplot as plt
import csv
from scipy.signal import spectrogram


def processTones(name, L, fs, samplesPerTone):

    filters = createFilterDictionary(
        [1209, 1336, 1477, 697, 770, 852, 941], L, fs)
    data = readCSV(name, samplesPerTone)

    means = {}
    number = ""
    for d in data:
        means = {}
        for filt in filters:
            out = np.convolve(d, filters[filt])
            means[filt] = np.mean(out ** 2)
        max1, max2 = getMaximums(means)
        number += getDigit(max1, max2)
    plt.show()
    return number


def getMaximums(means):
    max1 = max(means, key=means.get)
    means.pop(max1)
    max2 = max(means, key=means.get)
    return max1, max2


def getDigit(key1, key2):
    digitDict = createFrozenSet()
    return digitDict[frozenset((key1, key2))]


def createFrozenSet():
    digitDict = {}
    digitDict[frozenset((1209, 697))] = '1'
    digitDict[frozenset((1209, 770))] = '4'
    digitDict[frozenset((1209, 852))] = '7'
    digitDict[frozenset((1209, 941))] = '*'
    digitDict[frozenset((1336, 697))] = '2'
    digitDict[frozenset((1336, 770))] = '5'
    digitDict[frozenset((1336, 852))] = '8'
    digitDict[frozenset((1336, 941))] = '0'
    digitDict[frozenset((1477, 697))] = '3'
    digitDict[frozenset((1477, 770))] = '6'
    digitDict[frozenset((1477, 852))] = '9'
    digitDict[frozenset((1477, 941))] = '#'
    return digitDict


def readCSV(name, samplesPerTone):
    with open(name) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            rawData = [float(col) for col in row]
            plt.figure(1)
            plt.ylabel('Frequency [Hz]')
            plt.xlabel('Time [sec]')
            f, t, Sxx = spectrogram(np.asarray(rawData), 8000)
            plt.pcolormesh(t, f, Sxx)
    data = [[] for _ in range(int(len(row) / samplesPerTone))]
    for index, col in enumerate(row):
        data[int(index / samplesPerTone)].append(float(col))
    return np.asarray(data)


def produceFilter(freq, L, fs):
    h = []
    for n in range(L):
        coefficient = 2 / L
        coefficient *= np.cos((2 * np.pi * freq * n) / fs)
        h.append(coefficient)
    return np.asarray(h)


def createFilterDictionary(frequencies, L, fs):
    filters = {}
    plt.figure(0)
    plt.xlabel('Hertz')
    plt.suptitle('Frequency Responses of Bandpass Filters')
    for freq in frequencies:
        filters[freq] = produceFilter(freq, L, fs)
        x, y = freqz(filters[freq], fs=fs)
        plt.plot(x, abs(y))
    return filters


#############  main  #############
if __name__ == "__main__":
    filename = "tones-123456789star0pound.csv"  # name of file to process
    L = 64  # filter length
    fs = 8000  # sampling rate
    samplesPerTone = 4000  # 4000 samples per tone,
    #    NOT the total number of samples per signal

    # returns string of telephone buttons corresponding to tones
    phoneNumber = processTones(filename, L, fs, samplesPerTone)

    print(phoneNumber)
