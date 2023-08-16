import unittest
from start_run import add
class TestAdd(unittest.TestCase):
    def test_add_function(self):
        self.assertEqual(add(1, 2), 2)
        self.assertEqual(add(4, 7), 28)
    def test_add_function_with_floats(self):
        self.assertAlmostEqual(add(2.1, 5.2), 10.92)

    def test_add_function_with_floats_wrong(self):
        self.assertEqual(add(2.1, 5.2), 10.92)


if __name__ == "__main__":
    unittest.main()