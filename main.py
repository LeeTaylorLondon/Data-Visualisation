# Author: Lee Taylor, ST Number: 190211479
from imports import *
from part_a import part_a
from part_b import part_b
from part_c import part_c
from part_d import part_d

''' Create a 16:9 4 panel plot '''
fig, (row1, row2) = plt.subplots(2, 3, figsize=(19.2, 10.8),
                                 width_ratios=[1, 1, 1])

# Bar charts
part_a(row1[0], row1[1], False)

# Scatter plots
part_b(row2[0], row2[1], False)

# Time series
part_c(row2[2], False)

# Text Description
part_d()

fig.show()
plt.savefig('Images/final')

if __name__ == '__main__':
    # Create 4 panel plot as figmain
    # Save figmain
    # [Optional] prompt user to open figmain
    pass