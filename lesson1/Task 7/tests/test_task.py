import unittest
import matplotlib.pyplot as plt


class TestPlotSetup(unittest.TestCase):
    def test_figure_and_axis_creation(self):
        fig, ax = plt.subplots(figsize=(10, 6))
        # Check if the figure and axis were created
        self.assertIsNotNone(fig)
        self.assertIsNotNone(ax)
        # Check if the figure size is set correctly
        self.assertEqual(fig.get_size_inches().tolist(), [10, 6])

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
