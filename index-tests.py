import unittest2 as unittest
from ipynb.fs.full.index import (neighbors,
fred, natalie, street_distance, avenue_distance,
distance_between_neighbors_squared, distance, distance_with_neighbor,
distance_all, nearest_neighbors)

class TestDistance(unittest.TestCase):
    def test_street_distance(self):
        self.assertEqual(street_distance(fred, natalie), 4)

    def test_avenue_distance(self):
        self.assertEqual(avenue_distance(fred, natalie), 1)

    def test_distance_between_neighbors_squared(self):
        self.assertEqual(distance_between_neighbors_squared(fred, natalie), 17)

    def test_distance(self):
        self.assertEqual(distance(fred, natalie), 4.123105625617661)

    def test_distance_with_neighbor(self):
        self.assertEqual(distance_with_neighbor(fred, natalie), {'avenue': 5, 'distance': 4.123105625617661, 'name': 'Natalie', 'street': 4})

    def test_distance_all(self):
        self.assertEqual(distance_all(fred, neighbors), [{'avenue': 1, 'distance': 4.242640687119285, 'name': 'Suzie', 'street': 11},
             {'avenue': 5, 'distance': 1.0, 'name': 'Bob', 'street': 8},
             {'avenue': 6, 'distance': 5.385164807134504, 'name': 'Edgar', 'street': 13},
             {'avenue': 3, 'distance': 2.23606797749979, 'name': 'Steven', 'street': 6},
             {'avenue': 5, 'distance': 4.123105625617661, 'name': 'Natalie', 'street': 4}])

    def test_nearest_neighbors(self):
        self.assertEqual(nearest_neighbors(fred, neighbors, 2), [{'avenue': 5, 'distance': 1.0, 'name': 'Bob', 'street': 8},
            {'avenue': 3, 'distance': 2.23606797749979, 'name': 'Steven', 'street': 6}])
