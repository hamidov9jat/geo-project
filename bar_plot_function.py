import matplotlib.pyplot as plt


def bar_plot(ax, data, fig=None, colors=None, total_width=0.8, single_width=1, legend=True, legend_labels=None):
    """Draws a bar plot with multiple bars per data point.

    Parameters
    ----------
    ax : matplotlib.pyplot.axis
        The axis we want to draw our plot on.

    fig : matplolib figure object
        The figure of our graph (optional)

    data: dictionary
        A dictionary containing the data we want to plot. Keys are the names of the
        data, the items is a list of the values.

        Example:
        data = {
            "x":[1,2,3],
            "y":[1,2,3],
            "z":[1,2,3],
        }

    colors : array-like, optional
        A list of colors which are used for the bars. If None, the colors
        will be the standard matplotlib color cyle. (default: None)

    total_width : float, optional, default: 0.8
        The width of a bar group. 0.8 means that 80% of the x-axis is covered
        by bars and 20% will be spaces between the bars.

    single_width: float, optional, default: 1
        The relative width of a single bar within a group. 1 means the bars
        will touch eachother within a group, values less than 1 will make
        these bars thinner.

    legend: bool, optional, default: True
        If this is set to true, a legend will be added to the axis.

    legend_labels: iterable of strings, optional, default: None
        If this is supplied, custom legends will be added to the axis, otherwise
        default ones are used
    """

    # Check if colors where provided, otherwhise use the default color cycle
    if colors is None:
        colors = plt.rcParams['axes.prop_cycle'].by_key()['color']

    # Number of bars per group
    n_bars = len(data)

    # The width of a single bar
    bar_width = total_width / n_bars

    # List containing handles for the drawn bars, used for the legend
    bars = []

    # indexes for bar groups
    # bar_groups_indexes = []
    # group_index = 1

    # Iterate over all data
    for i, (name, values) in enumerate(data.items()):
        # The offset in x direction of that bar
        x_offset = (i - n_bars / 2) * bar_width + bar_width / 2

        # Draw a bar for every value of that type
        for x, y in enumerate(values):
            bar = ax.bar(x + x_offset, y, width=bar_width * single_width, color=colors[i % len(colors)], zorder=3)

        # Add a handle to the last drawn bar, which we'll need for the legend
        bars.append(bar[0])

    # Draw default legend if we need otherwise use custom labels for legend
    if legend_labels:  # custom labels
        plt.legend(bars, legend_labels, prop={'size': 20}, loc='lower center', bbox_to_anchor=(0.5, -0.20), ncol=n_bars,
                   frameon=False)
    elif legend:  # default labels (correspond to column names in data)
        plt.legend(bars, data.keys(), prop={'size': 20}, loc='lower center', bbox_to_anchor=(0.5, -0.20), ncol=n_bars,
                   frameon=False)
    if fig:
        # extend the bottom margin of the figure by padding to fit the legend.
        fig.subplots_adjust(bottom=0.15)
