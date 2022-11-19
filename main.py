# Author: Lee Taylor, ST Number: 190211479
from imports import *
import matplotlib.image as mpimg
from part_a import part_a
from part_b import part_b
from part_c import part_c


def collage(showplt=True, savepltimg=False):
    """ Plot a 4 panel 16:9 figure for each graph
    and text summarising each graph. """
    ## Configure main figure and subplots
    fig, (r1, r2) = plt.subplots(2, 2, figsize=(19.2, 10.8),
                                 facecolor=(0.90, 0.90, 0.90, 1))
    fig.suptitle("State of the (UK) Nation 2021", size=22)
    fig.tight_layout(pad=1)
    plt.subplots_adjust(wspace=-0.1)
    plts = [r1[0], r1[1], r2[0], r2[1]]
    for plt_ in plts:
        plt_.set_xticks([])
        plt_.set_yticks([])
    imgs_char = [c for c in 'dabc']
    ## Create images
    parts = [part_a, part_b, part_c]
    for i,part in enumerate(parts):
        if i != len(parts) - 1: fig_, (ax1_, ax2_) = plt.subplots(1, 2, figsize=(19.2, 10.8))
        else:
            fig_, ax1_ = plt.subplots(1, 1, figsize=(19.2, 10.8))
            ax2_ = None
        part(ax1_, ax2_, show=False, save=True)
        del fig_, ax1_, ax2_
    ## Load and plot images
    for plt_, ichar in zip(plts, imgs_char):
        plt_.imshow(mpimg.imread(f'Images/part_{ichar}.png'))
    ## Render figure and save as image
    if showplt: fig.show()
    if savepltimg: fig.savefig('final.png')


if __name__ == '__main__':
    collage(showplt=True, savepltimg=True)