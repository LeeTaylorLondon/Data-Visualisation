# Author: Lee Taylor, ST Number: 190211479
from imports import *


''' Part A - Create House DataFrame
Read the CSV file into a dataframe and rename the columns '''
## Create house data frame
houseDf = pd.read_csv("Data/Average-prices-Property-Type-2021-05_modified.csv")

## Standardize columns names
colNames = houseDf.columns
# print(f"Before: {colNames}")
houseDf.rename(columns={houseDf.columns[2]:'Property_Type'}, inplace=True)
houseDf.rename(columns={houseDf.columns[3]:'Avg_Price'}, inplace=True)

## Print houseDf information
# houseDf.columns
# print(houseDf[:5])

london_data = pd.DataFrame({'London Detached Avg': 0,
                            'London Semi Detached Avg': 0,
                            'London Terraced Avg': 0,
                            'London Flat Avg': 0},
                           index=[0])

newcastle_data = pd.DataFrame({'Newcastle Detached Avg': 0,
                            'Newcastle Semi Detached Avg': 0,
                            'Newcastle Terraced Avg': 0,
                            'Newcastle Flat Avg': 0},
                           index=[0])


''' Subplot London & Newcastle
Compare four categories of housing and their prices in two regions of the UK. 
This is nominal data where each category is a house type.
~Compare four types of housing and their prices in two regions of the UK. '''


ld = london_data
nd = newcastle_data


def part_a(fig, ax1, ax2, show=True, save=False):
    fig.suptitle("Regional Comparison of House Types and Prices")
    fig.text(0.01, 0.95, "FIGURE A", size=25)
    fig.text(0.46, 0.02, "Property Types", size=19)
    ## Axis 1 - London Data
    ax1.set_facecolor((0.8, 0.8, 0.8, 1.0))
    ax1.grid(axis='y', color='black')
    # 0.3 0.18 0.07
    ax1.bar(ld['Property_Type'], ld['Avg_Price'], color=
            [(0.6, 0.48, 0.37, 1.0), (0.5, 0.38, 0.27, 1.0),
             (0.4, 0.28, 0.17, 1.0), (0.3, 0.18, 0.07, 1.0)])
    ax1.set_title("London", color=(0.5, 0.38, 0.27, 1.0))
    ax1.tick_params('x', labelrotation=20)
    ax1.set_yticks(ticks=[x*200_000 for x in range(6)])
    ax1.set_yticklabels(labels=["£0", "£200K", "£400K",  "£600K", "£800K", "£1M"])
    # ax1.set_xlabel("Property Types")
    ax1.set_ylabel("Average Prices £")
    ax1.set_ylim(0, 1_000_000)
    ax1.legend()
    ## Axis 2 - Newcastle Data
    ax2.set_facecolor((0.8, 0.8, 0.8, 1.0))
    ax2.grid(axis='y', color='black')
    ax2.bar(nd['Property_Type'], nd['Avg_Price'], color=[
        (0.22, 0.47, 0.44, 1), (0.16, 0.41, 0.38, 1),
        (0.11, 0.36, 0.33, 1), (0.06, 0.31, 0.28, 1)])
    ax2.set_title("Newcastle upon Tyne", color=(0.17, 0.42, 0.39, 1))
    ax2.tick_params('x', labelrotation=20)
    ax2.set_yticks(ticks=[x*200_000 for x in range(6)])
    ax2.set_yticklabels(labels=["£0", "£200K", "£400K",  "£600K", "£800K", "£1M"])
    # ax2.set_xlabel("Property Types")
    ax2.set_ylabel("Average Prices £")
    ax2.set_ylim(0, 1_000_000)
    # Arguments
    if save: plt.savefig('Images/part_a.png')
    if show: plt.show()


if __name__ == '__main__':
    # print(houseDf.columns)
    # print(houseDf.columns[4:8])
    # print(houseDf.columns[8:12])

    print(london_data)

    for col in london_data.columns:
        print(houseDf[col][0])
        london_data[col][0] = houseDf[col][0]
    # print(london_data.columns)

    print("Actual")
    print(london_data)

    # print("\nLONDONNNNNN\n", london_data)
    # print("\nNEWWY CAR SAULLLL", newcastle_data)

    ## Plot data
    # plt.rcParams.update({'font.size': 18})
    # fig_, (ax1_, ax2_) = plt.subplots(1, 2, figsize=(19.2, 10.8))
    # part_a(fig_, ax1_, ax2_, False, True)
