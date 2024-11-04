import unittest
import pandas as pd


class TestGenrePlatformAggregation(unittest.TestCase):

    def setUp(self):
        """Set up the filtered dataset for testing."""
        # Load the provided dataset and filter it as per the previous step
        self.data = pd.read_csv('dataset.csv')
        self.platforms = ['PS4', 'XOne', 'PC', 'WiiU']
        self.filtered_data = self.data[self.data['platform'].isin(self.platforms)]

    def test_genre_platform_aggregation(self):
        """Test that genre_platform_counts has the correct structure and data types."""
        # Aggregate the filtered data by Genre and Platform
        genre_platform_counts = self.filtered_data.groupby(['genre', 'platform']).size().unstack(fill_value=0)

        # Test if genre_platform_counts has genres as rows and platforms as columns
        self.assertTrue('PS4' in genre_platform_counts.columns,
                        "Column 'PS4' should be present in genre_platform_counts")
        self.assertTrue('XOne' in genre_platform_counts.columns,
                        "Column 'XOne' should be present in genre_platform_counts")
        self.assertTrue('PC' in genre_platform_counts.columns, "Column 'PC' should be present in genre_platform_counts")
        self.assertTrue('WiiU' in genre_platform_counts.columns,
                        "Column 'WiiU' should be present in genre_platform_counts")

        # Test if each cell in genre_platform_counts is an integer
        self.assertTrue((genre_platform_counts.dtypes == 'int64').all(),
                        "All values in genre_platform_counts should be integers")

        # Print a sample of genre_platform_counts to verify the structure
        print("Sample of aggregated data:\n", genre_platform_counts.head())


# Run the tests
if __name__ == '__main__':
    unittest.main()
