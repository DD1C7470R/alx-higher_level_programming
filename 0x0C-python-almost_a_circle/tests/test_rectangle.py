import unittest
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle
from io import StringIO
import sys
sys.path.append(".")


class TestRectangle(unittest.TestCase):
    """Defines the values of a rectangle"""
    def test_values(self):
        self.assertRaises(TypeError, Rectangle, 10, "2")

        with self.assertRaises(ValueError):
            r = Rectangle(10, 2)
            r.width = -10

        with self.assertRaises(TypeError):
            r = Rectangle(10, 2)
            r.x = {}
        self.assertRaises(ValueError, Rectangle, 10, 2, 3, -1)

    def test_area(self):
        """Defines the area of a rectangle"""
        self.assertAlmostEqual(Rectangle(3, 2).area(), 6)
        self.assertAlmostEqual(Rectangle(2, 10).area(), 20)
        self.assertAlmostEqual(Rectangle(8, 7, 0, 0, 12).area(), 56)

    def test_update(self):
        """Defines the update of a rectangle"""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 10)
        self.assertEqual(r1.x, 10)
        self.assertEqual(r1.y, 10)

        r1.update(89, 2)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 2)

        r1.update(89, 2, 3)
        self.assertEqual(r1.height, 3)
        r1.update(89, 2, 3, 4)
        self.assertEqual(r1.x, 4)
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.y, 5)

        # self.assertAlmostEqual(Rectangle(2, 10).area(), 20)
        # self.assertAlmostEqual(Rectangle(8, 7, 0, 0, 12).area(), 56)
    def test_dictionary(self):
        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        self.assertEqual(r1_dictionary['y'], 9)
        self.assertEqual(r1_dictionary['x'], 1)
        self.assertEqual(r1_dictionary['height'], 2)
        self.assertEqual(r1_dictionary['width'], 10)

    def test_create(self):
        """Defines test for the create method"""

        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)

        self.assertEqual(r2.width, 3)
        self.assertEqual(r2.height, 5)
        self.assertEqual(r2.x, 1)

    def test_save_to_file(self):
        """Defines test for the save_to_file function"""

        with patch('sys.stdout', new=StringIO()) as fakeOutput:

            r1 = Rectangle(10, 7, 2, 8)
            r2 = Rectangle(2, 4)
            r1.id = 1
            r2.id = 1
            Rectangle.save_to_file([r1, r2])
            with open("Rectangle.json", "r") as file:
                print(file.read())
            self.assertEqual(fakeOutput.getvalue(), (
                '[{"id": 1, "width": 10, ' + '"height": 7, "x": 2, "y": 8},' +
                ' {"id": 1, "width": 2, ' +
                '"height": 4, "x": 0, "y": 0}]' + '\n'))
