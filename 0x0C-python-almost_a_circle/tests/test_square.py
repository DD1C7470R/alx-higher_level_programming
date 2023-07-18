import unittest
from models.square import Square
import io
from models.base import Base
import sys
sys.path.append(".")


class TestSquare(unittest.TestCase):
    """Defines the values of a rectangle"""
    def test_values(self):
        self.assertRaises(TypeError, Square, 10, "2")

        with self.assertRaises(ValueError):
            r = Square(10, 2)
            r.width = -10

        with self.assertRaises(TypeError):
            r = Square(10, 2)
            r.x = {}
        self.assertRaises(ValueError, Square, 10, 2, -3)

    # def test_area(self):
    #     """Defines the area of a rectangle"""
    #     self.assertAlmostEqual(Rectangle(3, 2).area(), 6)
    #     self.assertAlmostEqual(Rectangle(2, 10).area(), 20)
    #     self.assertAlmostEqual(Rectangle(8, 7, 0, 0, 12).area(), 56)

    def test_size_mutator(self):
        s1 = Square(5)
        self.assertEqual(s1.width, 5)
        s1.size = 10
        self.assertEqual(s1.width, 10)

        with self.assertRaises(TypeError):
            s1.size = "10"
        with self.assertRaises(ValueError):
            s1.size = -10

    def test_update(self):
        """Defines the update of a Square"""
        r1 = Square(5)
        r1.update(10)
        self.assertEqual(r1.id, 10)
        self.assertEqual(r1.size, 5)
        r1.update(1, 2)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.size, 2)
        r1.update(1, 2, 3)
        self.assertEqual(r1.x, 3)
        r1.update(1, 2, 3, 4)
        self.assertEqual(r1.y, 4)
        r1.update(x=12)
        self.assertEqual(r1.x, 12)
        r1.update(size=7, y=1)
        self.assertEqual(r1.size, 7)
        self.assertEqual(r1.y, 1)
        r1.update(size=7, id=89, y=1)
        self.assertEqual(r1.size, 7)
        self.assertEqual(r1.y, 1)
        self.assertEqual(r1.id, 89)
