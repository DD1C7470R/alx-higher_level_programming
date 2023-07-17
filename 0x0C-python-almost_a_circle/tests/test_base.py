#!/usr/bin/python3

""" Defines test for base class
"""
import unittest
from models.base import Base
import sys
sys.path.append(".")


class TestBaseClass(unittest.TestCase):
    """Defines test for the Base class"""
    def test_values(self):
        """Test the id of a Base"""
        self.assertAlmostEqual(Base().id, 1)
        self.assertAlmostEqual(Base().id, 2)
        self.assertAlmostEqual(Base().id, 3)
        self.assertAlmostEqual(Base(12).id, 12)
        self.assertAlmostEqual(Base().id, 4)
