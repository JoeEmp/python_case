import unittest
import time

class sub_case(unittest.TestCase):
    def test_sub_2(self):
        self.assertEqual(-1, 1-2)

    def test_sub_1(self):
        time.sleep(5)
        self.assertEqual(1, 1-1, '1-1 = 0')


    @unittest.skip('debug')
    def test_sub_0(self):
        self.assertEqual(1, 1-0, '1-0= 1')

if "__main__" == __name__:
    unittest.main(verbosity=2,catchbreak=True)
