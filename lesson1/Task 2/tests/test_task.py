import unittest

class TestLibraryImports(unittest.TestCase):

    def test_pandas_import(self):
        """Test that the pandas library can be imported."""
        try:
            import pandas as pd
        except ImportError:
            self.fail("pandas library is not installed.")

    def test_matplotlib_import(self):
        """Test that the matplotlib library can be imported."""
        try:
            import matplotlib.pyplot as plt
        except ImportError:
            self.fail("matplotlib library is not installed.")

if __name__ == "__main__":
    unittest.main()
