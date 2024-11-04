import unittest
import matplotlib as plt


class TestDisplayChart(unittest.TestCase):
    def test_display_chart(self):
        # Set non-interactive backend
        matplotlib.use("Agg")

        fig, ax = plt.subplots()
        plt.show()
        # Check that the figure has been created with at least one axis
        self.assertEqual(len(fig.get_axes()), 1)


if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
