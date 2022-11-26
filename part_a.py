# Author: Lee Taylor, ST Number: 190211479
from imports import *


''' Part A - Create House DataFrame
Read the CSV file into a dataframe and rename the columns '''
## Create house data frame
houseDf = pd.read_csv("Data/Average-prices-Property-Type-2021-05_wrangled.csv")

## Standardize columns names
colNames = houseDf.columns
# print(f"Before: {colNames}")
houseDf.rename(columns={houseDf.columns[2]:'Property_Type'}, inplace=True)
houseDf.rename(columns={houseDf.columns[3]:'Avg_Price'}, inplace=True)

## Print houseDf information
# houseDf.columns
# print(houseDf[:5])

london_data = pd.DataFrame({'Property_Type': ['Detached', 'Semi_Detached', 'Terraced', 'Flat'],
                            'Region': ['London' for y in range(4)],
                            'Avg_Price': [968220.5103, 628968.471, 331361.7469, 196840.7592],
                            'Year': [2021 for z in range(4)]},
                           index=['Detached', 'Semi_Detached', 'Terraced', 'Flat'])

newcastle_data = pd.DataFrame({'Property_Type': ['Detached', 'Semi_Detached', 'Terraced', 'Flat'],
                            'Region': ['Newcastle' for j in range(4)],
                            'Avg_Price': [538415.3778, 427992.3715, 167206.5231, 114659.7908],
                            'Year': [2021 for i in range(4)]},
                           index=['Detached', 'Semi_Detached', 'Terraced', 'Flat'])


''' Subplot London & Newcastle
Compare four categories of housing and their prices in two regions of the UK. 
This is nominal data where each category is a house type.
~Compare four types of housing and their prices in two regions of the UK. '''

## Debug information
# print('>>> Lunny Done')
# print(london_data)
# print(london_data.shape)
# print()
# print('>>> Newwy Car Saul')
# print(newcastle_data)
# print(newcastle_data.shape)
# print()

ld = london_data
nd = newcastle_data

for i,v in enumerate(houseDf['Date']):
    if v.__contains__('2021'):
        london   = False
        full_val = houseDf.loc[i]
        if full_val['Region_Name'][0] == 'L': london = True
        ## Todo: get this to work
        # if london: ld.loc[full_val['Property_Type']]['Avg_Price'] = full_val['Avg_Price']
        # print(">>>>>>>>><<<<<<<<<<<<<")
        # print(full_val['Avg_Price'])


def part_a(fig, ax1, ax2, show=True, save=False):
    fig.suptitle("Regional Comparison of House Types and Prices 2021")
    fig.text(0.01, 0.95, "FIGURE A", size=25, color=(0.35, 0.35, 0.35, 1.0))
    fig.text(0.46, 0.02, "Property Types", size=19)
    ## Axis 1 - London Data
    ax1.set_facecolor((0.8, 0.8, 0.8, 1.0))
    ax1.grid(axis='y', color='black')
    ax1_bars = ax1.bar(ld['Property_Type'], ld['Avg_Price'], color=
            [(0.6, 0.48, 0.37, 1.0), (0.5, 0.38, 0.27, 1.0),
             (0.4, 0.28, 0.17, 1.0), (0.3, 0.18, 0.07, 1.0)],
            label=['Detached', 'Semi Detached', 'Terraced', 'Flat'])
    ax1.bar_label(container=ax1_bars, labels=['£968,220.51', '£628,968.47',
                                              '£331,361.75', '£196,840.76'],
                  size=16, color=(0.0, 0.0, 0.0, 1.0))
    ax1.set_title("London", color=(0.5, 0.38, 0.27, 1.0))
    ax1.tick_params('x', labelrotation=20)
    ax1.set_yticks(ticks=[x*100_000 for x in range(11)])
    ax1.set_yticklabels(labels=["£" + str(x*100) + "K" for x in range(11)], size=16)
    # ax1.set_xlabel("Property Types")
    ax1.set_ylabel("Average Prices £")
    ax1.set_ylim(0, 1_000_000)
    ax1.legend()
    ## Axis 2 - Newcastle Data
    ax2.set_facecolor((0.8, 0.8, 0.8, 1.0))
    ax2.grid(axis='y', color='black')
    ax2_bars = ax2.bar(nd['Property_Type'], nd['Avg_Price'], color=[
        (0.22, 0.47, 0.44, 1), (0.16, 0.41, 0.38, 1),
        (0.11, 0.36, 0.33, 1), (0.06, 0.31, 0.28, 1)],
            label=['Detached', 'Semi Detached', 'Terraced', 'Flat'])
    ax2.bar_label(ax2_bars, labels=['£538,415.38', '£427,992.37',
                                    '£167,206.52', '£114,659.79'],
                  size=16, color=(0.0, 0.0, 0.0, 1.0))
    ax2.set_title("Newcastle upon Tyne", color=(0.17, 0.42, 0.39, 1))
    ax2.tick_params('x', labelrotation=20)
    ax2.set_yticks(ticks=[x*100_000 for x in range(11)])
    ax2.set_yticklabels(labels=["£" + str(x*100) + "K" for x in range(11)], size=16)
    # ax2.set_xlabel("Property Types")
    ax2.set_ylabel("Average Prices £")
    ax2.set_ylim(0, 1_000_000)
    ax2.legend()
    # Arguments
    if save: plt.savefig('Images/part_a.png')
    if show: plt.show()


if __name__ == '__main__':
    ## Debug
    # print("\n>>> Actual")
    # print(london_data)
    # print(newcastle_data)
    ## Plot data
    plt.rcParams.update({'font.size': 18})
    fig_, (ax1_, ax2_) = plt.subplots(1, 2, figsize=(19.2, 10.8))
    part_a(fig_, ax1_, ax2_, False, True)
