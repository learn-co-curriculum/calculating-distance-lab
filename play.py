import unittest
from ipynb.fs.full.distancelab import what_now, test_distance

class TestDistance(unittest.TestCase):
    def test_isupper(self):
        self.assertTrue(test_distance())
        # self.assertFalse()

if __name__ == '__main__':
    unittest.main()
