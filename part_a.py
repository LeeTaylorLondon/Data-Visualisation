# Author: Lee Taylor, ST Number: 190211479
from imports import *


''' Part A - Create House DataFrame
Read the CSV file into a dataframe and rename the columns '''
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
The wrangled data is seperated into two different dataframes by region '''
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

~Compare four types of housing and their prices in two regions of the UK. '''
ld = london_data
nd = newcastle_data


def part_a(ax1, ax2, show=True, save=False):
    ## Axis 1 - London Data
    ax1.grid(axis='y', color='black')
    ax1.bar(ld['Property_Type'], ld['Avg_Price'], color='red')
    ax1.set_title("London", color='red', fontdict=fd22)
    ax1.tick_params('x', labelrotation=0)
    ax1.set_yticks(ticks=[x*200_000 for x in range(6)])
    ax1.set_yticklabels(labels=["£0", "£200K", "£400K",  "£600K", "£800K", "£1M"])
    ax1.set_xlabel("Property Types")
    ax1.set_ylabel("Average Prices £")
    ax1.set_ylim(0, 1_000_000)
    ## Axis 2 - Newcastle Data
    ax2.grid(axis='y')
    ax2.bar(nd['Property_Type'], nd['Avg_Price'], color='blue')
    ax2.set_title("Newcastle upon Tyne", color='blue')
    ax2.tick_params('x', labelrotation=0)
    ax2.set_yticks(ticks=[x*200_000 for x in range(6)])
    ax2.set_yticklabels(labels=["£0", "£200K", "£400K",  "£600K", "£800K", "£1M"])
    ax2.set_xlabel("Property Types")
    ax2.set_ylabel("Average Prices £")
    ax2.set_ylim(0, 1_000_000)

    if show: fig.show()
    if save: plt.savefig('Images/part_a.png')


if __name__ == '__main__':
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(19.2, 10.8))

