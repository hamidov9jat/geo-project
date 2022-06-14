import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np
import pandas as pd

# read the csv file and put it in a pandas data frame
df_for_project4 = pd.read_csv("project_data4.csv")

# x values from csv values
x_values = df_for_project4.iloc[5:, 0]

# Need to convert str type x values in csv file to float type
x_values = (x_values.to_numpy()).astype(np.float64)

# Need to convert str type y values in csv file to float64 type numpy array
y_beta04_values = df_for_project4.iloc[5:, 1]
y_beta04_values = (y_beta04_values.to_numpy()).astype(np.float64)

y_beta1_values = df_for_project4.iloc[5:, 2]
y_beta1_values = (y_beta1_values.to_numpy()).astype(np.float64)

y_beta2_values = df_for_project4.iloc[5:, 3]
y_beta2_values = (y_beta2_values.to_numpy()).astype(np.float64)

y_beta5_values = df_for_project4.iloc[5:, 4]
y_beta5_values = (y_beta5_values.to_numpy()).astype(np.float64)

# Get the figure and axes objects with figure size of 14x7
fig, ax = plt.subplots(figsize=(14, 7))

# # Set a tick on each integer multiple of a base within the view interval of 10.
ax.yaxis.set_major_locator(mtick.MultipleLocator(0.2))

# Place a grid behid the graph (zorder=0)
ax.grid(which='major', axis='y', alpha=0.5, color='k', linestyle='-', linewidth=1, zorder=0)

# curve for beta=0.4 is a blue line
ax.plot(x_values, y_beta04_values, 'b-', linewidth=3, label='beta 0.4')

# curve for beta=1 is a red line
ax.plot(x_values, y_beta1_values, 'r-', linewidth=3, label='beta 1.0')

# curve for beta=2 is a green line
ax.plot(x_values, y_beta2_values, 'g-', linewidth=3, label='beta 2.0')

# curve for beta=5 is a violet (#7f09d9) line
ax.plot(x_values, y_beta5_values, linestyle='-', color='#7f09d9', linewidth=3, label='beta 5.0')

# Show the legend
ax.legend(prop={'size': 20}, loc='lower center', bbox_to_anchor=(0.5, -0.27), ncol=4, frameon=False)

# extend the bottom margin of the figure by padding to fit the legend.
fig.subplots_adjust(bottom=0.20)

# Set title of the graph
ax.set_title("Weibull Distribution (PDF)", fontsize=30, fontweight="bold", pad=30)

# increase font of x and y ticks
ax.tick_params(axis='both', labelsize=15)

# Set y axis top view limit
ax.set_ylim(top=2)

# set lower numerical bound of the y-axis to 0
ax.set_ybound(lower=0)

# save the image of a graph in folder imgs
fig.savefig('imgs/part4.jpg')

plt.show()
