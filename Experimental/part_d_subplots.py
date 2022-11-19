# Author: Lee Taylor, ST Number: 190211479
from imports import *
import matplotlib.image as pltimg

## Create a paragraph of text detailing each part a,b,c
def part_d(ax, saveimg=True):
    ax.set_xticks([])
    ax.set_yticks([])

    img = pltimg.imread('Images/Ipsum Lorem.png')

    ax.imshow(img)

    if saveimg: plt.savefig('Images/part_d')
    pass


if __name__ == '__main__':
    fig, ax1 = plt.subplots(1, 1, figsize=(19.2, 10.8))
    part_d(ax1)
    fig.show()