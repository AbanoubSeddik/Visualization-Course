
## Task 5 Aggregate by Genre and Platform:


Aggregating data by genre and platform allows us to see patterns across categories.

By grouping the filtered data by Genre and Platform, we can count the number of games for each genre on each platform.

This summary helps create a clearer picture of genre popularity across platforms, setting up the data for a grouped bar chart visualization.

Using groupby with `size()` counts occurrences, and `unstack()` reshapes the result, creating a table with genres as rows and platforms as columns.

This makes it easier to visualize the data directly.

## Task:

For this step, your task is to write code to aggregate the data by Genre and Platform. You should:

1. Use `groupby` on Genre and Platform.
2. Count the number of games for each combination.
3. Reshape the result using `unstack()` to get genres as rows and platforms as columns.

<div class="hint">
  You’ll want to use the `groupby` method on both Genre and Platform, followed by `size()` to count occurrences. After that, call `unstack(fill_value=0)` to make the result easier to visualize, with genres as rows and platforms as columns. For instance, if your DataFrame is named `filtered_data`, your code might start with `filtered_data.groupby(...)`.
</div>

