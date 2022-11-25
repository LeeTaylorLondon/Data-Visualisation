# Author: Lee Taylor, ST Number: 190211479
import pandas as pd

from imports import *

## Create house data frame
bbSpeedDf = pd.read_csv("Data/202006_fixed_laua_performance_wrangled.csv")

## Print dataset information
# print(">>> Broadband speed original dataset")
# print(bbSpeedDf[:5])
# print(f"Len(bbSpeedDf) = {len(bbSpeedDf)}")
# print()

## Print dataset copy information
bbSpeedDf_cleaned = bbSpeedDf.__copy__()
# print(">>> Broadband speed dataset copied")
# print(bbSpeedDf_cleaned[:5])

# ['laua', 'laua_name', 'medDown', 'averageDown', 'medUpload',
#        'averageUpload']

bbSpeedDf_outliers = pd.DataFrame(columns=['laua', 'laua_name', 'medDown',
                                           'averageDown', 'medUpload',
                                            'averageUpload'])

## Remove outliers by download speed
for i,dspeed in enumerate(bbSpeedDf_cleaned['averageDown']):
    if dspeed > 120:
        bbSpeedDf_outliers = bbSpeedDf_outliers.append(bbSpeedDf_cleaned.loc[i])
        bbSpeedDf_cleaned.drop(index=i, inplace=True)
bbSpeedDf_cleaned.reset_index(drop=True, inplace=True)
## Remove outliers by upload speed
dropped = []
for i,uspeed in enumerate(bbSpeedDf_cleaned['averageUpload']):
    if uspeed > 20 or uspeed < 6:
        dropped.append(i)
        bbSpeedDf_outliers = bbSpeedDf_outliers.append(bbSpeedDf_cleaned.loc[i])
        bbSpeedDf_cleaned.drop(index=i, inplace=True)
bbSpeedDf_cleaned.reset_index(drop=True, inplace=True)

## Debug information
# print(f"Len(bbSpeedDf_cleaned) = {len(bbSpeedDf_cleaned)}")

## Sorting by average download & upload speed has no effect
# bbSpeedDf.sort_values(by=['averageDown', 'averageUpload'], ascending=False, inplace=True)

bbs  = bbSpeedDf
bbsc = bbSpeedDf_cleaned
bbso = bbSpeedDf_outliers

def part_b(fig, ax1, ax2, show=True, save=False):
    fig.suptitle("National Download to Upload Speed Comparison")
    fig.text(0.01, 0.95, "FIGURE B", size=25, color=(0.35, 0.35, 0.35, 1.0))
    ## Non clean data
    ax1.grid(color=(0.05, 0.05, 0.05, 1.0))
    ax1.set_facecolor((0.8, 0.8, 0.8, 1.0))
    ax1.set_title("Dataset with outliers", color=(0.16, 0.30, 0.38, 1.0))
    ax1.set_xlabel("Average Broadband Download Speed")
    ax1.set_ylabel("Average Broadband Upload Speed")
    x, y = bbs['averageDown'], bbs['averageUpload']
    ax1.scatter(x=x, y=y, color=(0.16, 0.30, 0.38, 1.0),
             label='Down to Up Speed')
    xo, yo = bbso['averageDown'], bbso['averageUpload']
    ax1.scatter(x=xo, y=yo, color='orange', label='Outliers')
    ax1.set_yticks(ticks=[x*10 for x in range(11)], rotation=0)
    # Regression line
    b, a = np.polyfit(x, y, deg=1)
    xseq = np.linspace(25, 165)
    ax1.plot(xseq, a + b * xseq, color='red', lw=3.0,
             label='Regression Line')
    ax1.legend()
    ## Clean data
    ax2.grid(color=(0.05, 0.05, 0.05, 1.0))
    ax2.set_facecolor((0.8, 0.8, 0.8, 1.0))
    ax2.set_title("Dataset with outliers removed",
                  color=(0.5, 0.0, 0.5, 1.0))
    ax2.set_xlabel("Average Broadband Download Speed")
    ax2.set_ylabel("Average Broadband Upload Speed")
    yticks = [x for x in range(6, 20)]
    ax2.set_yticks(ticks=yticks, labels=yticks, rotation=0)
    # Regression line
    x2, y2 = bbsc['averageDown'], bbsc['averageUpload']
    ax2.scatter(x=x2, y=y2, color=(0.35, 0.0, 0.35, 1.0),
             label='Down to Up Speed')
    b2, a2 = np.polyfit(x2, y2, deg=1)
    xseq = np.linspace(30, 110)
    ax2.plot(xseq, a2 + b2 * xseq, color='red', lw=3.0,
             label='Regression Line')
    ax2.legend()

    if save: plt.savefig('Images/part_b.png')
    if show: plt.show()


if __name__ == '__main__':
    plt.rcParams.update({'font.size': 18})
    fig_, (ax1_, ax2_) = plt.subplots(1, 2, figsize=(19.2, 10.8))
    part_b(fig_, ax1_, ax2_, False, True)
    pass


