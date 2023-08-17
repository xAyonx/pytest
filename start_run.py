import unittest
from start import add

class TestAdd(unittest.TestCase):
    def test_add_function(self):
        self.assertEqual(add(5, 5), 25)

    


if __name__ == "__main__":
    unittest.main()