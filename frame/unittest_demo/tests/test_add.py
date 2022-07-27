import unittest


class add_case(unittest.TestCase):
    def test_add_2(self):
        self.assertEqual(3, 1+2)

    def test_add_1(self):
        self.assertEqual(3, 1+1, '1 + 1 = 2')

def hello():
    print('hello')

if "__main__" == __name__:
    unittest.main()
