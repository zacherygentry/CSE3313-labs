# Zachery Gentry

import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import norm
import soundfile as sf
from scipy.signal import spectrogram
import glob
import math


def classifyMusic():
    fileNames = glob.glob('song-*.wav')

    database = {}
    dataDict = {}

    # loop through filesnames of song-* format to extract their signatures
    for fileName in fileNames:
        data, fs = sf.read(fileName)
        dataDict[fileName] = data
        f, t, Sxx = spectrogram(data, fs, nperseg=fs//2)

        database[fileName] = createSignature(Sxx, f)

    # grab signature of the test song
    testData, testFs = sf.read('testSong.wav')
    f, t, Sxx = spectrogram(testData, testFs, nperseg=fs//2)
    testSignature = createSignature(Sxx, f)

    # find the difference norm between the test song signature and each signature in our database
    similarity = []
    for key in database:
        norm = np.linalg.norm(database[key] - testSignature, ord=1)
        similarity.append([norm, key])

    similarity = sorted(similarity, key=lambda x: x[0])

    # print top 5 songs that match
    for song in similarity[:5]:
        print('{0:.0f}  {1}'.format(song[0], song[1]))

    # testSong.wav spectrogram
    plt.figure(0)
    plt.title("Test Song")
    plt.specgram(testData, Fs=testFs)

    # first closest match spectrogram
    plt.figure(1)
    plt.title("First closest match")
    data, fs = sf.read(similarity[0][1])
    plt.specgram(data, Fs=fs)

    # Second closest match spectrogram
    plt.figure(2)
    plt.title("Second closest match")
    data, fs = sf.read(similarity[1][1])
    plt.specgram(data, Fs=fs)

    plt.show()

def createSignature(s, f):
    signature = []
    for column in s.T:
        signature.append(f[np.argmax(column)])
    return np.asarray(signature)


###################  main  ###################
if __name__ == "__main__":
    classifyMusic()
