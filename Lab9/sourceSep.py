# Zachery Gentry

import numpy as np
import soundfile as sf
from scipy import signal
from sklearn.decomposition import FastICA, PCA


def unmixAudio(leftName, rightName):
    left_data, left_fs = sf.read(leftName)
    right_data, right_fs = sf.read(rightName)

    S = np.c_[left_data, right_data]

    ica = FastICA(n_components=2)
    S_ = ica.fit_transform(S)
    S_ *= 10

    sf.write('unmixed0.wav', S_[:,0], left_fs)
    sf.write('unmixed1.wav', S_[:,1], right_fs)
    

###################  main  ###################
if __name__ == "__main__":
    leftName = "darinSiren0.wav"
    rightName = "darinSiren1.wav"
    unmixAudio(leftName, rightName)
