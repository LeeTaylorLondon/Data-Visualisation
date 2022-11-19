# Author: Lee Taylor, ST Number: 190211479
from imports import *

## Create house data frame
bbSpeedDf = pd.read_csv("Data/202006_fixed_laua_performance_wrangled.csv")

## Print dataset information
print(">>> Broadband speed original dataset")
print(bbSpeedDf[:5])
print(f"Len(bbSpeedDf) = {len(bbSpeedDf)}")
print()

## Print dataset copy information
bbSpeedDf_cleaned = bbSpeedDf.__copy__()
print(">>> Broadband speed dataset copied")
print(bbSpeedDf_cleaned[:5])

## Remove outliers by download speed
for i,dspeed in enumerate(bbSpeedDf_cleaned['averageDown']):
  if dspeed > 100:
    bbSpeedDf_cleaned.drop(index=i, inplace=True)
bbSpeedDf_cleaned.reset_index(drop=True, inplace=True)
## Remove outliers by upload speed
for i,uspeed in enumerate(bbSpeedDf_cleaned['averageUpload']):
  if uspeed > 20:
    bbSpeedDf_cleaned.drop(index=i, inplace=True)
bbSpeedDf_cleaned.reset_index(drop=True, inplace=True)

print(f"Len(bbSpeedDf_cleaned) = {len(bbSpeedDf_cleaned)}")

## Sorting by average download & upload speed has no effect
# bbSpeedDf.sort_values(by=['averageDown', 'averageUpload'], ascending=False, inplace=True)

bbs  = bbSpeedDf
bbsc = bbSpeedDf_cleaned

def part_b(ax1, ax2, show=True, save=False):
    ## Non clean data
    ax1.grid()
    ax1.set_title("Dataset with outliers", color='red')
    ax1.set_xlabel("Average Broadband Download Speed")
    ax1.set_ylabel("Average Broadband Upload Speed")
    x, y = bbs['averageDown'], bbs['averageUpload']
    ax1.scatter(x=x, y=y, color='red')
    # Regression line
    b, a = np.polyfit(x, y, deg=1)
    xseq = np.linspace(25, 165)
    ax1.plot(xseq, a + b * xseq, color='k', lw=2.0)
    ## Clean data
    ax2.grid()
    ax2.set_title("Dataset with outliers removed", color='blue')
    ax2.set_xlabel("Average Broadband Download Speed")
    ax2.set_ylabel("Average Broadband Upload Speed")
    # Regression line
    x2, y2 = bbsc['averageDown'], bbsc['averageUpload']
    ax2.scatter(x=x2, y=y2, color='blue')
    b2, a2 = np.polyfit(x2, y2, deg=1)
    xseq = np.linspace(30, 100)
    ax2.plot(xseq, a + b * xseq, color='k', lw=2.0)

    if show: fig_b.show()
    if save: plt.savefig('Images/part_b.png')
