import unittest2 as unittest
from ipynb.fs.full.distancelab import (students,
fred, daniel, street_distance, avenue_distance,
distance_between_students_squared, distance, distance_with_student,
distance_all, nearest_neighbors)

class TestDistance(unittest.TestCase):
    def test_street_distance(self):
        self.assertEqual(street_distance(fred, daniel), 3)

    def test_avenue_distance(self):
        self.assertEqual(avenue_distance(fred, daniel), 3)

    def test_distance_between_students_squared(self):
        self.assertEqual(distance_between_students_squared(fred, daniel), 4)

    def test_distance(self):
        self.assertEqual(distance(fred, daniel), 2)

    def test_distance_with_student(self):
        self.assertEqual(distance_with_student(fred, daniel), {'avenue': 5, 'distance': 2.0, 'name': 'daniel', 'street': 1})

    def test_distance_all(self):
        self.assertEqual(distance_all(fred, students), [{'avenue': 5, 'distance': 2.0, 'name': 'daniel', 'street': 1},
            {'avenue': 6, 'distance': 2.0, 'name': 'rachel', 'street': 2},
            {'avenue': 10, 'distance': 1.4142135623730951, 'name': 'steven', 'street': 4}])

    def test_nearest_neighbors(self):
        self.assertEqual(nearest_neighbors(fred, students, 2), [{'avenue': 10, 'distance': 1.4142135623730951, 'name': 'steven', 'street': 4},
            {'avenue': 5, 'distance': 2.0, 'name': 'daniel', 'street': 1}])


unittest.main()
