
## Task 4: Filter the Dataset

In data analysis, focusing on relevant data is crucial for clarity and efficiency. 

Here, we’re filtering the dataset to include only specific gaming platforms (PS4, XOne, PC, and WiiU).

Filtering ensures that the final visualization represents the intended scope and prevents clutter from irrelevant data.

Filtering also allows us to customize visualizations more precisely.

For instance, if we included every platform, the chart might become too crowded, making it harder to interpret. Limiting the data keeps the chart focused and clean, helping viewers to quickly understand trends in the selected platforms.

## Task

Your task is to filter the dataset so that it only includes rows where the "Platform" column matches one of the specified platforms: **PS4, XOne, PC, or WiiU.** Filtering is done using the `isin()` method in pandas, which lets you check if a value in a column belongs to a specific list of values.

To guide you, part of the code is provided below. Complete the TODO to filter the data and store the result in filtered_data.

<div class="hint">

To filter the dataset:

* Use `data[condition]`, where `condition` is a boolean filter for the rows.
* `isin()` is a method that checks if a value in a column belongs to a list of values.
* In this case, you want to apply `isin()` to the "Platform" column, checking if it matches any of the values in the platforms list.
</div>
