import unittest



class TestBarWidthAndPositions(unittest.TestCase):
    def test_bar_width_and_positions(self):
        bar_width = 0.2
        genres = ["Action", "Adventure", "RPG"]  # Example genre list
        platform_positions = range(len(genres))

        # Check bar width
        self.assertEqual(bar_width, 0.2)
        # Check platform positions have correct length
        self.assertEqual(len(platform_positions), len(genres))
        # Check platform_positions is a range object starting from 0
        self.assertEqual(list(platform_positions), [0, 1, 2])


if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
