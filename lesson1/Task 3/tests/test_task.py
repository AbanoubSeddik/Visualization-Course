import unittest
import pandas as pd


class TestLoadDataset(unittest.TestCase):

    def setUp(self):
        """Set up the test case with a sample dataset."""
        self.file_path = 'dataset.csv'  # Path to your dataset
        # You can create a sample dataset for testing or ensure the actual dataset exists.

    def test_load_dataset(self):
        """Test that the dataset can be loaded into a DataFrame."""
        try:
            data = pd.read_csv(self.file_path)
            self.assertIsInstance(data, pd.DataFrame, "Data should be loaded into a DataFrame.")
        except FileNotFoundError:
            self.fail(f"Dataset file '{self.file_path}' not found.")

    def test_display_rows(self):
        """Test that the first few rows of the DataFrame can be displayed."""
        data = pd.read_csv(self.file_path)
        displayed_rows = data.head()  # Display first few rows
        self.assertFalse(displayed_rows.empty, "The displayed rows should not be empty.")


if __name__ == "__main__":
    unittest.main()
