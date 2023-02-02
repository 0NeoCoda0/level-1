import unittest


class TestFunction(unittest.TestCase):

    def test_is_power_of_three(self):
        self.assertEqual(is_power_of_three(81), True)
        self.assertEqual(is_power_of_three(80), False)

def is_power_of_three(x):
    i = 0
    while 3 ** i <= x:
        if x == 3 ** i:
            return True
        i += 1
    return False

if __name__ == '__main__':
    unittest.main()