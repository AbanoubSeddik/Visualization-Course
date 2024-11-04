import unittest
import matplotlib.pyplot as plt


class TestLabelsAndLegend(unittest.TestCase):
    def test_labels_and_legend(self):
        fig, ax = plt.subplots()
        genres = ["Action", "Adventure", "RPG"]
        platforms = ["PS4", "XOne", "PC", "WiiU"]
        bar_width = 0.2
        platform_positions = range(len(genres))

        # Set x-ticks
        ax.set_xticks([pos + bar_width for pos in platform_positions])
        ax.set_xticklabels(genres)

        # Set axis labels
        ax.set_xlabel("Genre")
        ax.set_ylabel("Number of Games")

        # Add legend
        ax.legend(title="Platform")

        # Check x-axis label
        self.assertEqual(ax.get_xlabel(), "Genre")
        # Check y-axis label
        self.assertEqual(ax.get_ylabel(), "Number of Games")
        # Check x-tick labels match genres
        self.assertEqual([tick.get_text() for tick in ax.get_xticklabels()], genres)
        # Check if legend title is set correctly
        self.assertEqual(ax.get_legend().get_title().get_text(), "Platform")


if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
