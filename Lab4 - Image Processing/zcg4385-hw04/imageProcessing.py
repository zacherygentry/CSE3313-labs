# Zachery Gentry

import matplotlib.pyplot as plt
from matplotlib.colors import NoNorm
import matplotlib.image as mpimg
import numpy as np
from scipy import ndimage
from PIL import Image

boat = np.array(Image.open("boat.512.tiff"))
clock = np.array(Image.open("clock-5.1.12.tiff"))
darin = np.array(Image.open("darinGrayNoise.jpg"))
man = np.array(Image.open("man-5.3.01.tiff"))
tank = np.array(Image.open("tank-7.1.07.tiff"))


def lowpass_filter(img, n=10):
    m = np.ones(n)/n
    result_array = np.empty((len(img), len(img[0])))
    for index, row in enumerate(img):
        result = np.convolve(row, m)
        result_array[index] = result[4: len(result) - 5]
    return result_array


def highpass_filter(img):
    m = np.array([1, -1])
    result_array = np.empty((len(img), len(img[0])))
    for index, row in enumerate(img):
        result = np.convolve(row, m)
        result_array[index] = result[1: len(result)]
    return result_array


count = 0


def display_pic(arr, title):
    global count
    plt.figure(count)
    plt.title(title)
    plt.imshow(arr)
    count += 1


def display_originals():
    display_pic(boat, "Boat - Original")
    display_pic(clock, "Clock - Original")
    display_pic(man, "Man - Original")
    display_pic(tank, "Tank - Original")


def display_lowpass():
    arr = lowpass_filter(boat)
    display_pic(arr, "Boat - Lowpass Filter")

    arr = lowpass_filter(clock)
    display_pic(arr, "Clock - Lowpass Filter")

    arr = lowpass_filter(man)
    display_pic(arr, "Man - Lowpass Filter")

    arr = lowpass_filter(tank)
    display_pic(arr, "Tank - Lowpass Filter")


def display_highpass():
    arr = highpass_filter(boat)
    display_pic(arr, "Boat - Highpass Filter")

    arr = highpass_filter(clock)
    display_pic(arr, "Clock - Highpass Filter")

    arr = highpass_filter(man)
    display_pic(arr, "Man - Highpass Filter")

    arr = highpass_filter(tank)
    display_pic(arr, "Tank - Highpass Filter")



### M A I N ###
plt.gray()
display_originals()
display_lowpass()
display_highpass()

# Darin
display_pic(darin, "Darin Brezeale - Original")
display_pic(lowpass_filter(darin), "Darin Brezeale - Lowpass Filter")
outputImage = ndimage.median_filter(darin, 5)
display_pic(outputImage, "Darin Brezeale - Median Filter")

plt.show()
