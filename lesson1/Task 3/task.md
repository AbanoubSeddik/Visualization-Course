## Task 3: Load the Dataset:


Theory:
Loading the dataset is the first step in analyzing and visualizing data.

Using `pd.read_csv`, we load the CSV  
(Comma-Separated Values) file into a DataFrame, which is pandas' table-like data structure. 

DataFrames make it easy to manipulate and explore data as they provide methods for indexing, slicing, and aggregating data, similar to Excel but much more programmatically flexible.

Loading the dataset allows us to inspect the structure and contents to determine what we’re working with. This includes identifying columns like Platform and Genre, which will be crucial for filtering and grouping the data later.


##  Task:
Your task is to load the dataset into a pandas DataFrame. To do this, you will use the `pd.read_csv` function, passing the filename of your dataset **(in this case, 'dataset.csv')** as an argument. 

After loading the data, you should display the first few rows of the DataFrame to get a glimpse of its structure and contents.

<div class="hint">
  After you have successfully loaded the dataset into a DataFrame, you can display the first few rows to understand its structure and contents. To do this, use the method that starts with head(). This method, when called on your DataFrame, will show you the first five rows by default. If you want to see a different number of rows, you can pass a number as an argument to this method.

**For example**, if your DataFrame is named data, you would call` data.head()` to display the first five rows.

This step will help you quickly inspect the data and identify important columns such as "Platform" and "Genre."
</div>
