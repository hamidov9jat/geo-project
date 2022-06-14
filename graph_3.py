import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import pandas as pd

# read the csv file and put it in a pandas data frame
df_for_project3 = pd.read_csv("project_data3.csv")

# rename the columns (in csv file β was printed as ?)
df_for_project3 = df_for_project3.rename(columns={'?': 'β', '1-?': '1-β'})

# multiply 1-β column by 100
df_for_project3.iloc[:, 2] = df_for_project3.iloc[:, 2].mul(100)

# x and y values to plot
x_values = df_for_project3.iloc[0:, 0]
y_values = df_for_project3.iloc[0:, 2]

# Get the figure and axes objects with figure size of 14x7
fig, ax = plt.subplots(figsize=(14, 7))

# Format labels as a percents
ax.yaxis.set_major_formatter(mtick.PercentFormatter())

# Set a tick on each integer multiple of a base within the view interval of 10.
ax.yaxis.set_major_locator(mtick.MultipleLocator(10))

# Place a grid along y axis behid the graph (zorder=0)
ax.grid(which='major', axis='y', color='k', linestyle='-', linewidth=1, zorder=0)

# curve is a blue line
ax.plot(x_values, y_values, 'b-', linewidth=4)

# Set title of the graph
ax.set_title("Power Curve - two-tailed", fontsize=30, fontweight="bold", pad=30)

# Set y axis top view limit to 100
ax.set_ylim(top=100)

# set lower numerical bounds of the y-axis to 0
ax.set_ybound(lower=0)

# mark x ticks based on x values
ax.set_xticks(x_values)

# increase font of x and y ticks
ax.tick_params(axis='both', labelsize=15)

# Set the label for the y-axis.
ax.set_ylabel("Power", fontsize=20, fontweight='demibold')

# Set the label for the x-axis.
ax.set_xlabel("Actual value of p", fontsize=20, fontweight='demibold')

# save the image of a graph in folder imgs
fig.savefig('imgs/part3.jpg')

plt.show()
