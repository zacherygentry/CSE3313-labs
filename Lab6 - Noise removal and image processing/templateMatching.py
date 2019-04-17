# Zachery Gentry

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from skimage import feature


def findImage(mainImage, template):
    main = Image.open(mainImage).convert('LA')
    template = Image.open(template).convert('LA')
    main_arr = np.array(main)
    template_arr = np.array(template)

    plt.figure(1)
    plt.imshow(main)
    plt.figure(2)
    plt.imshow(template)

    shape = template_arr.shape
    width = shape[0]
    length = shape[1]

    result = feature.match_template(main_arr, template_arr)
    corner = np.where(result == np.max(result))
    x = corner[0][0]
    y = corner[1][0]
    print("Coordinates for top left corner (X, Y): ", x, y)

    new_image = np.copy(main_arr)
    new_image[x: x + width, y: y + length] = [0, 255]

    final_img = Image.fromarray(new_image)
    plt.figure(3)
    plt.imshow(final_img)

    plt.show()


#############  main  #############
if __name__ == "__main__":
    mainImage = "ERBwideColorSmall.jpg"
    template = "ERBwideTemplate.jpg"
    findImage(mainImage, template)
