import unittest
from unittest import TestCase
import Direction


class TestDirection(TestCase):
    def test_validirection(self):
        self.assertTrue(Direction.Direction.validatedirection("NORTH"))

    def test_invalidirection(self):
        self.assertFalse(Direction.Direction.validatedirection("NORTEH"))

    def test_getindexfromstring(self):
        self.assertEquals(Direction.Direction.getdirectionindex("NORTH"),1)

    def test_getstringfromindex(self):
        self.assertEquals(Direction.Direction.getdirection(1),"NORTH")


if __name__ == '__main__':
    unittest.main()
