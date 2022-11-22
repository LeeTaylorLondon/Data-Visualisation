# Author: Lee Taylor, ST Number: 190211479
from imports import *
import matplotlib.image as mpimg
from part_a import part_a
from part_b import part_b
from part_c import part_c


def collage(showplt=True, savepltimg=False):
    """ Plot a 4 panel 16:9 figure for each graph
    and text summarising each graph. """

    ## Set font-size for everything
    plt.rcParams.update({'font.size': 18})

    ## Configure main figure and subplots
    fig, (r1, r2) = plt.subplots(2, 2, figsize=(19.2, 10.8),
                                 facecolor=(0.07, 0.14, 0.2, 1))
    fig.suptitle("State of the (UK) Nation 2021", size=18, color='white')
    fig.tight_layout(pad=0.4)
    plt.subplots_adjust(wspace=-0.05)
    plts = [r1[0], r1[1], r2[0], r2[1]]
    for plt_ in plts:
        plt_.set_xticks([])
        plt_.set_yticks([])

    ## Set FTSE Chart border to white
    r2[1].spines[::].set_color('white')

    ## Create images
    parts = [part_a, part_b, part_c]
    for i,part in enumerate(parts):
        ## if-statement accounts for part_c different parameters
        if i != len(parts) - 1:
            fig_, (ax1_, ax2_) = plt.subplots(1, 2, figsize=(19.2, 10.8))
        else:
            fig_, ax1_ = plt.subplots(1, 1, figsize=(19.2, 10.8))
            ax2_ = None
        ## Call part_x function and delete plt vars
        part(fig_, ax1_, ax2_, show=False, save=True)
        del fig_, ax1_, ax2_
    plt.style.use('default')

    ## Load and plot images
    imgs_char = [c for c in 'dabc']
    for plt_, ichar in zip(plts, imgs_char):
        plt_.imshow(mpimg.imread(f'Images/part_{ichar}.png'))

    ## Save plot image then render (both optional)
    if showplt: fig.show()
    if savepltimg: fig.savefig('final.png')


if __name__ == '__main__':
    collage(showplt=False, savepltimg=True)
    # Todo: part_b highlight one or two areas of interest
    # Todo: part_c time period dashed vertical lines
    # Todo: (optional) part_a include legend
    # Todo: Include short paragraph for each panel
    # Todo: Write short summaries for each plot - Explain moving average for part_c
    # Todo: 1,000 Word Report
    # Todo: 200 Word Report