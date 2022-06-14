import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# our user defined function for plotting bar chart
from bar_plot_function import bar_plot

# read the csv file and put it in a pandas data frame
df_for_project5 = pd.read_csv("project_data5.csv")

# x values taken from data frame
x_vals_project_5 = df_for_project5.iloc[:, 0]

# read the colums "B and N" from data frame and convert to dictionary to pass in bar_plot function
data_as_dictionaray = df_for_project5.iloc[:, 1:].to_dict(orient="list")

# Get the figure and axes objects with figure size of 14x7
fig, ax = plt.subplots(figsize=(14, 7))

# Place a grid behid the graph (zorder=0)
ax.grid(which='major', axis='y', color='k', linestyle='-', linewidth=1, zorder=0)

# Plot the bars corresponding to thr column values in csv "2 3 4"
bar_plot(ax, data_as_dictionaray, fig, total_width=0.7, single_width=1, legend=True,
         legend_labels=("Binomial", "Normal"))

# Set y axis view limit to 0.25
ax.set_ylim(top=0.25)

# Set title of the graph
ax.set_title("Binomial vs Normal Distribution", fontsize=30, fontweight="bold", pad=30)

# customize major ticks so that group of bar/bars is between them
total_width_of_group_of_bars = 0.7
x_ticks_values = np.array(x_vals_project_5) + total_width_of_group_of_bars / 2 + 0.1

# place major x ticks and their labels
ax.set_xticks(x_ticks_values)

# Set lower numerical bound of x axis to -total_width_of_group_of_bars + 0.1
ax.set_xbound(lower=-total_width_of_group_of_bars + 0.1)

# Hide major tick labels
ax.set_xticklabels('')

# Add minor ticks and customize their labels
ax.set_xticks(x_vals_project_5, minor=True)
ax.set_xticklabels(map(str, np.array(x_vals_project_5) + 1), minor=True)

# remove minor ticks but keep their labels
ax.tick_params(axis='x', which='minor', length=0, labelsize=15)

# increase font size of y axis major ticks
ax.tick_params(axis='y', labelsize=15)

# save the image of a graph in folder imgs
fig.savefig('imgs/part5.jpg')

plt.show()
