# Author: Lee Taylor, ST Number: 190211479
from imports import *

# Create house data frame
ftsedf = pd.read_csv("Data/ftse_data_wrangled.csv")

ftsedf.index = ftsedf.date
# print(ftsedf[:45])

# 1D 5D 1M 6M YTD 1Y 5Y MAX
# 1M 6M 1Y 5Y

# Create different time periods
ftse1m = pd.DataFrame(ftsedf['2021-09-08':])
ftse6m = pd.DataFrame(ftsedf['2021-04-08':])
ftse1y = pd.DataFrame(ftsedf['2020-10-08':])
ftse5y = pd.DataFrame(ftsedf['2016-10-08':])
ftse2008 = pd.DataFrame(ftsedf['2008-03-07':])
ftsemax = ftsedf


def calc_moving_avg(period=1, alpha=0.5, c=ftse2008):
    # Calculate moving average
    c = c['Close']
    ns = pd.Series(c)
    ma = round(ns.ewm(
        alpha=alpha, adjust=False).mean(), period)
    mali = ma.tolist()
    # Convert list-ma to type <class 'pandas.core.series.Series'>
    # ma = pd.core.series.Series(ma)
    return mali


def part_c(fig, ax1, _, show=True, save=False):
    plt.style.use('dark_background')
    ax1 = plt.axes()
    ax1.grid(color='white')
    ax1.set_facecolor(color=(0.10, 0.10, 0.10, 1.0))
    fig.suptitle("FTSE 100 Index - Close Price - 5 Years")
    fig.text(0.01, 0.95, "FIGURE C", size=25)
    # Shorten variable names
    d = ftse5y['date']   # d = Dates
    c = ftse5y['Close']  # c = Close prices
    # Calculate moving average
    ma = calc_moving_avg(1, 0.025, ftse5y)
    # Plot data
    ax1.plot(d, c, linewidth=1.5, color=(0.99, 0.99, 0.99, 1.0), label='Close Price')
    ax1.plot(d, ma, linewidth=1.2, color=(0.06, 0.24, 0.8, 1.0), label='Moving Average')
    # Title and Axis labels
    ax1.set_title("FTSE Data", size=20)
    ax1.set_xlabel("Date (Year-Month-Day)")
    ax1.set_ylabel("Close Price")
    # Axis tickers and labels
    ax1.set_xticks(ticks=[x for x in range(0, len(d), 125)])
    ax1.tick_params(labelrotation=20, length=10)
    yticks  = [y for y in range(int(min(c)), int(max(c)) + 200, 200)]
    ylabels = ["£" + str(x) + ".00" for x in yticks]
    ax1.set_yticks(ticks=yticks, labels=ylabels, rotation=0)
    # Highlight corona time period
    ax1.axvspan('2020-02-27', '2020-12-23',
               label="Corona Virus", color="red", alpha=0.3)
    # Render chart with legend
    ax1.legend()
    if save: plt.savefig('Images/part_c.png')
    if show: plt.show()


if __name__ == '__main__':
    plt.rcParams.update({'font.size': 16})
    fig_, ax1_ = plt.subplots(1, 1, figsize=(19.2, 10.8),
                              facecolor=(0.90, 0.90, 0.90, 1))
    part_c(fig_, ax1_, None, False, True)
