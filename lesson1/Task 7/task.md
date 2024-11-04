in matplotlib,
the first step in creating a plot is to set up a figure and an axis.

The figure is the overall window or page that will hold the chart,

while the axis is the specific area within the figure where the chart will be drawn.

By using :

    fig, ax = plt.subplots()

we create both a figure and an axis. 

Setting the figure size can help ensure the chart is readable, especially when there are many labels or bars.

<div class="hint">

* Set up your figure and axis with plt.subplots() to prepare for plotting.

  * Use

        figsize=(10, 6) # Width and height of the figure in inches
</div>

