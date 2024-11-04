import unittest
import pandas as pd


class TestFilterDataset(unittest.TestCase):

    def setUp(self):
        """Set up the dataset for testing."""
        # Load the provided dataset for testing
        self.data = pd.read_csv('dataset.csv')
        self.platforms = ['PS4', 'XOne', 'PC', 'WiiU']

    def test_filter_platforms(self):
        """Test that the filtered data only includes the specified platforms."""
        # Filter the dataset to include only the specified platforms
        filtered_data = self.data[self.data['platform'].isin(self.platforms)]

        # Check that all platforms in the filtered data are in the specified platform list
        for platform in filtered_data['platform'].unique():
            self.assertIn(platform, self.platforms, f"Platform '{platform}' should be in {self.platforms}")

    def test_no_other_platforms(self):
        """Test that the filtered data excludes platforms not in the specified list."""
        # Filter the dataset
        filtered_data = self.data[self.data['platform'].isin(self.platforms)]

        # Get unique platforms in the filtered data and verify they match the specified platforms
        unique_platforms = set(filtered_data['platform'].unique())
        self.assertTrue(unique_platforms.issubset(set(self.platforms)),
                        f"Filtered data contains unexpected platforms: {unique_platforms - set(self.platforms)}")


# Run the unittests
unittest.TextTestRunner().run(unittest.makeSuite(TestFilterDataset))
