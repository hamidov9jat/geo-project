import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# our user defined function for plotting bar chart
from bar_plot_function import bar_plot

# read the csv file and put it in a pandas data frame
df_for_project1 = pd.read_csv("project_data2.csv")

# x values taken from data frame
x_vals = df_for_project1.iloc[:, 0]

# read the column "f(x)" from data frame and convert to dictionary to pass in bar_plot function
data_as_dictionaray = (df_for_project1.iloc[:, [1]]).to_dict(orient="list")

# Get the figure and axes objects with figure size of 14x7
fig, ax = plt.subplots(figsize=(14, 7))

# Place a grid behid the graph (zorder=0)
ax.grid(which='major', axis='y', alpha=0.5, color='k', linestyle='-', linewidth=1, zorder=0)

# Plot the bars corresponding to the column values in csv "f(x)"
bar_plot(ax, data_as_dictionaray, total_width=.8, single_width=0.7, legend=False)

# detemininig x coordinate to plot critical value
total_width = 0.8
single_width = 0.7
n_bars = len(data_as_dictionaray)

# The width of a single bar
bar_width = total_width / n_bars

# x coordinate of the critical value
x_coordiante = 12 - (1 - total_width) - 0.1

# plot the critical value line with ymax equal to the largest values from f(x) column
critical_value = ax.vlines(x=x_coordiante, ymin=0, ymax=max(*data_as_dictionaray.values()),
                           colors='r', zorder=4, linewidth=2, label='critical value')

# add text for critical value
ax.text(x=12, y=0.15, s='critical value', color='r', fontsize=15, fontweight='bold')

# Set y axis view limit to 0.25
ax.set_ylim(top=0.18)

# customize major ticks so that group of bar/bars is between them
total_width_of_group_of_bars = 0.8
x_ticks_values = np.array(x_vals) + total_width_of_group_of_bars / 2 + 0.1
ax.set_xticks(x_ticks_values)

# Set lower numerical bound of x axis to 0
ax.set_xbound(lower=-total_width_of_group_of_bars)

# Hide major tick labels
ax.set_xticklabels('')

# # Add minor ticks and customize their labels
ax.set_xticks(x_vals, minor=True)
ax.set_xticklabels(map(str, x_vals), minor=True, fontsize=15)

# remove minor ticks but keep their labels
ax.tick_params(axis='x', which='minor', length=0, labelsize=15)

# increase font size of y axis major ticks
ax.tick_params(axis='y', labelsize=15)

# Set title of the graph
ax.set_title("Binomial Distribution", fontsize=30, fontweight="bold", pad=30)

# save the image of a graph in folder imgs
fig.savefig('imgs/part2.jpg')

plt.show()
