# Author: Lee Taylor, ST Number: 190211479
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

''' Part A - Create House DataFrame
Read the CSV file into a dataframe and rename the columns 
'''

## Create house data frame
houseDf = pd.read_csv("Data/Average-prices-Property-Type-2021-05_wrangled.csv")

## Standardize columns names
colNames = houseDf.columns
print(f"Before: {colNames}")
houseDf.rename(columns={houseDf.columns[2]:'Property_Type'}, inplace=True)
houseDf.rename(columns={houseDf.columns[3]:'Avg_Price'}, inplace=True)

# Print houseDf information
houseDf.columns
print(houseDf[:5])

''' Seperate Data by Region
The wrangled data is seperated into two different dataframes by region
'''

london_data    = pd.DataFrame(columns=['Date', 'Region_Name', 'Property_Type', 'Avg_Price'])
newcastle_data = pd.DataFrame(columns=['Date', 'Region_Name', 'Property_Type', 'Avg_Price'])

for i,v in enumerate(houseDf['Region_Name']):
  if v.lower()[0] == 'l':
    london_data = london_data.append(houseDf.loc[i], ignore_index=True)
  elif v.lower()[0] == 'n':
    newcastle_data = newcastle_data.append(houseDf.loc[i], ignore_index=True)

print(">>> LONDON DATA")
print(london_data)
print()

print(">>> NEWCASTLE DATA")
print(newcastle_data)

''' Subplot London & Newcastle
Compare four categories of housing and their prices in two regions of the UK. This is nominal data where each category is a house type.

~Compare four types of housing and their prices in two regions of the UK. 
'''
ld = london_data
nd = newcastle_data

fd   = {'fontsize':18} # fd -> fontdict
fd22 = {'fontsize':22} # fd -> fontdict

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(19.2, 10.8))
fig.tight_layout(pad=10)
fig.suptitle("Regional Comparison of Property Types by Average Price" , fontsize=24)
## Axis 1 - London Data
ax1.grid(axis='y', color='black')
ax1.bar(ld['Property_Type'], ld['Avg_Price'], color='red')
ax1.set_title("London", color='red', fontdict=fd22)
ax1.tick_params('x', labelrotation=0, labelsize=16)
ax1.set_yticks(ticks=[x*200_000 for x in range(6)])
ax1.set_yticklabels(labels=["£0", "£200K", "£400K",  "£600K", "£800K", "£1M"],
                    fontdict=fd)
ax1.set_xlabel("Property Types", fontdict=fd)
ax1.set_ylabel("Average Prices £", fontdict=fd22)
ax1.set_ylim(0, 1_000_000)
## Axis 2 - Newcastle Data
ax2.grid(axis='y')
ax2.bar(nd['Property_Type'], nd['Avg_Price'], color='blue')
ax2.set_title("Newcastle upon Tyne", color='blue', fontdict=fd22)
ax2.tick_params('x', labelrotation=0, labelsize=16)
ax2.set_yticks(ticks=[x*200_000 for x in range(6)])
ax2.set_yticklabels(labels=["£0", "£200K", "£400K",  "£600K", "£800K", "£1M"],
                    fontdict=fd)
ax2.set_xlabel("Property Types", fontdict=fd)
ax2.set_ylabel("Average Prices £", fontdict=fd22)
ax2.set_ylim(0, 1_000_000)

fig.show()
plt.savefig('Images/part_a')

''' PART B '''

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

plt.style.use('default')

fig_b, (ax1, ax2) = plt.subplots(1, 2, figsize=(19.2, 10.8))
fig_b.suptitle("Comparison of all Regions Download to Upload Broadband Speed")
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

fig.show()
plt.savefig('Images/part_b')

''' PART C '''

## Create house data frame
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
  c    = c['Close']
  ns   = pd.Series(c)
  ma   = round(ns.ewm(
      alpha=alpha, adjust=False).mean(), period)
  mali = ma.tolist()
  # Convert list-ma to type <class 'pandas.core.series.Series'>
  # ma = pd.core.series.Series(ma)
  return mali

# Init. matplotlib
plt.style.use('dark_background')
fig_c = plt.figure(figsize=(19.2, 10.8))  # 1920px by 1080px
plt.grid(color='grey')
# Shorten variable names
d = ftse5y['date']  # d = Dates
c = ftse5y['Close'] # c = Close prices
# Calculate moving average
ma = calc_moving_avg(1, 0.025, ftse5y)
# Plot data
plt.plot(d, c, linewidth=1.25, color=(0, 0.8, 0, 1.0), label='Close Price')
plt.plot(d, ma, linewidth=0.75, color=(0.8, 0, 0.8, 1.0), label='Moving Average')
# Title and Axis labels
plt.title("FTSE Data")
plt.xlabel("Date (Year-Month-Day)")
plt.ylabel("Close Price")
# Axis tickers and labels
plt.yticks(ticks=[y for y in range(int(min(c)), int(max(c)) + 200, 200)],
           labels=["£" + str(x) + ".00" for x in range(int(min(c)),
                                                       int(max(c)) + 200, 200)])
plt.xticks(ticks=[x for x in range(0, len(d), 125)],
           rotation=0)

fig.show()
plt.savefig('Images/part_c')

# Render chart with legend
plt.legend()
plt.show()
