import unittest
import matplotlib.pyplot as plt
from task import genre_platform_counts


class TestPlotBars(unittest.TestCase):
    def test_plot_bars(self):
        platforms = genre_platform_counts.columns
        bar_width = 0.2
        fig, ax = plt.subplots()

        for i, platform in enumerate(platforms):
            bar_positions = [pos + i * bar_width for pos in range(len(genre_platform_counts.index))]
            ax.bar(bar_positions, genre_platform_counts[platform], width=bar_width, label=platform)

        self.assertEqual(len(ax.patches), len(platforms) * len(genre_platform_counts.index))
        for bar in ax.patches:
            self.assertAlmostEqual(bar.get_width(), bar_width)


if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
